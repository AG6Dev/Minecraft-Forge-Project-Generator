import os
import re
import shutil

import toml


class ProjectInfo:
    name = ""
    modid = ""
    author = ""
    license = ""
    description = ""
    domain = ""
    game_ver = ""
    promo = "recommended"

    def __init__(self, mc_ver=str, promo_type=str, **kwargs):
        self.name = "Example Mod" if kwargs.get("name") == "" else kwargs.get("name")
        self.modid = "examplemod" if kwargs.get("modid") == "" else kwargs.get("modid")
        self.author = "You!" if kwargs.get("author") == "" else kwargs.get("author")
        self.license = "All rights reserved" if kwargs.get("license") == "" else kwargs.get("license")
        self.description = "Lorem Ipsum" if kwargs.get("description") == "" else kwargs.get("description")
        self.domain = "com.example.examplemod" if kwargs.get("domain") == "" else kwargs.get("domain")
        self.game_ver = mc_ver
        self.promo = promo_type.lower()


def convertDomainToFilePath(info=ProjectInfo) -> str:
    domainlist = info.domain.split(".")
    basestr = ""
    for i in domainlist:
        basestr = basestr + i + "\\"
    return basestr


def createNewDomain(info=ProjectInfo):
    oldmodloc = os.getcwd() + "\\" + info.name + "\\src\\main\\java\\com\\example\\examplemod\\ExampleMod.java"
    newmodloc = os.getcwd() + "\\" + info.name + "\\src\\main\\java\\" + convertDomainToFilePath(info)
    dirtodel = os.getcwd() + "\\" + info.name + "\\src\\main\\java\\com"
    try:
        os.makedirs(newmodloc)
    except FileExistsError:
        pass

    shutil.copyfile(oldmodloc, newmodloc + str(info.name).replace(" ", "") + ".java")
    shutil.rmtree(dirtodel)



def changeTomlInfo(info=ProjectInfo):
    tomlloc = os.getcwd() + "\\" + info.name + "\\src\\main\\resources\\META-INF\\mods.toml"

    data = toml.load(tomlloc)

    data['license'] = info.license
    data['mods'][0]["modId"] = info.modid
    data['mods'][0]["displayName"] = info.name
    data['mods'][0]["authors"] = info.author
    data['mods'][0]["description"] = info.description

    towrite = toml.dumps(data)

    with open(tomlloc, mode='w') as file:
        file.write(towrite)


def editMainModFile(info=ProjectInfo):
    loc = os.getcwd() + "\\" + info.name + "\\src\\main\\java\\" + convertDomainToFilePath(info) + str(
        info.name).replace(" ", "") + ".java"

    with open(loc, mode='r') as file:
        lines = file.readlines()

        with open(loc, mode='w') as file_2:
            lines[0] = "package {domain};\n".format(domain=info.domain)
            lines[20] = "@Mod(\"{modid}\")\n".format(modid=info.modid)
            lines[21] = "public class {filename}\n".format(filename=str(info.name).replace(" ", ""))
            lines[26] = '\tpublic {filename}() \n'.format(filename=str(info.name).replace(" ", ""))

            file_2.writelines(lines)


def checkValidModId(info=ProjectInfo) -> bool:
    if len(info.modid) < 32:
        if re.match("[a-z0-9/._-]", info.modid):
            return True
    return False
