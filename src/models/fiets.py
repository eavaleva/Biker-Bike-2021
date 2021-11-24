# Container van Biker Fiets.py

class Fiets:
    def __init__(self, data: dict):
        if data is None:
            return

        self._type = data.get('types')
        self._merk = data.get('merk')
        self._dagprijs = data.get('dagprijs')
        self._borg = data.get('borg')


    def values(self):
        return [self.type, self.merk, self.dagprijs, self.borg]

    def attributes(self):
        return ('types', 'merk', 'dagprijs', 'borg')

    # getter setter van type fiets
    def get_type(self):
        return self._type

    def set_type(self, x):
        self._type = x

    type = property(get_type, set_type)

    # getter en setter van merk fiets
    def get_merk(self):
        return self._merk

    def set_merk(self, x):
        self._merk = x

    merk = property(get_merk, set_merk)

    # getter en setter van dagprijs fiets
    def get_dagprijs(self):
        return self._dagprijs

    def set_dagprijs(self, x):
        self._dagprijs = x

    dagprijs = property(get_dagprijs, set_dagprijs)    
    # getter en setter van borg fiets
    def get_borg(self):
        return self._borg

    def set_borg(self, x):
        self._borg = x

    borg = property(get_borg, set_borg)
