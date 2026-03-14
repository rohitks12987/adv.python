import zlib
str =b"hello world"
print("Original string: ", str)
compressed = zlib.compress(str)
print("Compressed data: ", compressed)
decompressed = zlib.decompress(compressed)
print("Decompressed data: ", decompressed)