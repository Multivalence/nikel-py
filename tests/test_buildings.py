import unittest
from nikel_py import Buildings

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


class BuildingsTestCase(unittest.TestCase):

    def test_sync(self):

        #Gets name of Building where the Postal Code contains M5S

        x = Buildings.get({'address' : '~M5S'}, limit=1)[0]
        self.assertEqual(x.name, "University College")


    @async_wrapper
    async def test_async(self):

        #Gets Code of Building that has the name 'Hart House'

        x = await Buildings.async_get({'name' : 'Hart House'}, limit=1)
        x = x[0]
        self.assertEqual(x.code, "HH")




if __name__ == '__main__':

    unittest.main()