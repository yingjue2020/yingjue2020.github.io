Title: hacking android app with frida
Date: 2019-04-24 17:35:05
Modified: 2019-04-24 17:35:05
Category: Reverse Engineering
Tags: Frida, Android
Slug: hacking-android-app-with-frida
Figure: frida.png

# 环境安装
- frida-server
- frida-tools
```shell
pip3 install frida
pip3 install frida-tools
```

# 基础用法
```shell
frida-ps -U
frida-trace -U -i "recvfrom" com.android.chrome
```

## Javascript example 1
```javascript
Java.enumerateLoadedClasses(
  {
  "onMatch": function(className){ 
        console.log(className) 
    },
  "onComplete":function(){}
  }
)
```

## Javascript example 2:chrome.js
```javascript
Java.perform(function () {
    var Activity = Java.use("android.app.Activity");
    Activity.onResume.implementation = function () {
        console.log("[*] onResume() got called!");
        this.onResume();
    };
});
```

```shell
frida -U -l chrome.js com.android.chrome
```

# References
https://www.frida.re/docs/home/
