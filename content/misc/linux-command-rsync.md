Title: Linux Command : rsync
Date: 2020-03-24 17:46:35
Modified: 2020-03-24 17:46:35
Category: Misc
Tags: Linux
Slug: linux-command-rsync
Figure: linux.png

Linux 下合并两个目录，软连接也一起同步。
```bash
rsync -K -a 源目录  被覆盖目录
```

比如：
```bash
rsync -K -a dir1/ dir2/
```

参考连接：https://linux.die.net/man/1/rsync

