import unittest
from _async_testing import async_wrapper
from nikel_py import Parking

'''
Data is subject to change. As such, Test Cases may or may not work in the future
'''


class ParkingTestCase(unittest.TestCase):

    def test_sync(self):

        #Gets first parking spot that appears in API (No Filter)

        x = Parking.get(limit=1)[0]
        self.assertEqual(x.alias, "Faculty of Education")


    @async_wrapper
    async def test_async(self):

        #Gets Address of a Parking spot at the Mississauga Campus. The parking spot must also have a name that starts with 'Alumni'

        x = await Parking.async_get({'campus' : 'Mississauga', 'name' : '(Alumni'}, limit=1)
        x = x[0]
        self.assertEqual(x.address, "3353 Mississauga Road North")




if __name__ == '__main__':

    unittest.main()