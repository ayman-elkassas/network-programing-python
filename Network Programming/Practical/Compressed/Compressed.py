import zlib
import sys

text=open("file.txt","rb").read()
print("Raw size of file is {}".format(sys.getsizeof(text)))

compressed=zlib.compress(text,9)
print("size of compressed data is {}".format(sys.getsizeof(compressed)))

# save=open("compress.txt","ab")
open("compress.txt","wb").write(compressed)
# original=zlib.decompress(compressed)
# print(original)
# save.write(original)
