import typing
from nikel_py.utils._constants import COURSES_BASE_URL
from nikel_py.utils._getter import _get, _async_get
from dateutil import parser


class Course:

    def __init__(self, response):

        self._response = response

        self.id = response['id']
        self.code = response['code']
        self.name = response['name']
        self.description = response['description']
        self.division = response['division']
        self.department = response['department']
        self.prerequisites = response['prerequisites']
        self.corequisites = response['corequisites']
        self.exclusions = response['exclusions']
        self.recommended_preparation = response['recommended_preparation']
        self.level = response['level']
        self.campus = response['campus']
        self.term = response['term']
        self.arts_and_science_breadth = response['arts_and_science_breadth']
        self.arts_and_science_distribution = response['arts_and_science_distribution']
        self.utm_distribution = response['utm_distribution']
        self.utsc_breadth = response['utsc_breadth']
        self.apsc_electives = response['apsc_electives']
        self.meeting_sections = response['meeting_sections']
        self.last_updated = parser.parse(response["last_updated"])


    @property
    def all_data(self):
        return self._response



class Courses:


    @staticmethod
    def get(query : typing.Dict = None, limit : int = 10):

        r = _get(COURSES_BASE_URL, query, limit)

        return [Course(i) for i in r]




    @staticmethod
    async def async_get(query : typing.Dict = None, limit : int = 10):

        r = await _async_get(COURSES_BASE_URL, query, limit)

        return [Course(i) for i in r]




