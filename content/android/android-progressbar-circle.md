Title: Android ProgressBar Circle
Date: 2019-05-13 14:37:26
Modified: 2019-05-13 14:37:26
Category: Android
Tags: Android, ProgressBar
Slug: android-progressbar-circle


# Shape
```xml
<?xml version="1.0" encoding="utf-8"?>
<shape
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape=["rectangle" | "oval" | "line" | "ring"] 
    android:innerRadius="integer"
    android:innerRadiusRatio="integer"
    android:thickness="integer"
    android:thicknessRatio="integer"
    android:useLevel="boolean"
    >
    <corners
        android:radius="integer"
        android:topLeftRadius="integer"
        android:topRightRadius="integer"
        android:bottomLeftRadius="integer"
        android:bottomRightRadius="integer" />
    <gradient
        android:angle="integer"
        android:centerX="float"
        android:centerY="float"
        android:centerColor="integer"
        android:endColor="color"
        android:gradientRadius="integer"
        android:startColor="color"
        android:type=["linear" | "radial" | "sweep"]
        android:useLevel=["true" | "false"] />
    <padding
        android:left="integer"
        android:top="integer"
        android:right="integer"
        android:bottom="integer" />
    <size
        android:width="integer"
        android:height="integer" />
    <solid
        android:color="color" />
    <stroke
        android:width="integer"
        android:color="color"
        android:dashWidth="integer"
        android:dashGap="integer" />
</shape>
```
android:innerRadius : 指定圆环内圆的半径

android:innerRadiusRatio :该值是以比例的形式来指定内圆半径。内圆半径等于该shape的宽除以该值。或者说该值的倒数代表了内圆半径占整个shape宽的比例。默认值是9。当该值等于2的时候，内圆就将占满整个shape，从而我们将看不到圆环。

android:thickness : 指定圆环的宽窄，也就是内圆与外圆的距离。

android:thicknessRatio : 以比例的形式来指定圆环的宽窄。其算法与innerRadiusRatio相同。

android:useLevel :值为true意味着这是一个levelListDrawable（关于levelListDrawable又是另一个话题了）。当我们要画一个圆环是，应当而且必须将该值设为false，否则会看不到画面。

# References
https://demonuts.com/circular-progress-bar/
https://medium.com/@evanca/android-tutorial-for-beginners-create-a-pie-chart-with-xml-36e67dabe67f
