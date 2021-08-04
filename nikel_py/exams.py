import typing
from nikel_py.utils._constants import EXAMS_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Exam:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.course_id = response['course_id']
        self.course_code = response['course_code']
        self.campus = response['campus']
        self.date = response['date']
        self.start = response['start']
        self.end = response['end']
        self.duration = response['duration']
        self.sections = response['sections']
        self.last_updated = parser.parse(response["last_updated"])


    @property
    def all_data(self):
        return self._response



class Exams:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(EXAMS_BASE_URL, query, limit)

        return [Exam(i) for i in r]



    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(EXAMS_BASE_URL, query, limit)

        return [Exam(i) for i in r]