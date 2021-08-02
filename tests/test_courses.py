import unittest
from nikel_py import Courses


'''
Data is subject to change. As such, Test Cases may or may not work in the future
'''

class CoursesTestCase(unittest.TestCase):

    def test_sync(self):

        #Gets name of course that starts with the code 'CSC'

        x = Courses.get({'code' : '(CSC'}, limit=1)[0]
        self.assertEqual(x.name, "Introduction to Computer Programming")



class CoursesAsyncTestCase(unittest.IsolatedAsyncioTestCase):

    async def test_async(self):

        #Gets Course code of a course named 'Introduction to Computer Programming'

        x = await Courses.async_get({'name' : 'Introduction to Computer Programming'}, limit=1)
        x = x[0]
        self.assertEqual(x.code, "CSC108H1")




if __name__ == '__main__':

    unittest.main()