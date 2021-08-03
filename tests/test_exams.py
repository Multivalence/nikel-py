import unittest
from _async_testing import async_wrapper
from nikel_py import Exams


'''
Data is subject to change. As such, Test Cases may or may not work in the future
'''


class ExamsTestCase(unittest.TestCase):

    def test_sync(self):

        #Gets campus for 'MAT102' Exam

        x = Exams.get({'course_code' : 'MAT102'}, limit=1)[0]
        self.assertEqual(x.campus, "Mississauga")


    @async_wrapper
    async def test_async(self):

        #Gets course code for exam that starts at '2019-06-25'

        x = await Exams.async_get({'date' : '2019-06-25'}, limit=1)
        x = x[0]
        self.assertEqual(x.course_code, "ACT230H1F")




if __name__ == '__main__':

    unittest.main()