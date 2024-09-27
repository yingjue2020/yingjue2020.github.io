Title: The Implementation Details of Android's force-stop
Date: 2019-06-26 18:32:15
Modified: 2019-06-26 18:32:15
Category: Android
Tags: Android, AOSP
Slug: the implementation-details-of-android-force-stop
Figure: android.png

基于AOSP 8.0.1源码分析force-stop的实现细节。

# 使用 force-stop
```shell
am force-stop com.example
```
com.example 是应用程序包名。

# am命令
```shell
cat /system/bin/am
#!/system/bin/sh
if [ "$1" != "instrument" ] ; then
    cmd activity "$@"
else
    base=/system
    export CLASSPATH=$base/framework/am.jar
    exec app_process $base/bin com.android.commands.am.Am "$@"
fi
```
am 是一个shell脚本。如果第一个参数不等于"instrument"，就执行cmd activity。

# cmd 命令
```shell
am force-stop com.example
```
相当于
```shell
cmd activity force-stop com.example
```
查看cmd是个什么文件？
```shell
cd /system/bin
file cmd
cmd: ELF shared object, 64-bit LSB arm64, dynamic (/system/bin/linker64), for Android 27, BuildID=684237e221655418caf713b8cedf9382, stripped
```
可以看出cmd是一个ELF可执行文件。
源码文件：frameworks/native/cmds/cmd/cmd.cpp
```c++
int main(int argc, char* const argv[]){
    // ...
    sp<IServiceManager> sm = defaultServiceManager();
    // ...
    Vector<String16> args;
    for (int i=2; i<argc; i++) {
        args.add(String16(argv[i]));
    }
    String16 cmd = String16(argv[1]);
    sp<IBinder> service = sm->checkService(cmd);

    // ...
    sp<MyShellCallback> cb = new MyShellCallback();
    sp<MyResultReceiver> result = new MyResultReceiver();

    // ...
    // TODO: block until a result is returned to MyResultReceiver.
    status_t err = IBinder::shellCommand(service, STDIN_FILENO, STDOUT_FILENO, STDERR_FILENO, args,
            cb, result);

    // ...
}
```
args[1]  表示服务名。
通过ServiceManager找到对应的服务，比如第1个参数是activity，找到服务ActivityManagerService。
然后调用IBinder::shellCommand()。

# IBinder::shellCommand
frameworks/native/libs/binder/Binder.cpp
```c++
status_t IBinder::shellCommand(const sp<IBinder>& target, int in, int out, int err,
    Vector<String16>& args, const sp<IShellCallback>& callback,
    const sp<IResultReceiver>& resultReceiver)
{
    Parcel send;
    Parcel reply;
    send.writeFileDescriptor(in);
    send.writeFileDescriptor(out);
    send.writeFileDescriptor(err);
    const size_t numArgs = args.size();
    send.writeInt32(numArgs);
    for (size_t i = 0; i < numArgs; i++) {
        send.writeString16(args[i]);
    }
    send.writeStrongBinder(callback != NULL ? IInterface::asBinder(callback) : NULL);
    send.writeStrongBinder(resultReceiver != NULL ? IInterface::asBinder(resultReceiver) : NULL);
    return target->transact(SHELL_COMMAND_TRANSACTION, send, &reply);
}
```
这个函数比较简单，构造一个Parcel 执行SHELL_COMMAND_TRANSCTION。

# AMS::onShellCommand
frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java
```java
public class ActivityManagerService extends IActivityManager.Stub
        implements Watchdog.Monitor, BatteryStatsImpl.BatteryCallback {
    @Override
    public void onShellCommand(FileDescriptor in, FileDescriptor out,
            FileDescriptor err, String[] args, ShellCallback callback,
            ResultReceiver resultReceiver) {
        (new ActivityManagerShellCommand(this, false)).exec(
                this, in, out, err, args, callback, resultReceiver);
    }
}
```
exec函数在ShellCommand类里实现，最终会调用ActivityManagerShellCommand的onCommand函数。

# ActivityManagerShellCommand::onCommand
frameworks/base/services/core/java/com/android/server/am/ActivityManagerShellCommand.java
frameworks/base/core/java/android/os/ShellCommand.java
```java
@Override
public int onCommand(String cmd) {
    // ...
    case "force-stop":
        return runForceStop(pw);
    // ...
}
```
runForceStop
```java
int runForceStop(PrintWriter pw) throws RemoteException {
    int userId = UserHandle.USER_ALL;

    String opt;
    while ((opt = getNextOption()) != null) {
        if (opt.equals("--user")) {
            userId = UserHandle.parseUserArg(getNextArgRequired());
        } else {
            getErrPrintWriter().println("Error: Unknown option: " + opt);
            return -1;
        }
    }
    mInterface.forceStopPackage(getNextArgRequired(), userId);
    return 0;
}
```
从ActivityManagerShellCommand的构造函数中发现mInterface表示ActivityManagerService。

# forceStopPackage
frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java
```java
@Override
public void forceStopPackage(final String packageName, int userId) {
    if (checkCallingPermission(android.Manifest.permission.FORCE_STOP_PACKAGES)
            != PackageManager.PERMISSION_GRANTED) {
        String msg = "Permission Denial: forceStopPackage() from pid="
                + Binder.getCallingPid()
                + ", uid=" + Binder.getCallingUid()
                + " requires " + android.Manifest.permission.FORCE_STOP_PACKAGES;
        Slog.w(TAG, msg);
        throw new SecurityException(msg);
    }
    final int callingPid = Binder.getCallingPid();
    userId = mUserController.handleIncomingUser(callingPid, Binder.getCallingUid(),
            userId, true, ALLOW_FULL_ONLY, "forceStopPackage", null);
    long callingId = Binder.clearCallingIdentity();
    try {
        IPackageManager pm = AppGlobals.getPackageManager();
        synchronized(this) {
            int[] users = userId == UserHandle.USER_ALL
                    ? mUserController.getUsers() : new int[] { userId };
            for (int user : users) {
                int pkgUid = -1;
                try {
                    pkgUid = pm.getPackageUid(packageName, MATCH_DEBUG_TRIAGED_MISSING,
                            user);
                } catch (RemoteException e) {
                }
                if (pkgUid == -1) {
                    Slog.w(TAG, "Invalid packageName: " + packageName);
                    continue;
                }
                try {
                    // 关键点1
                    pm.setPackageStoppedState(packageName, true, user);
                } catch (RemoteException e) {
                } catch (IllegalArgumentException e) {
                    Slog.w(TAG, "Failed trying to unstop package "
                            + packageName + ": " + e);
                }
                if (mUserController.isUserRunningLocked(user, 0)) {
                    // 关键点2
                    forceStopPackageLocked(packageName, pkgUid, "from pid " + callingPid);
                    finishForceStopPackageLocked(packageName, pkgUid);
                }
            }
        }
    } finally {
        Binder.restoreCallingIdentity(callingId);
    }
}
```
这个函数的参数packageName 表示被杀进程的包名， userId值为UserHandle.USER_ALL。

## setPackageStoppedState
frameworks/base/services/core/java/com/android/server/pm/PackageManagerService.java
```java
@Override
public void setPackageStoppedState(String packageName, boolean stopped, int userId) {
    if (!sUserManager.exists(userId)) return;
    final int callingUid = Binder.getCallingUid();
    if (getInstantAppPackageName(callingUid) != null) {
        return;
    }
    final int permission = mContext.checkCallingOrSelfPermission(
            android.Manifest.permission.CHANGE_COMPONENT_ENABLED_STATE);
    final boolean allowedByPermission = (permission == PackageManager.PERMISSION_GRANTED);
    enforceCrossUserPermission(callingUid, userId,
            true /* requireFullPermission */, true /* checkShell */, "stop package");
    // writer
    synchronized (mPackages) {
        final PackageSetting ps = mSettings.mPackages.get(packageName);
        if (!filterAppAccessLPr(ps, callingUid, userId)
                && mSettings.setPackageStoppedStateLPw(this, packageName, stopped,
                        allowedByPermission, callingUid, userId)) {
            scheduleWritePackageRestrictionsLocked(userId);
        }
    }
}
```
如果需要启动处于停止状态的应用，则只要为Intent添加 FLAG_INCLUDE_STOPPED_PACKAGES 标记即可。

# forceStopPackageLocked
```java
private void forceStopPackageLocked(final String packageName, int uid, String reason) {
    forceStopPackageLocked(packageName, UserHandle.getAppId(uid), false,
            false, true, false, false, UserHandle.getUserId(uid), reason);
}
final boolean forceStopPackageLocked(
    String packageName, 
    int appId,
    boolean callerWillRestart, // false
    boolean purgeCache,        // false
    boolean doit,              // true
    boolean evenPersistent,    // false
    boolean uninstalling,      // false
    int userId, 
    String reason
    ) {
    int i;

    if (userId == UserHandle.USER_ALL && packageName == null) {
        Slog.w(TAG, "Can't force stop all processes of all users, that is insane!");
    }

    if (appId < 0 && packageName != null) {
        try {
            appId = UserHandle.getAppId(AppGlobals.getPackageManager()
                    .getPackageUid(packageName, MATCH_DEBUG_TRIAGED_MISSING, 0));
        } catch (RemoteException e) {
        }
    }

    if (doit) {
        if (packageName != null) {
            Slog.i(TAG, "Force stopping " + packageName + " appid=" + appId
                    + " user=" + userId + ": " + reason);
        } else {
            Slog.i(TAG, "Force stopping u" + userId + ": " + reason);
        }

        mAppErrors.resetProcessCrashTimeLocked(packageName == null, appId, userId);
    }

    // 清理 Processes
    boolean didSomething = killPackageProcessesLocked(packageName, appId, userId,
            ProcessList.INVALID_ADJ, callerWillRestart, true, doit, evenPersistent,
            packageName == null ? ("stop user " + userId) : ("stop " + packageName));

    didSomething |= mActivityStarter.clearPendingActivityLaunchesLocked(packageName);

    // 清理 Activities
    if (mStackSupervisor.finishDisabledPackageActivitiesLocked(
            packageName, null, doit, evenPersistent, userId)) {
        if (!doit) {
            return true;
        }
        didSomething = true;
    }

    // 清理 Services
    if (mServices.bringDownDisabledPackageServicesLocked(
            packageName, null, userId, evenPersistent, true, doit)) {
        if (!doit) {
            return true;
        }
        didSomething = true;
    }

    if (packageName == null) {
        // Remove all sticky broadcasts from this user.
        mStickyBroadcasts.remove(userId);
    }

    ArrayList<ContentProviderRecord> providers = new ArrayList<>();
    if (mProviderMap.collectPackageProvidersLocked(packageName, null, doit, evenPersistent,
            userId, providers)) {
        if (!doit) {
            return true;
        }
        didSomething = true;
    }
    // 清理 Providers
    for (i = providers.size() - 1; i >= 0; i--) {
        removeDyingProviderLocked(null, providers.get(i), true);
    }

    // 移除APP申请的临时权限
    // Remove transient permissions granted from/to this package/user
    removeUriPermissionsForPackageLocked(packageName, userId, false);

    if (doit) {
        //  清理 Broadcast
        for (i = mBroadcastQueues.length - 1; i >= 0; i--) {
            didSomething |= mBroadcastQueues[i].cleanupDisabledPackageReceiversLocked(
                    packageName, null, userId, doit);
        }
    }

    if (packageName == null || uninstalling) {
        // Remove pending intents.  For now we only do this when force
        // stopping users, because we have some problems when doing this
        // for packages -- app widgets are not currently cleaned up for
        // such packages, so they can be left with bad pending intents.
        if (mIntentSenderRecords.size() > 0) {
            Iterator<WeakReference<PendingIntentRecord>> it
                    = mIntentSenderRecords.values().iterator();
            while (it.hasNext()) {
                WeakReference<PendingIntentRecord> wpir = it.next();
                if (wpir == null) {
                    it.remove();
                    continue;
                }
                PendingIntentRecord pir = wpir.get();
                if (pir == null) {
                    it.remove();
                    continue;
                }
                if (packageName == null) {
                    // Stopping user, remove all objects for the user.
                    if (pir.key.userId != userId) {
                        // Not the same user, skip it.
                        continue;
                    }
                } else {
                    if (UserHandle.getAppId(pir.uid) != appId) {
                        // Different app id, skip it.
                        continue;
                    }
                    if (userId != UserHandle.USER_ALL && pir.key.userId != userId) {
                        // Different user, skip it.
                        continue;
                    }
                    if (!pir.key.packageName.equals(packageName)) {
                        // Different package, skip it.
                        continue;
                    }
                }
                if (!doit) {
                    return true;
                }
                didSomething = true;
                it.remove();
                makeIntentSenderCanceledLocked(pir);
                if (pir.key.activity != null && pir.key.activity.pendingResults != null) {
                    pir.key.activity.pendingResults.remove(pir.ref);
                }
            }
        }
    }

    if (doit) {
        if (purgeCache && packageName != null) {
            AttributeCache ac = AttributeCache.instance();
            if (ac != null) {
                ac.removePackage(packageName);
            }
        }
        if (mBooted) {
            // 恢复 Activity栈
            mStackSupervisor.resumeFocusedStackTopActivityLocked();
            mStackSupervisor.scheduleIdleLocked();
        }
    }

    return didSomething;
}
```

# Process
## AMS.killPackageProcessesLocked
```java
private final boolean killPackageProcessesLocked(
    String packageName, 
    int appId,
    int userId, 
    int minOomAdj, // static final int INVALID_ADJ = -10000;
    boolean callerWillRestart, // false
    boolean allowRestart,      // true
    boolean doit,              // true
    boolean evenPersistent,    // false
    String reason
    ) {
    ArrayList<ProcessRecord> procs = new ArrayList<>();

    // Remove all processes this package may have touched: all with the
    // same UID (except for the system or root user), and all whose name
    // matches the package name.
    final int NP = mProcessNames.getMap().size();
    for (int ip=0; ip<NP; ip++) {
        SparseArray<ProcessRecord> apps = mProcessNames.getMap().valueAt(ip);
        final int NA = apps.size();
        for (int ia=0; ia<NA; ia++) {
            ProcessRecord app = apps.valueAt(ia);
            if (app.persistent && !evenPersistent) {
                // we don't kill persistent processes
                continue;
            }
            if (app.removed) {
                if (doit) {
                    procs.add(app);
                }
                continue;
            }

            // Skip process if it doesn't meet our oom adj requirement.
            if (app.setAdj < minOomAdj) {
                continue;
            }

            // If no package is specified, we call all processes under the
            // give user id.
            if (packageName == null) {
                if (userId != UserHandle.USER_ALL && app.userId != userId) {
                    continue;
                }
                if (appId >= 0 && UserHandle.getAppId(app.uid) != appId) {
                    continue;
                }
            // Package has been specified, we want to hit all processes
            // that match it.  We need to qualify this by the processes
            // that are running under the specified app and user ID.
            } else {
                final boolean isDep = app.pkgDeps != null
                        && app.pkgDeps.contains(packageName);
                if (!isDep && UserHandle.getAppId(app.uid) != appId) {
                    continue;
                }
                if (userId != UserHandle.USER_ALL && app.userId != userId) {
                    continue;
                }
                if (!app.pkgList.containsKey(packageName) && !isDep) {
                    continue;
                }
            }

            // Process has passed all conditions, kill it!
            if (!doit) {
                return true;
            }
            app.removed = true;
            procs.add(app);
        }
    }

    int N = procs.size();
    for (int i=0; i<N; i++) {
        removeProcessLocked(procs.get(i), callerWillRestart, allowRestart, reason);
    }
    updateOomAdjLocked();
    return N > 0;
}
```

## removeProcessLocked
```java
boolean removeProcessLocked(ProcessRecord app,
        boolean callerWillRestart, boolean allowRestart, String reason) {
    final String name = app.processName;
    final int uid = app.uid;
    if (DEBUG_PROCESSES) Slog.d(TAG_PROCESSES,
        "Force removing proc " + app.toShortString() + " (" + name + "/" + uid + ")");

    ProcessRecord old = mProcessNames.get(name, uid);
    if (old != app) {
        // This process is no longer active, so nothing to do.
        Slog.w(TAG, "Ignoring remove of inactive process: " + app);
        return false;
    }
    removeProcessNameLocked(name, uid);
    if (mHeavyWeightProcess == app) {
        mHandler.sendMessage(mHandler.obtainMessage(CANCEL_HEAVY_NOTIFICATION_MSG,
                mHeavyWeightProcess.userId, 0));
        mHeavyWeightProcess = null;
    }
    boolean needRestart = false;
    if (app.pid > 0 && app.pid != MY_PID) {
        int pid = app.pid;
        synchronized (mPidsSelfLocked) {
            mPidsSelfLocked.remove(pid);
            mHandler.removeMessages(PROC_START_TIMEOUT_MSG, app);
        }
        mBatteryStatsService.noteProcessFinish(app.processName, app.info.uid);
        boolean willRestart = false;
        if (app.persistent && !app.isolated) {
            if (!callerWillRestart) {
                willRestart = true;
            } else {
                needRestart = true;
            }
        }

        // 杀进程
        app.kill(reason, true);
        if (app.isolated) {
            mBatteryStatsService.removeIsolatedUid(app.uid, app.info.uid);
            getPackageManagerInternalLocked().removeIsolatedUid(app.uid);
        }
        handleAppDiedLocked(app, willRestart, allowRestart);
        if (willRestart) {
            removeLruProcessLocked(app);
            addAppLocked(app.info, null, false, null /* ABI override */);
        }
    } else {
        mRemovedProcesses.add(app);
    }

    return needRestart;
}
```

# finishForceStopPackageLocked
```java
private void finishForceStopPackageLocked(final String packageName, int uid) {
    Intent intent = new Intent(Intent.ACTION_PACKAGE_RESTARTED,
            Uri.fromParts("package", packageName, null));
    if (!mProcessesReady) {
        intent.addFlags(Intent.FLAG_RECEIVER_REGISTERED_ONLY
                | Intent.FLAG_RECEIVER_FOREGROUND);
    }
    intent.putExtra(Intent.EXTRA_UID, uid);
    intent.putExtra(Intent.EXTRA_USER_HANDLE, UserHandle.getUserId(uid));
    broadcastIntentLocked(null, null, intent,
            null, null, 0, null, null, null, AppOpsManager.OP_NONE,
            null, false, false, MY_PID, SYSTEM_UID, UserHandle.getUserId(uid));
}
```
清理完与包名相关的进程后，会发送一个ACTION_PACKAGE_RESTARTED广播。

# References
http://gityuan.com/2014/01/04/get-service/
