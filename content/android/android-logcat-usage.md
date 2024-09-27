Title: Android Logcat Usage
Date: 2020-04-04 12:07:38
Modified: 2020-04-04 12:07:38
Category: Android
Tags: Android, Logcat
Slug: android-logcat-usage
Figure: android.png

## zsh:no matches found

因为zsh缺省情况下始终自己解释这个firefox*，而不会传递给adb logcat来解释。
在~/.zshrc中加入:
setopt no_nomatch, 然后进行source .zshrc命令
