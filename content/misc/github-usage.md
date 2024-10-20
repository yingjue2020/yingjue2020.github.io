Title: Github Usage
Date: 2019-05-13 00:07:46
Modified: 2019-05-13 00:07:46
Category: Misc
Tags: Git, Github
Slug: github-usage
Figure: git.png

# 创建ssh-key 并且重命名
```shell
cd ~/.ssh
ssh-keygen -t rsa -C "example@example.com"
ssh-keygen -t ed25519 -C "your_email@example.com"
```

on Windows:
```bash
eval `ssh-agent -s`
```

# 将ssh-key添加到ssh agent

```shell
ssh-add example
```

# 配置，将不同账号与ssh-key关联

```shell
vim config
Host example
    Hostname github.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/example
```

# 在git服务器上添加公钥
```shell
cat example.pub
```

# 测试
```shell
ssh -T example
```

# Common Usage
## zip branch
```bash
git archive -o v0.0.1.zip main
```

## Create empty branch
```bash
git switch --orphan <new branch>
git commit --allow-empty -m "Initial commit on orphan branch"
git push -u origin <new branch>
```

## Submodule
```bash
git submodule add <remote url> <local url>
git submodule add https://github.com/tatamobile/pelican-boostrap5.git themes/pelican-bootstrap5

git submodule update --init
git submodule update --init --recursive
```

__用zip加密压缩文件和目录__

```bash
zip -e -r keys.zip keys
```
