import typing
from nikel_py.utils._constants import PROGRAMS_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Program:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.name = response['name']
        self.description = response['description']
        self.campus = response['campus']
        self.type = response['type']
        self.enrollment = response['enrollment']
        self.completion = response['completion']
        self.last_updated = parser.parse(response["last_updated"])



    @property
    def all_data(self):
        return self._response



class Programs:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(PROGRAMS_BASE_URL, query, limit)

        return [Program(i) for i in r]




    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(PROGRAMS_BASE_URL, query, limit)

        return [Program(i) for i in r]