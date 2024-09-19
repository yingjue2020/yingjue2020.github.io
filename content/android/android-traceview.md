Title: Android traceview 原理分析
Date: 2019-04-24 14:04:01
Modified: 2019-04-24 14:04:01
Category: Android
Tags: Android, Instrumentation
Slug: android-traceview

# 使用方法

目标进程需要打开调试开关,android:debuggable=true
```shell
adb shell am profile start com.tencent.mm /data/local/tmp/1.trace
adb shell am profile stop com.tencent.mm
adb pull /data/local/tmp/1.trace
~/adt-2014/sdk/tools/traceview 1.trace
```

# 文件格式
http://androidxref.com/6.0.1_r10/xref/art/runtime/trace.h
```c++
enum TracingMode {
  kTracingInactive,
  kMethodTracingActive,
  kSampleProfilingActive,
};
// File format:
//     header
//     record 0
//     record 1
//     ...
//
// Header format:
//     u4  magic ('SLOW')
//     u2  version
//     u2  offset to data
//     u8  start date/time in usec
//     u2  record size in bytes (version >= 2 only)
//     ... padding to 32 bytes
//
// Record format v1:
//     u1  thread ID
//     u4  method ID | method action
//     u4  time delta since start, in usec
//
// Record format v2:
//     u2  thread ID
//     u4  method ID | method action
//     u4  time delta since start, in usec
//
// Record format v3:
//     u2  thread ID
//     u4  method ID | method action
//     u4  time delta since start, in usec
//     u4  wall time since start, in usec (when clock == "dual" only)
//
// 32 bits of microseconds is 70 minutes.
//
// All values are stored in little-endian order.
enum TraceAction {
    kTraceMethodEnter = 0x00,       // method entry
    kTraceMethodExit = 0x01,        // method exit
    kTraceUnroll = 0x02,            // method exited by exception unrolling
    // 0x03 currently unused
    kTraceMethodActionMask = 0x03,  // two bits
};

```

# 原理解析
Android 6.0.1
- 服务进程
http://androidxref.com/6.0.1_r10/xref/frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java#19543

```Java
public boolean profileControl(
    String process,
    int userId,
    boolean start,
    ProfilerInfo profilerInfo,
    int profileType
    ) throws RemoteException{
    // ...
    ProcessRecord proc = null;
    if (process != null){
        proc = findProcessLocked(process,userId,"profileControl");
    }
    // ...
    if (start){
        // ...
        proc.thread.profileControl(start,profilerInfo,profileType);
    }
    // ...

}
```
- 目标进程
http://androidxref.com/6.0.1_r10/xref/frameworks/base/core/java/android/app/ActivityThread.java#914
```Java
public void proilerControl(boolean start,ProfilerInfo profilerInfo, int profileType) {
    sendMessage(H.PROFILER_CONTROL, profilerInfo, start ? 1 : 0, profileType);
}
```

http://androidxref.com/6.0.1_r10/xref/frameworks/base/core/java/android/app/ActivityThread.java#handleProfilerControl
```Java
final void handleProfilerControl(boolean start, ProfilerInfo profilerInfo, int profileType){
    if (start){
        mProfiler.startProfiling();
    }else{
        mProfiler.stopProfiling();
    }
}
```

http://androidxref.com/6.0.1_r10/xref/frameworks/base/core/java/android/app/ActivityThread.java#startProfiling
http://androidxref.com/6.0.1_r10/xref/libcore/dalvik/src/main/java/dalvik/system/VMDebug.java
```Java
public void startProfiling(){
    VMDebug.startMethodTracing(profileFile, profileFd.getFileDescriptor(),
        8 * 1024 * 1024, 0, samplingInterval != 0, samplingInterval);
}
```
- Native

http://androidxref.com/6.0.1_r10/xref/art/runtime/native/dalvik_system_VMDebug.cc#116
```c++
static void VMDebug_startMethodTracingFilename(JNIEnv* env, jclass, jstring javaTraceFilename,
    jint bufferSize, jint flags,
    jboolean samplingEnabled, jint intervalUs){

    }
```
