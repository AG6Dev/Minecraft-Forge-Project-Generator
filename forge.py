import os as os
import requests as req
import json as json
from fileutil import *
from project import *

PROMOTED_VERSIONS_URL = "https://files.minecraftforge.net/maven/net/minecraftforge/forge/promotions_slim.json"

def downloadForgeZip(info=ProjectInfo) -> str:
    forge_version = getForgeVersion(info)
    base_url = "https://maven.minecraftforge.net/net/minecraftforge/forge/{mc_ver}-{forge_ver}/forge-{mc_ver}-{forge_ver}-mdk.zip/".format(
        mc_ver=info.game_ver, forge_ver=forge_version)

    checkAndDeleteFile(os.getcwd() + "\\temp.zip")

    data = req.get(base_url)

    with open(os.getcwd()+"\\temp.zip", mode='wb') as file:
        file.write(data.content)
        return os.path.realpath(file.name)

def getForgeVersion(info=ProjectInfo) -> str:
    vers = json.loads(req.get(PROMOTED_VERSIONS_URL).text)
    print(vers)
    return dict(dict(vers).get("promos")).get("{mc}-{pro}".format(mc=info.game_ver, pro=info.promo))


