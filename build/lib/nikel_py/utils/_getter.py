import typing
import aiohttp
import requests
from nikel_py.utils._urlparser import url_parse
from nikel_py.utils.errors import NoDataFound, ResponseError


def _get(base_url : str, query : typing.Dict = None, limit : int = 10):

    url = base_url if not query else url_parse(base_url, query, limit)


    try:

        r = requests.get(url)

        if r.status_code != 200:
            raise ResponseError

        r = r.json()

    except Exception:
        raise ResponseError


    if len(r['response']) >= 1:
        return r['response']


    else:
        raise NoDataFound






async def _async_get(base_url : str, query : typing.Dict = None, limit : int = 10):

    url = base_url if not query else url_parse(base_url, query, limit)


    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:

                if resp.status != 200:
                    raise ResponseError

                r = await resp.json()

    except Exception:
        raise ResponseError


    if len(r['response']) >= 1:
        return r['response']


    else:
        raise NoDataFound