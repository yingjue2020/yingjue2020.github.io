Title: Android 8.1 源码分析：PackageInstaller
Date: 2019-08-22 10:00:24
Modified: 2019-08-22 10:00:24
Category: Android
Tags: AOSP
Slug: read-source-code-packageinstaller
Figure: android.png

## PackageInstallerSession
源码位置：[PackageInstallerSession.java](http://androidxref.com/8.1.0_r33/xref/frameworks/base/services/core/java/com/android/server/pm/PackageInstallerSession.java) 。

### commit
{% include_code lang:java from:689 to:750 aosp/8.1/frameworks/base/services/core/java/com/android/server/pm/PackageInstallerSession.java %}
该方法主要发送了一个MSG_COMMIT消息。下面看Handler如何处理这个消息。

### Handler.Callback
{% include_code lang:java from:275 to:303 aosp/8.1/frameworks/base/services/core/java/com/android/server/pm/PackageInstallerSession.java %}
处理MSG_COMMIT消息非常简单，关键方法是commitLocked。

### commitLocked
{% include_code lang:java from:841 to:946 aosp/8.1/frameworks/base/services/core/java/com/android/server/pm/PackageInstallerSession.java %}
至此PackageInstallerSession的工作就完成了，余下的工作交由PMS来完成。

#### needToAskForPermissionsLocked
{% include_code lang:java from:324 to:340 aosp/8.1/frameworks/base/services/core/java/com/android/server/pm/PackageInstallerSession.java %}


## PackageManagerServices
### installStage
{% include_code lang:java from:14931 to:14967 aosp/8.1/frameworks/base/services/core/java/com/android/server/pm/PackageManagerService.java %}

### MSG:INIT_COPY
