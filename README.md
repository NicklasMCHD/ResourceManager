# ResourceManager
A resource manager for any python 3 game or application.

### What is this?
This is a simple Resource Manager you can use in your python 3 games / applications, to encrypt and compress your assets.

### Why would I want to encrypt / compress my assets.
So they don't get modified, don't get stolen and so on.

### How do I use this?
Good question:
* Clone this git repository.
* install the requirements from the "requirements.txt" file.
* (optionally) Change the iv and compression_level variables to make your encrypted data more secure (you'll find them at the top of the resourcemanager.py file).

Then after doing that, you can make an encrypted package by copying the resourcemanager.py file to the desired folder and running one of the following commands in a terminal:
* $ python resourcemanager.py key file
* $ python resourcemanager.py key

or run this command for help:
* $ python resourcemanager.py

When you have your resource file, you can get it's encrypted content into your application by doing this:

from resourcemanager import *

ress = ResourceManager()
ress.loadResources("resources.dat", "test123")
txt = ress.getResource("test.txt")
print(txt)

### So how does it work?
The resource manager encrypts all files and folders found recursively in the directory it were executed from, preserving the directory structure.

### What about the security?
The Resource Manager uses an age256 encryption protocol along with a 16 bit initialization vector and a 256 bit hash of the password you give it.

### Credits:
This handy little module were made by [@NicklasMCHD](https://twitter.com/NicklasMCHD "NicklasMCHD on twitter")

