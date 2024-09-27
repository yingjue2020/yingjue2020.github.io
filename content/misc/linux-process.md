Title: Linux Process
Date: 2019-06-27 17:34:15
Modified: 2019-06-27 17:34:15
Category: Misc
Tags: Linux
Slug: linux-process
Figure: linux.png

# 概念
程序是一系列指令的集合，通常存为可执行文件。进程是程序的执行过程。

# 进程属性
使用ps可以查看系统正在运行的进程。 ps --help显示该命令的用法。
```shell
ps -e -o USER,PID,PPID,GID,NAME
USER           PID  PPID      GID NAME                        CMD            
root             1     0        0 init                        init
root             2     0        0 [kthreadd]                  kthreadd
root             3     2        0 [ksoftirqd/0]               ksoftirqd/0
root             5     2        0 [kworker/0:0H]              kworker/0:0H
root             6     2        0 [kworker/u16:0]             kworker/u16:0
root             7     2        0 [rcu_preempt]               rcu_preempt
root             8     2        0 [rcu_sched]                 rcu_sched
root             9     2        0 [rcu_bh]                    rcu_bh
```
USER: 进程所属用户的ID
PID:进程ID
PPID:父进程的ID
GID:进程组ID
NAME:进程名

# 孤儿进程
使用fork创建的子进程，父进程应该调用wait函数，等待子进程的退出信息，如果父进程先结束，子进程将变成孤儿进程，过继给init进程，
init进程成为它的父进程。

# 进程组
进程组包含多个进程，进程组会有一个领导进程(process group leader)，该领导进程的PID将作为进程组的PGID。



