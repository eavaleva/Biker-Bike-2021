class Medewerker:
    def __init__(self, data: dict):
        if data is None:
            return

        self._voornaam = data.get('voornaam')
        self._achternaam = data.get('achternaam')
        self._rol = data.get('rol')
        self._loginnaam = data.get('loginnaam')

    def values(self):
        return [self.voornaam, self.achternaam, self.rol, self.loginnaam]

    def attributes(self):
        return ('voornaam', 'achternaam', 'rol', 'loginnaam')

    #  Getter/Setter voornaam
    def setVoornaam(self, voornaam):
        self._voornaam = voornaam

    def getVoornaam(self):
        return self._voornaam

    voornaam = property(getVoornaam, setVoornaam)

    # Getter/Setter achternaam
    def setAchternaam(self, achternaam):
        self._achternaam = achternaam

    def getAchternaam(self):
        return self._achternaam

    achternaam = property(getAchternaam, setAchternaam)

    # Getter/Setter rol
    def setrol(self, rol):
        self._rol = rol

    def getrol(self):
        return self._rol

    rol = property(getrol, setrol)

    # Getter/Setter login-naam
    def setloginnaam(self, loginnaam):
        self._loginnaam = loginnaam

    def getloginnaam(self):
        return self._loginnaam

    loginnaam = property(getloginnaam, setloginnaam)