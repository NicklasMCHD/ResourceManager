# Changes this for more security
# Note: If you change this, please note that it must be 16 characters long.
iv = "thisisrandomsalt"

# Compression preset (default 6, between 1-9).
compression_level = 6

# These are the file types you want to exclude from the pack.
excluded_file_types = (".py", ".pyc", ".log", ".dll", ".dat")


import pickle, sys, os, hashlib, lzma
from Cryptodome.Cipher import AES

# Internal functions.
def encrypt_data(key, data):
	try:
		key = key.encode("utf-8")
	except AttributeError:
		pass
	try:
		data = data.encode("utf-8")
	except AttributeError:
		pass
	encryptor = AES.new(hashlib.sha256(key).digest(), AES.MODE_CFB, iv.encode("utf-8"))
	return encryptor.encrypt(data)


def decrypt_data(key, data):
	try:
			key = key.encode("utf-8")
	except AttributeError:
		pass
	decryptor = AES.new(hashlib.sha256(key).digest(), AES.MODE_CFB, iv.encode("utf-8"))
	decryptedData = decryptor.decrypt(data)
	return decryptedData

def compress_data(data):
	return lzma.compress(data, preset=compression_level)

def decompress_data(data):
	return lzma.decompress(data)

class ResourceManager():
	def __init__(self):
		self.data = {}

	def loadResources(self, file, password):
		f = open(file, "rb")
		eD = f.read()
		f.close()
		qData = decrypt_data(password, eD)
		sData = pickle.loads(qData)
		for key in sData:
			self.data[key] = decompress_data(sData[key])

	def getResource(self, file):
		return self.data[file]

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: " + sys.argv[0] + " key")
		print("Usage: " + sys.argv[0] + " key file")
		print("")
		print("key - required - encryption key to use.")
		print("file - optional - The filename to write the encrypted data to (default \"resources.dat\")")
		sys.exit()
	
	pwd = sys.argv[1]
	resourceFile = "resources.dat"
	if len(sys.argv) == 3:
		resourceFile = sys.argv[2]
	
	print("Starting")
	print("Key: " + pwd)
	print("Resource File: " + resourceFile)
	print("")
	
	storedFiles = {}
	key = pwd
	
	print("Reading files from system. Please wait!")
	for path, subdirs, files in os.walk(os.getcwd()):
		for name in files:
			p = os.path.join(path, name)
			niceName = p[1+len(os.getcwd()):].replace("\\", "/")
			if niceName.lower().endswith(excluded_file_types):
				print("Skipping " + niceName + ".")
				continue
			print("Compressing " + niceName + ".")
			f = open(p, "rb")
			data = f.read()
			f.close()
			storedFiles[niceName] = compress_data(data)
			del data
	
	print("Converting data.")
	tmpData = pickle.dumps(storedFiles)
	print("Encrypting data...")
	encryptedData = encrypt_data(key, tmpData)
	print("Writing data to disk...")
	f = open(resourceFile, "wb")
	f.write(	encryptedData)
	f.close()
	print("Done")
	print("Running checks on generated resources file.")
	f = open(resourceFile, "rb")
	eD = f.read()
	f.close()
	qData = decrypt_data(key, eD)
	sData = pickle.loads(qData)
	print("Running decryption/decompression test.")
	testData = {}
	for key in sData:
		testData[key] = decompress_data(sData[key])
	print("decryption/decompression test passed.")
	print("Running byte matcher test.")
	if len(testData) == len(storedFiles):
		print("Passed byte matcher.")
	else:
		print("Warning: Bytematching failed. This can happen if you have non-audio files in your resources file.")
	print("Done")
