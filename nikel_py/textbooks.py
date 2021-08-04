import typing
from nikel_py.utils._constants import TEXTBOOKS_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Textbook:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.isbn = response['isbn']
        self.title = response['title']
        self.edition = response['edition']
        self.author = response['author']
        self.image = response['image']
        self.price = response['price']
        self.url = response['url']
        self.courses = response['courses']
        self.last_updated = parser.parse(response["last_updated"])



    @property
    def all_data(self):
        return self._response



class Textbooks:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(TEXTBOOKS_BASE_URL, query, limit)

        return [Textbook(i) for i in r]




    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(TEXTBOOKS_BASE_URL, query, limit)

        return [Textbook(i) for i in r]