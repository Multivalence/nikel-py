import unittest
from nikel_py import Textbooks

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

class TextbooksTestCase(unittest.TestCase):

    def test_sync(self):

        #Gets Textbook URL for course that has the code 'CSC'

        x = Textbooks.get({'courses' : '~CSC'}, limit=1)[0]
        self.assertEqual(x.url, "https://uoftbookstore.com/buy_book_detail.asp?pf_id=10554753")



    @async_wrapper
    async def test_async(self):

        #Gets name of a textbook that costs less than $300

        x = await Textbooks.async_get({'price' : '<300'}, limit=1)
        x = x[0]
        self.assertEqual(x.title, "Where The Wild Things Are")




if __name__ == '__main__':

    unittest.main()