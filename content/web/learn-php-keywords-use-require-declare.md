Title: Learn PHP: keywords such as declare,use,require
Date: 2024-12-25 14:00
Modified: 2024-12-25 14:00
Category: Web
Tags: php
Slug: learn-php-keywords-use-require-declare
Figure: php.png
Authors: Apple

**declare** 是一个用于设置脚本执行指令的结构，主要用于控制 PHP 的运行时行为。

**语法：**
```php
declare (directive = value) {
    // Code block
}
```

**常用指令：**

- ticks：定义在脚本中每执行一定次数的低级语句时触发一次信号处理。

```php
declare(ticks=1);
function tick_handler() {
    echo "Tick\n";
}
register_tick_function('tick_handler');
for ($i = 0; $i < 3; $i++) {
    echo $i . "\n";
}
```

- strict_types：启用严格类型检查（从 PHP 7 开始）。

```php
declare(strict_types=1);
function add(int $a, int $b): int {
    return $a + $b;
}
echo add(2, 3); // 正常
echo add(2.5, 3); // TypeError
```

**特点：**

- declare 的作用域通常是当前文件或代码块。
- 一般用于设置编译时和运行时的行为。

**use**是一个用于引入命名空间或类别名的关键字。

**引入命名空间：**

```php
namespace MyApp;
use AnotherNamespace\MyClass;

$obj = new MyClass(); // 等同于 AnotherNamespace\MyClass
```

**类别名：**

```php
use AnotherNamespace\MyClass as AliasClass;

$obj = new AliasClass(); // 等同于 AnotherNamespace\MyClass
```

**用于引入特性（traits）：**

```php
class MyClass {
    use SomeTrait;
}
```

**特点**

- use 主要用于提高代码的可读性和简化命名。
- 它只在文件级别生效，不能动态导入命名空间或类。

**require** 是用于引入和执行 PHP 文件的关键字。被引入的文件会作为当前文件的一部分执行。

**引入文件：**

```php
require 'config.php';
```

**条件引入：**

```php
if ($condition) {
    require 'optional.php';
}
```

**require vs include**

- require 如果文件不存在或加载失败，会抛出 **致命错误（fatal error）**，脚本停止执行。
- include 如果文件不存在或加载失败，会抛出 **警告（warning）**，脚本继续执行。

**特点:**

- require 是运行时导入文件，文件内容在导入时被解析和执行。
- 通常用于加载必需的配置文件或核心逻辑文件。

**区别总结**

| 关键字 | 主要用途 | 作用范围 | 运行时行为 |
| ----- | ------  | ------ | ------- |
| declare |设置脚本运行时行为，如严格类型、信号处理|当前文件或代码块	|控制执行指令，例如严格类型检查|
|use	  |引入命名空间、类或特性               |文件级别         |编译时处理，用于简化类名、特性名的使用|
|require|引入和执行文件                      |当前文件	       |运行时加载，文件不存在时报错并停止脚本执行|

**最佳实践**

- 使用 declare(strict_types=1) 进行严格类型检查，提高代码的健壮性。
- 使用 use 管理命名空间，避免全局命名冲突。
- 使用 require 或 require_once 加载必需文件，建议对非必须文件使用 include 或 include_once。