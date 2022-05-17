ALL_FORGE_VERSIONS_URL = "https://files.minecraftforge.net/maven/net/minecraftforge/forge/maven-metadata.xml"
PROMOTED_VERSIONS_URL = "https://files.minecraftforge.net/maven/net/minecraftforge/forge/promotions_slim.json"

# https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.1.0/forge-1.18.2-40.1.0-mdk.zip
# https://maven.minecraftforge.net/net/minecraftforge/forge/{mcver}-{forgever}/forge-{mcver}-{forgever}-mdk.zip

import json as json
import xml.etree.ElementTree as ET
import requests as req
import window 

promo_vers = req.get(PROMOTED_VERSIONS_URL).text


print(promo_vers)
#ver_json_obj = json.loads(promo_vers)
#dict(ver_json_obj).pop('homepage')
#promos = list(dict(ver_json_obj).get('promos'))
#print(promos)

#print(promo_vers)

window.setupWindowBasics()
