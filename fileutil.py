import os as os
import zipfile as zip

def checkAndDeleteFile(path=str) -> bool:
    if os.path.exists(path) == True:
        os.remove(path)

    
def unzipFileAtPath(path_to_file=str) -> str:
    with zip.ZipFile(path_to_file, mode='r') as ref:
        folderpath = str(path_to_file).removesuffix(".zip")
        
        os.makedirs(folderpath, exist_ok=True)

        ref.extractall(path=folderpath)
    os.remove(path_to_file)