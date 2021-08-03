import unittest
from nikel_py import Evals

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


class CoursesTestCase(unittest.TestCase):

    def test_sync(self):

        #Gets ID of Eval associated with 'Intro to Academic Studies'
        x = Evals.get({'name' : 'Intro to Academic Studies'}, limit=1)[0]
        self.assertEqual(x.id, "ABP100Y1")


    @async_wrapper
    async def test_async(self):

        #Gets name of Eval associated with the St. George Campus
        x = await Evals.async_get({'campus' : 'St. George'}, limit=1)
        x = x[0]
        self.assertEqual(x.name, "Intro to Academic Studies")




if __name__ == '__main__':

    unittest.main()