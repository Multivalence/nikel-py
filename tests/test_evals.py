import unittest
from nikel_py import Evals

class CoursesTestCase(unittest.TestCase):

    def test_sync(self):

        x = Courses.get({'code' : '(CSC'}, limit=1)[0]
        self.assertEqual(x.name, "Introduction to Computer Programming")



class CoursesAsyncTestCase(unittest.IsolatedAsyncioTestCase):

    async def test_async(self):

        x = await Courses.async_get({'name' : 'Introduction to Computer Programming'}, limit=1)
        x = x[0]
        self.assertEqual(x.code, "CSC108H1")




if __name__ == '__main__':

    unittest.main()