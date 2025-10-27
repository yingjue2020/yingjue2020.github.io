Title: How to jailbreak iOS 16 using palera1n
Date: 2024-09-25 10:56:00
Modified: 2025-10-27 10:56:00
Category: Reverse Engineering
Tags: jailbreak, palera1n
Slug: jailbreak-palera1n
Summary: Building iOS environment for reverse engineering. How to jailbreak iOS 15~18 using palera1n. Install Sileo and frida .
Figure: palera1n.png

Q: **Build may be slow as Theos isn’t using all available CPU cores on this computer.**

参考链接：[Parallel Building](https://theos.dev/docs/parallel-building)

步骤：

```bash
brew install make
echo PATH=\"$(brew --prefix make)/libexec/gnubin:\$PATH\" >> ~/.zprofile
```

Q: **palera1n loader app can't disappear after jailbreak on iPhone X(16.7.10)**

Reference Link: [palera1n #541](https://github.com/palera1n/palera1n/issues/541)

- Restore iPhone by Finder
- Don't use passcode
- Turn off "Find My Device"

## How to jailbreak iPhone
### Download palera1n

Download [palera1n](https://palera.in/download/?tab=macos) on Mac:
```bash
sudo /bin/sh -c "$(curl -fsSL https://static.palera.in/scripts/install.sh)"
```

### Rootless jailbreak
```bash
palera1n -l
#
# palera1n: v2.0.2 
#
# ========  Made by  =======
# Made by: Nick Chan, Ploosh, Khcrysalis, Mineek, staturnz, kok3shidoll, HAHALOSAH 
# ======== Thanks to =======
# Thanks to: llsc12, Nebula, Lrdsnow, nikias (libimobiledevice),
# checkra1n team (Siguza, axi0mx, littlelailo et al.),
# Procursus Team (Hayden Seay, Cameron Katri, Keto et.al)
# ==========================

 - [10/27/25 10:21:10] <Info>: Waiting for devices
 - [10/27/25 10:21:10] <Info>: Entering recovery mode
 - [10/27/25 10:21:21] <Info>: Press Enter when ready for DFU mode

Hold volume down + side button (0)
Hold volume down button (4)
 - [10/27/25 10:21:49] <Info>: Device entered DFU mode successfully
 - [10/27/25 10:21:49] <Info>: About to execute checkra1n
#
# Checkra1n 0.1337.3
#
# Proudly written in nano
# (c) 2019-2023 Kim Jong Cracks
#
#========  Made by  =======
# argp, axi0mx, danyl931, jaywalker, kirb, littlelailo, nitoTV
# never_released, nullpixel, pimskeks, qwertyoruiop, sbingner, siguza
#======== Thanks to =======
# haifisch, jndok, jonseals, xerub, lilstevie, psychotea, sferrini
# Cellebrite (ih8sn0w, cjori, ronyrus et al.)
#==========================

 - [10/27/25 10:21:50] <Verbose>: Starting thread for Apple TV 4K Advanced board
 - [10/27/25 10:21:50] <Info>: Waiting for DFU mode devices
 - [10/27/25 10:21:50] <Verbose>: DFU mode device found
 - [10/27/25 10:21:50] <Info>: Checking if device is ready
 - [10/27/25 10:21:50] <Verbose>: Attempting to perform checkm8 on 8010 11
 - [10/27/25 10:21:50] <Info>: Setting up the exploit
 - [10/27/25 10:21:50] <Verbose>: == checkm8 setup stage ==
 - [10/27/25 10:21:50] <Verbose>: Entered initial checkm8 state after 1 steps
 - [10/27/25 10:21:50] <Verbose>: Stalled input endpoint after 1 steps
 - [10/27/25 10:21:50] <Verbose>: DFU mode device found
 - [10/27/25 10:21:50] <Verbose>: == checkm8 trigger stage ==
 - [10/27/25 10:21:53] <Info>: Checkmate!
 - [10/27/25 10:21:53] <Verbose>: Device should now reconnect in download mode
 - [10/27/25 10:21:53] <Verbose>: DFU mode device disconnected
 - [10/27/25 10:22:00] <Info>: Entered download mode
 - [10/27/25 10:22:00] <Verbose>: Download mode device found
 - [10/27/25 10:22:00] <Info>: Booting PongoOS...
 - [10/27/25 10:22:02] <Info>: Found PongoOS USB Device
 - [10/27/25 10:22:04] <Info>: Booting Kernel...

```

### Install Sileo
Open palera1n app and then install Sileo .

- install ssh: Open Sileo app and search ssh,install ssh-server and ssh-client .
- install frida: https://build.frida.re

### Enable ssh root

Install iproxy: brew install libusbmuxd

On mac run command:
```bash
iproxy 2222 22
```

Connect to iPhone using ssh
```bash
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 2222 mobile@127.0.0.1
This is the Z Shell configuration function for new users,
zsh-newuser-install.
You are seeing this message because you have no zsh startup files
(the files .zshenv, .zprofile, .zshrc, .zlogin in the directory
~).  This function can help you with a few settings that should
make your use of the shell easier.

You can:

(q)  Quit and do nothing.  The function will be run again next time.

(0)  Exit, creating the file ~/.zshrc containing just a comment.
     That will prevent this function being run again.

(1)  Continue to the main menu.

--- Type one of the keys in parentheses --- 

Aborting.
The function will be run again next time.  To prevent this, execute:
  touch ~/.zshrc
```

Enbale root user:
```bash
Parrot:~ mobile% sudo passwd root

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for mobile: 
Changing password for root.
Old Password:
New Password:
Retype New Password:

################################### WARNING ###################################
# This tool does not update the login keychain password.                      #
# To update it, run `security set-keychain-password` as the user in question, #
# or as root providing a path to such user's login keychain.                  #
###############################################################################

```

### Install Frida
```bash
scp -P 2222 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no bin/frida_16.6.6_iphoneos-arm64.deb root@127.0.0.1:/tmp/frida.deb
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 2222 root@127.0.0.1 "dpkg -i /tmp/frida.deb"

Warning: Permanently added '[127.0.0.1]:2222' (ED25519) to the list of known hosts.
(root@127.0.0.1) Password for root@Parrot:
Selecting previously unselected package re.frida.server.
(Reading database ... 6596 files and directories currently installed.)
Preparing to unpack /tmp/frida.deb ...
Unpacking re.frida.server (16.6.6) ...
Setting up re.frida.server (16.6.6) ...
```

## How to install ipa

Install ideviceinstaller:

```bash
brew install libimobiledevice
brew install ideviceinstaller
```

Install ipa:

```bash
ideviceinstaller -i <path_to_your_app>.ipa
ideviceinstaller -l
ideviceinstaller -u <bundle_id>
ideviceinstaller -r -i <path_to_your_app>.ipa
```

## Common sources

- Frida: https://build.frida.re