import typing
from nikel_py.utils._constants import BUILDINGS_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Building:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.code = response['code']
        self.name = response['name']
        self.tags = response['tags']
        self.short_name = response['short_name']
        self.address = response['address']
        self.coordinates = response['coordinates']
        self.last_updated = parser.parse(response["last_updated"])


    @property
    def all_data(self):
        return self._response



class Buildings:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(BUILDINGS_BASE_URL, query, limit)

        return [Building(i) for i in r]


    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(BUILDINGS_BASE_URL, query, limit)

        return [Building(i) for i in r]