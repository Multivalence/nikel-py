import typing
from nikel_py.utils._constants import PARKING_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Park:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.name = response['name']
        self.description = response['description']
        self.campus = response['campus']
        self.address = response['address']
        self.coordinates = response['coordinates']
        self.alias = response['alias']
        self.building_id = response['building_id']
        self.last_updated = parser.parse(response["last_updated"])



    @property
    def all_data(self):
        return self._response



class Parking:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(PARKING_BASE_URL, query, limit)

        return [Park(i) for i in r]




    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(PARKING_BASE_URL, query, limit)

        return [Park(i) for i in r]