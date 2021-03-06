import unittest
from nikel_py import Foods

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


class FoodTestCase(unittest.TestCase):

    def test_sync(self):

        #Gets name of Restaurant that starts with 'C' and ends with 'f'

        x = Foods.get({'name' : '(C )f'}, limit=1)[0]
        self.assertEqual(x.name, "Café Reznikoff")



    @async_wrapper
    async def test_async(self):

        #Gets address of Restaurant that provides Gluten Free Items

        x = await Foods.async_get({'attributes' : '~Gluten Free'}, limit=1)
        x = x[0]
        self.assertEqual(x.address, "89 Chestnut Street, Toronto, ON M5G 1R1")




if __name__ == '__main__':

    unittest.main()