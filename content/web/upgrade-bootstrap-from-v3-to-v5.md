Title: Upgrade Bootstrap from V3 to V5
Date: 2024-10-08 14:00
Modified: 2024-10-08 14:00
Category: Web
Tags: Bootstrap5
Slug: upgrade-bootstrap-from-v3-to-v5
Figure: bootstrap.jpeg
Authors: Apple

Bootstrap 5 相比 Bootstrap 3，进行了全面的改进，尤其是去除了对 jQuery 的依赖、全面引入 Flexbox、提供了更丰富的响应式功能和现代化组件。升级到 Bootstrap 5 可以让你的项目更加轻量、现代，并且更具响应性，同时在设计方面也更加灵活。

1. 网格系统（Grid System）
- Bootstrap 3：
  - 网格系统基于 12 列布局，支持 xs、sm、md 和 lg 这四个屏幕尺寸断点。
  - 使用 col-xs-*, col-sm-*, col-md-*, col-lg-* 类名来定义不同屏幕尺寸下的列数。
  - 通过 col-*-offset-* 来进行列的偏移。
- Bootstrap 5：
  - 保持了 12 列布局，但新增了两个屏幕断点：xxl 和 xl，提供更精细的布局控制。
  - 断点类名为 col-*，例如：col-xxl-*, col-xl-*, col-lg-*, col-md-*, col-sm-*, col-xs-*。
  - 支持 gutter spacing (间距) 调整，采用 g-* 类名来控制列间距，代替 Bootstrap 3 中通过 padding 实现的列间距。
  - 使用 row-cols-* 类快速创建等宽列，减少了手动列配置的需求。

2. Flexbox 支持
- Bootstrap 3：不使用 Flexbox，而是使用浮动（float）和盒模型（box model）来布局。
- Bootstrap 5：全面使用 Flexbox，提供了更多灵活和现代的布局方式，通过 d-flex 和相关的 Flexbox 类，可以轻松实现各种布局（如水平和垂直对齐）。

3. jQuery 的移除

- Bootstrap 3：依赖 jQuery，所有动态组件（如模态框、下拉菜单等）都需要 jQuery 支持。
- Bootstrap 5：完全移除了 jQuery，改用原生 JavaScript 实现所有动态组件。这样减少了对外部库的依赖，提高了页面性能。

4. 表单（Forms）

- Bootstrap 3：表单控件的类较少且不支持自定义样式，表单的样式和布局需要更多手动配置。
- Bootstrap 5：表单系统进行了大幅改进，增加了许多 自定义表单控件 类，比如自定义的复选框（checkbox）、单选按钮（radio）和开关（switch）。还支持更灵活的网格系统、行列自动布局，以及改进的表单反馈机制。

5. 弃用和新增的组件

- Bootstrap 3：
  - 包含一些现在已被废弃的组件，如 Glyphicons 图标、input group addon 等。
- Bootstrap 5：
  - Glyphicons 被移除，推荐使用 Bootstrap Icons（官方提供的独立图标库）或其他图标库。
  - 引入了更多现代化组件，如 Toast 消息弹框、Offcanvas 侧边栏等。
  - Panel、Well 组件被移除，替代方式为使用 Card 组件。

6. 自定义 CSS 变量

- Bootstrap 3：没有使用 CSS 变量，主要依赖于 Sass/Less 预处理器。
- Bootstrap 5：引入了 CSS 变量（Custom Properties），使得开发者可以更加方便地定制样式而无需依赖预处理器。同时保留了对 Sass 的支持，但可以通过 CSS 变量更灵活地进行实时样式调整。

7. 响应式字体和间距

- Bootstrap 3：没有响应式字体大小的功能，间距（Margin、Padding）主要通过手动调整。
- Bootstrap 5：增加了响应式的字体类 fs-*，以及响应式的间距类 m-*, p-*，如 mb-md-4，可以根据不同的屏幕尺寸动态调整字体和间距。

8. 浮动（Floats）和定位

- Bootstrap 3：广泛使用 float 来实现布局和元素对齐，使用 clearfix 类清除浮动。
- Bootstrap 5：通过 Flexbox 实现布局，因此不再依赖浮动，仍然保留了 float-* 类，但建议使用 Flexbox 类如 d-flex 来代替。

9. 按钮（Buttons）

- Bootstrap 3：按钮样式相对简单，没有更多可扩展性。
- Bootstrap 5：按钮系统改进，引入了更多的按钮样式和颜色。还支持新的按钮组样式，增强了自定义性。

10. JavaScript 插件

- Bootstrap 3：依赖于 jQuery 的插件系统。
- Bootstrap 5：使用原生 JavaScript 重写了所有插件，提升了性能，减少了对外部依赖库的需求。

11. 断点改进

- Bootstrap 3：断点较少，依赖较大屏幕设备的布局。
- Bootstrap 5：引入了更细的断点，如 xxl 断点（大于 1400px 的屏幕），以便更精确地处理不同设备上的响应式布局。

12. 弃用的类

- Bootstrap 3：使用很多类名已在 Bootstrap 5 中弃用，例如 hidden-*, visible-*, pull-right, pull-left。
- Bootstrap 5：用新的类名替代了旧类，如 float-start, float-end, 并且移除了 hidden-* 系列类，建议使用 CSS 的 d-none 和响应式显示类 d-sm-block。

13. 卡片组件（Card Component）

- Bootstrap 3：使用的是 Panels、Thumbnails 和 Wells 等组件来创建容器。
- Bootstrap 5：引入了 Card 组件，统一了容器的设计风格，并提供了更多的定制化功能。


水平居中div

```html
<div class="d-flex justify-content-center">
</div>
```


## References
- [bootstrap3-upgrade-bootstrap5](https://www.liuzhining.com/post/bootstrap3-upgrade-bootstrap5)