import os as os
import zipfile as zip
from project import ProjectInfo
import shutil

def checkAndDeleteFile(path=str) -> bool:
    if os.path.exists(path) == True:
        os.remove(path)
    else:
        pass

    
def unzipFileAtPath(path_to_file=str) -> str:
    with zip.ZipFile(path_to_file, mode='r') as ref:
        folderpath = str(path_to_file).removesuffix(".zip")
        
        os.makedirs(folderpath, exist_ok=True)

        ref.extractall(path=folderpath)
    os.remove(path_to_file)

def convertDomainToFilePath(info=ProjectInfo) -> str:
    domainlist = str(info.domain).split(".")
    basestr = ""
    for i in domainlist:
        basestr = basestr + i + "\\"
    return basestr

def createNewDomain(info=ProjectInfo) -> str:
        oldmodloc = os.getcwd() + "\\" + info.name +"\\src\\main\\java\\com\\example\\examplemod\\ExampleMod.java"
        newmodloc = os.getcwd() + "\\" + info.name + "\\src\\main\\java\\" + convertDomainToFilePath(info)
        dirtodel = os.getcwd() + "\\" + info.name + "\\src\\main\\java\\com"
        
        os.makedirs(newmodloc)
        shutil.copyfile(oldmodloc, newmodloc + str(info.name).replace(" ", "") + ".java")
        shutil.rmtree(dirtodel)