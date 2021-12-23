import os
import shutil
path = "C:/Users/naani/Desktop"
print("beforeCopyingFile")
print(os.listdir(path))
source="C:/Users/naani/Desktop/Normal.txt"
destination="C:/Users/naani/Desktop/file2.txt"
dest=shutil.copy(source,destination)
print("afterCopyingFile")
print(os.listdir(path))