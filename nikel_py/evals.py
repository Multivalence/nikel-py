import typing
from nikel_py.utils._constants import EVALS_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Eval:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.campus = response['campus']
        self.name = response['name']
        self.terms = response['terms']
        self.last_updated = parser.parse(response["last_updated"])


    @property
    def all_data(self):
        return self._response



class Evals:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(EVALS_BASE_URL, query, limit)

        return [Eval(i) for i in r]




    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(EVALS_BASE_URL, query, limit)

        return [Eval(i) for i in r]