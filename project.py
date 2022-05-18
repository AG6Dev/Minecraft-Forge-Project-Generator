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
        self.descrption = kwargs.get("description")
        self.domain = kwargs.get("domain")
        self.game_ver = mc_ver
        self.promo = promo_type.lower()



