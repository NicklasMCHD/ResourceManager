# This is an example for how to use the resource manager.

from resourcemanager import *

ress = ResourceManager()
ress.loadResources("resources.dat", "test123")
txt = ress.getResource("test.txt")
print(txt)
