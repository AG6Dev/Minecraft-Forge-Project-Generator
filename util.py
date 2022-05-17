import requests as req
import json as json
import os as os
import zipfile as zip

PROMOTED_VERSIONS_URL = "https://files.minecraftforge.net/maven/net/minecraftforge/forge/promotions_slim.json"
# https://maven.minecraftforge.net/net/minecraftforge/forge/{mcver}-{forgever}/forge-{mcver}-{forgever}-mdk.zip
def getForgeVersion(mc_ver = str, promo_type = str) -> str:
    vers = json.loads(req.get(PROMOTED_VERSIONS_URL).text)
    print(vers)
    return dict(dict(vers).get("promos")).get("{mc}-{pro}".format(mc=mc_ver, pro=promo_type))

"""
Downloads the requested forge mdk zip and returns the path
"""
def downloadForgeZip(mc_version = str, promo_type = str) -> str:
    forge_version = getForgeVersion(mc_version, str(promo_type).lower()) 

    base_url = "https://maven.minecraftforge.net/net/minecraftforge/forge/{mc_ver}-{forge_ver}/forge-{mc_ver}-{forge_ver}-mdk.zip/".format(mc_ver=mc_version, forge_ver=forge_version)

    data = req.get(base_url)

    fs = open("temp.zip", mode='wb')
    fs.write(data.content)
    fs.close()
    
    return os.path.realpath(fs.name)

def unzipFileAtPath(path_to_file = str) :
    with zip.ZipFile(path_to_file, 'r') as ref:
        ref.extractall(path=path_to_file+"\\temp")
