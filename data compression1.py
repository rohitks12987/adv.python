import zipfile
with zipfile.ZipFile("Python.zip", "w") as f:
    f.write("file5.txt")

print("ZIP file created successfully")