# This is an example for how to use the resource manager.
# For this example to work, the iv and compression_level must not have been changed.

# first import it.
from resourcemanager import *

# Make an instance of the resource manager.
ress = ResourceManager()
# Load the resources packaget in "resources.dat" with the encryption key "test123"
ress.loadResources("resources.dat", "test123")

# Get the resource "test.txt" from the loaded resources.
txt = ress.getResource("test.txt")

# print the result.
print(txt)
