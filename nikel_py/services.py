import typing
from nikel_py.utils._constants import SERVICES_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Service:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.name = response['name']
        self.description = response['description']
        self.campus = response['campus']
        self.alias = response['alias']
        self.building_id = response['building_id']
        self.image = response['image']
        self.coordinates = response['coordinates']
        self.tags = response['tags']
        self.attributes = response['attributes']
        self.last_updated = parser.parse(response["last_updated"])



    @property
    def all_data(self):
        return self._response



class Services:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(SERVICES_BASE_URL, query, limit)

        return [Service(i) for i in r]




    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(SERVICES_BASE_URL, query, limit)

        return [Service(i) for i in r]