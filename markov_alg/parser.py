import aiohttp
import asyncio
import requests

from bs4 import BeautifulSoup


class PythonDocsParser(object):
    urls = ["https://docs.python.org/3/tutorial/appetite.html",
            "https://docs.python.org/3.6/tutorial/datastructures.html",
            "https://docs.python.org/3/tutorial/interpreter.html",
            "https://docs.python.org/3/tutorial/introduction.html",
            "https://docs.python.org/3/tutorial/controlflow.html",
            "https://docs.python.org/3/tutorial/modules.html"]

    def __init__(self):
        pass

    @staticmethod
    def parse_url(url):
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')

        docs = soup.findAll('div', {'class': 'body'})[0].findAll('p')
        return "\n".join((p.text.replace("\n", " ") for p in docs))

    def parse(self):
        return "\n".join([self.parse_url(url) for url in self.urls])


class AsyncPythonDocsParser(PythonDocsParser):
    def __init__(self):
        super().__init__()
        self.results = []

    async def parse_url(self, url, session):
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')

            docs = soup.findAll('div', {'class': 'body'})[0].findAll('p')
        return "\n".join((p.text.replace("\n", " ") for p in docs))

    async def parse_a(self, loop):
        async with aiohttp.ClientSession(loop=loop) as session:
            reqs = [self.parse_url(url, session) for url in self.urls]
            return await asyncio.gather(*reqs, loop=loop)

    def parse(self):

        loop = asyncio.new_event_loop()
        res = loop.run_until_complete(self.parse_a(loop))
        return "\n".join(res)
