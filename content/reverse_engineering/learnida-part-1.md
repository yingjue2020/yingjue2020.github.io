Title: Using IDAPython to Make Your Life Easier: Part 1 - Setup Environment
Date: 2024-02-25 10:50
Modified: 2024-09-27 10:50
Category: Reverse Engineering
Tags: IDA Pro
Slug: learn-ida-part-1-setup-environment

# Background

As a reverse engineer, I often use IDA Pro in my daily work. This is not surprising,
as IDA Pro is the industry standard (although alternatives such as radare2 and
Hopper are becoming increasingly popular). One of the most powerful features of IDA 
that I recommended all reverse engineers is the Python extension, aptly named 'IDAPython', 
which exposes a large number of IDA API calls. Of course, users also have the added
benefit of working with Python, giving them access to the many possibilities that the
scripting language offers.

While reverse-engineering a malicious example, I came across the following function:

![string decryption function]({static}/images/learnida/string_decryption_function.png "Figure 1 String decryption function")

Based on my experience, I suspected that this could be used to decrypt the data contained in the binary file. The number of references to this function confirmed my suspicion.

![High number of references to suspect function]({static}/images/learnida/high_number_reference_function.png "Figure 2 High number of references to suspect function")

As we can see in Figure 2, there are 2017 instances in which this particular function is called. In each instance in which this function is called, a data block is passed to this function as four arguments via registers X0, X1, W2and W3.

![Instances where the suspect function (10758A448) is called]({static}/images/learnida/call_string_decrypt_function.png "Figure 3 Instances where the suspect function (10758A448) is called")

At this point, I am confident that this feature is used by the malware to decrypt strings at runtime. When faced with this type of situation, I usually have a few options:

1. I can manually decrypt and rename these encrypted strings
2. I can run this example dynamically and rename the strings as I find them
3. I can write a script that decrypts and renames these strings for me

If it were a situation where the malware was only decrypting a few strings, I might take the first or second approach. However, as we have already established, this function is used 2017 times, so the scripting approach makes much more sense.


# Setup Environment

To complete the development of this script, you need to install the third-party Python library unicorn (unicorn is a lightweight library for running simulations that is very easy to use). There are two methods for installing third-party libraries:

1. Install directly into the system directory using pip
2. Create your own venv and install the third-party library in the venv

To avoid contamination of the system libraries or various conflicts, use the second method to install third-party libraries here. Take the MacOS system as an example.

First create a venv with the following command:

```bash
mkdir learnida
cd learnida
python3 -m venv .venv
source .venv/bin/activate
pip install unicorn
```

Then let IDAPro find these dependent libraries. To do this, set the environment variable "IDAUSR".
Add a line of text to the ~/.zprofile file 

```bash
export IDAUSR=$HOME/.idapro:$HOME/projects/learnida
```

and create a soft link
```bash
cd learnida
mkdir python
ln -s $HOME/projects/learnida/.venv/lib/python3.9/site-packages python/3
```


Finally, check whether Unicorn can be used. Start IDAPro via the terminal and try to output the version number of Unicorn

![check unicorn version]({static}/images/learnida/check_unicorn_version.png "Figure 4 check unicorn version")

You can see that the version number of Unicorn is 2.0.1, which proves that the installation was successful. Now it is time to develop the script to decrypt the string.

Special note: IDA Pro must be started via the terminal for the environment variable "IDAUSR" to take effect.


# Conclusion

With IDAPython, we were able to easily accomplish an otherwise difficult task of decrypting 2017 encrypted strings in a binary file. As we have seen, IDAPython can be a powerful tool for a reverse engineer, simplifying various tasks and saving valuable time. You can download the sample used in this article [here](https://drive.google.com/file/d/1T0ta_rfHPjSsvZw-B-LBiAgC7zgfCQuY) .

# References
- [Using IDAPython to Make Your Life Easier: Part 1](https://unit42.paloaltonetworks.com/using-idapython-to-make-your-life-easier-part-1/)
