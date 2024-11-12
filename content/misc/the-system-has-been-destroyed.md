Title: The system has been destroyed
Date: 2024-11-12 10:33:00
Modified: 2024-11-12 10:33:00
Category: Misc
Tags: Android, fastboot, MIUI
Slug: the-system-has-been-destroyed
Figure: android.png

今天将自己的一个旧手机Redmi Note 8找出来，想刷一个最新版本的全球版ROM : [ginkgo_global_images_V12.5.2.0.RCOMIXM_20220216.0000.00_11.0_global_da0a599e0c.tgz](https://bn.d.miui.com/V12.5.2.0.RCOMIXM/ginkgo_global_images_V12.5.2.0.RCOMIXM_20220216.0000.00_11.0_global_da0a599e0c.tgz)。下载解压完成，直接运行flash_all.sh脚本完成刷机，但系统启动后显示： “The system has been destroyed” 。

解决方法：

```bash
fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img
```