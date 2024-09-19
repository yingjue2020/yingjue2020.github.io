Title: Linux Command : grep & sed
Date: 2020-03-25 22:41:10
Modified: 2020-03-25 22:41:10
Category: Misc
Tags: Linux
Slug: linux-command-grep-sed

如何利用grep和sed实现搜索和替换
```bash
grep -Erl "M\\('local" .|xargs sed -Ei "" "s/M\\('local/M\\('remote/g"

grep -Erl "http://loca" .|xargs sed -Ei "" "s/http:\/\/local/http:\/\/remote/g"
```

## grep
- -E 将样式为延伸的普通表示法来使用
- -r 此参数的效果和指定“-d recurse”参数相同
- -l 列出文件内容符合指定的样式的文件名称

字符小括号 '(' 在正则表达式里有特殊含义，需要转义字。
## sed
- -i 直接修改读取的文件内容，而不是输出到终端

Mac OSX 下多了一个参数，备份名，如果不备份，就传空字符串""
## xargs

给其他命令传递参数的一个过滤器，也是组合多个命令的一个工具。它擅长将标准输入数据转换成命令行参数，xargs 能够处理管道或者 stdin 并将其转换成特定命令的命令参数。xargs 也可以将单行或多行文本输入转换为其他格式，例如多行变单行，单行变多行。xargs 的默认命令是 echo，空格是默认定界符。这意味着通过管道传递给 xargs 的输入将会包含换行和空白，不过通过 xargs 的处理，换行和空白将被空格取代。xargs 是构建单行命令的重要组件之一。

## References
- https://www.cnblogs.com/wangqiguo/p/6464234.html
- https://wangchujiang.com/linux-command/c/xargs.html