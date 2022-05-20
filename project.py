import os
from toml import *
import toml

class ProjectInfo:
    name = "Example Mod"
    modid = "examplemod"
    author = "You!"
    license = "All rights reserved"
    description = "Lorem Ipsum"
    domain = "com.example.examplemod"
    game_ver = ""
    promo = "recommended"

    def __init__(self, mc_ver=str, promo_type=str, **kwargs):
        self.name = kwargs.get("name")
        self.modid = kwargs.get("modid")
        self.author = kwargs.get("author")
        self.license = kwargs.get("license")
        self.description = kwargs.get("description")
        self.domain = kwargs.get("domain")
        self.game_ver = mc_ver
        self.promo = promo_type.lower()

def changeTomlInfo(info = ProjectInfo):
    tomlloc = os.getcwd() + "\\" + info.name + "\\src\\main\\resources\\META-INF\\mods.toml"
    
    data = toml.load(tomlloc)
    modinfo = dict(data['mods'][0])

    data['license'] = info.license
    data['mods'][0]["modId"] = info.modid
    data['mods'][0]["displayName"] = info.name
    data['mods'][0]["authors"] = info.author
    data['mods'][0]["description"] = info.description
    
    towrite = toml.dumps(data)

    with open(tomlloc, mode='w') as file:
        file.write(towrite)
