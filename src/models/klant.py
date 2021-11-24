class Klant:
    def __init__(self, data: dict):
        if data is None:
            return

        self.__achternaam = data.get('achternaam')
        self.__voornaam = data.get('voornaam')
        self.__adres = data.get('adres')
        self.__postcode = data.get('postcode')
        self.__woonplaats = data.get('woonplaats')
        self.__land = data.get('land')

    def values(self):
        return [self.voornaam, self.achternaam, self.adres, self.postcode, self.woonplaats, self.land]

    def attributes(self):
        return ('voornaam', 'achternaam', 'adres', 'postcode', 'woonplaats', 'land')

    def setAchternaam(self, achternaam):
        self.__achternaam = achternaam

    def getAchternaam(self):
        return self.__achternaam
    achternaam = property(getAchternaam, setAchternaam)

    def setVoornaam(self, voornaam):
        self.__voornaam = voornaam

    def getVoornaam(self):
        return self.__voornaam
    voornaam = property(getVoornaam, setVoornaam)

    def setAdres(self, adres):
        self.__adres = adres

    def getAdres(self):
        return self.__adres
    adres = property(getAdres, setAdres)

    def setPostcode(self, postcode):
        self.__postcode = postcode

    def getPostcode(self):
        return self.__postcode
    postcode = property(getPostcode, setPostcode)

    def setWoonplaats(self, woonplaats):
        self.__woonplaats = woonplaats

    def getWoonplaats(self):
        return self.__woonplaats
    woonplaats = property(getWoonplaats, setWoonplaats)

    def setLand(self, land):
        self.__land = land

    def getLand(self):
        return self.__land
    land = property(getLand, setLand)