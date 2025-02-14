Title: Learn Slim Skeleton
Date: 2024-12-24 14:00
Modified: 2024-12-24 14:00
Category: Web
Tags: php, slim
Slug: learn-slim-skeleton
Figure: slim.png
Authors: Apple

__Install php develop environment__

```bash
brew install php
brew install composer
```

Create project using slim skeleton
```bash
composer create-project slim/slim-skeleton [my-app-name]
composer create-project slim/slim-skeleton slim-card
```

__declare vs use vs require__

**declare** 是一个用于设置脚本执行指令的结构，主要用于控制 PHP 的运行时行为。

**语法：**
```php
declare (directive = value) {
    // Code block
}
```
