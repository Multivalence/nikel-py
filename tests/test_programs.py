import unittest
from _async_testing import async_wrapper
from nikel_py import Programs


'''
Data is subject to change. As such, Test Cases may or may not work in the future
'''


class ProgramsTestCase(unittest.TestCase):

    def test_sync(self):


        #Gets type for program that starts with 'Computer Science' and is done at the St. George campus

        x = Programs.get({'campus' : 'St. George', 'name' : '(Computer Science'}, limit=1)[0]
        self.assertEqual(x.type, "major")


    @async_wrapper
    async def test_async(self):

        #Gets name of program that requires 4 credits and is done at the Mississauga Campus

        x = await Programs.async_get({'campus' : 'Mississauga', 'description' : '(4.0'}, limit=1)
        x = x[0]
        self.assertEqual(x.name, "History of Religions (Arts)")




if __name__ == '__main__':

    unittest.main()