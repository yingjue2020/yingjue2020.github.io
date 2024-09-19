Title: docker 基础
Date: 2019-05-23 11:14:28
Modified: 2019-05-23 11:14:28
Category: Misc
Tags: Docker
Slug: docker-basics

# 自定义镜像

如何自定义一个镜像，并上传到Docker Hub 。

假设需要为php-fpm-alpine增加mysqli扩展并增加 usermod 命令。

编写Dockerfile
```Dockerfile
FROM php:7.4.3-fpm-alpine

LABEL maintainer="liujun<liujun@forkliu.com>"

RUN docker-php-ext-install mysqli
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories
RUN apk --no-cache add shadow && usermod -u 1000 www-data
```
构建镜像
```bash
docker build -t php-fpm-alpine-usermod:7.4.3 -f php_usermod.dockerfile .
```
上传镜像
```bash
docker tag php-fpm-alpine-usermod:7.4.3 sundayliu/php-fpm-alpine-usermod:7.4.3
docker push sundayliu/php-fpm-alpine-usermod:7.4.3
```


# 常用参数
```shell
docker run \
    --rm \
    -it \
    -e USER_ID=1001 \
    -e GROUP_ID=1002 \
    -v /data00/home/liujun.sun/aosp-6.0.1_r80/build-test.sh:/usr/local/bin/run.sh:ro \
    -v /home/liujun.sun/aosp-6.0.1_r80/aosp:/aosp \
    -v /home/liujun.sun/aosp-6.0.1_r80/ccache:/tmp/ccache \
    kylemanna/aosp:6.0-marshmallow \
    bash run.sh docker
```

```shell
[-v|--volume[=[[HOST-DIR:]CONTAINER-DIR[:OPTIONS]]]]
          Create a bind mount. If you specify, -v /HOST-DIR:/CONTAINER-DIR, Docker
          bind mounts /HOST-DIR in the host to /CONTAINER-DIR in the Docker
          container.
-v /data00/home/liujun.sun/aosp-6.0.1_r80/build-test.sh:/usr/local/bin/run.sh:ro
        ro:read-only mode
```

```shell
-e Set environment variables
-i, --interactive=true|false
          Keep STDIN open even if not attached. The default is false.
          保证容器中STDIN是开启的
-t, --tty=true|false
          Allocate a pseudo-TTY. The default is false.
          告诉Docker为要创建的容器分配一个伪tty终端。这样，新创建的容器才能提供一个交互式shell。
--rm true|false
    Automatically remove the container when it exits. The default is false.
```

# 常用命令
## 删除容器
```shell
docker rm `docker ps -a -q`
```
## 镜像操作
### 列出本地镜像
```bash
docker image ls
```

## 容器操作
### 网络配置

创建网络
```bash
docker network create test_backend
```
将容器连接到网络
```bash
docker network connect test_backend mysql_db_1
```

将容器与网络断开
```bash
docker network disconnect test_backend phpmyadmin
```

# XAMPP 安装
```bash
docker pull cswl/xampp
```
数据库密码默认为空"" 。