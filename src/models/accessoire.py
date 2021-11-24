MERK_KEY = 'merk'
TYPES_KEY = 'types'
DAG_PRIJS_KEY = 'dagprijs'
NIEUW_PRIJS_KEY = 'nieuwprijs'


class Accessoires:
    _merk: str = None
    _types: str = None
    _dagprijs: str = None
    _nieuwprijs: str = None

    def __init__(self, data: dict):
        if data is None:
            return

        self.merk = data.get(MERK_KEY)
        self.types = data.get(TYPES_KEY)
        self.dagprijs = data.get(DAG_PRIJS_KEY)
        self.nieuwprijs = data.get(NIEUW_PRIJS_KEY)

    def values(self):
        return [self.merk, self.types, self.dagprijs, self.nieuwprijs]

    def attributes(self):
        return ('merk', 'types', 'dagprijs', 'nieuwprijs')

    @property
    def merk(self) -> str:
        return self._merk

    @merk.setter
    def merk(self, merk: str) -> None:
        self._merk = merk

    @property
    def types(self) -> str:
        return self._types

    @types.setter
    def types(self, types) -> None:
        self._types = types

    @property
    def dagprijs(self) -> str:
        return self._dagprijs

    @dagprijs.setter
    def dagprijs(self, dagprijs) -> None:
        self._dagprijs = dagprijs

    @property
    def nieuwprijs(self) -> str:
        return self._nieuwprijs

    @nieuwprijs.setter
    def nieuwprijs(self, nieuwprijs) -> None:
        self._nieuwprijs = nieuwprijs
