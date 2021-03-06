import unittest
from nikel_py import Services

import asyncio

def async_wrapper(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
    return wrapper


'''
Data is subject to change. As such, Test Cases may or may not work in the future
'''

class ServicesTestCase(unittest.TestCase):

    def test_sync(self):


        #Gets name of Service that has the building ID '143'

        x = Services.get({'building_id' : '143'}, limit=1)[0]
        self.assertEqual(x.name, "Career Exploration and Education")


    @async_wrapper
    async def test_async(self):

        #Gets campus for 'John P. Robarts Research Library' Service

        x = await Services.async_get({'name' : 'John P. Robarts Research Library'}, limit=1)
        x = x[0]
        self.assertEqual(x.campus, "St. George")




if __name__ == '__main__':

    unittest.main()