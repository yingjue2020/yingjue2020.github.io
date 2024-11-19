Title: 禁止Spotlight对外部磁盘建立索引
Date: 2024-11-19 10:33:00
Modified: 2024-11-19 10:33:00
Category: Misc
Tags: MacOS, Spotlight
Slug: macos-splotlight-disable-index

#### 使用 System Preferences

1. 打开 系统设置（System Preferences）或 系统偏好设置。
2. 选择 Spotlight。
3. 切换到 Privacy（隐私）标签。
4. 点击 ”+” 按钮，将外部磁盘添加到列表中。
5. 确认后，Spotlight 将不会索引该磁盘。

#### 使用 mdutil 禁用索引

可以通过命令行工具 mdutil 禁用指定磁盘的索引。

禁用索引的命令：
```bash
sudo mdutil -i off /Volumes/YourExternalDiskName
```

将 YourExternalDiskName 替换为外部磁盘的名称。

清除现有索引：

如果磁盘上已经存在索引，可以清除它：
```bash
sudo mdutil -E /Volumes/YourExternalDiskName
```

#### 在磁盘根目录下添加 .metadata_never_index 文件

创建一个特殊文件来阻止 Spotlight 对磁盘进行索引。

步骤：

1. 打开终端。

2. 切换到外部磁盘的根目录：
```bash
cd /Volumes/YourExternalDiskName
```

3. 创建 .metadata_never_index 文件：
```bash
sudo touch .metadata_never_index
```

4. 如果索引已经存在，清除索引数据：
```bash
sudo mdutil -E /Volumes/YourExternalDiskName
```