import typing
from nikel_py.utils._constants import FOOD_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Food:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.name = response['name']
        self.description = response['description']
        self.tags = response['tags']
        self.campus = response['campus']
        self.address = response['address']
        self.coordinates = response['coordinates']
        self.hours = response['hours']
        self.image = response['image']
        self.twitter = response["twitter"]
        self.facebook = response["facebook"]
        self.attributes = response["attributes"]
        self.last_updated = parser.parse(response["last_updated"])



    @property
    def all_data(self):
        return self._response



class Foods:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(FOOD_BASE_URL, query, limit)

        return [Food(i) for i in r]



    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(FOOD_BASE_URL, query, limit)

        return [Food(i) for i in r]