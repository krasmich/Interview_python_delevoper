import aiohttp
import asyncio
import os


async def download_coroutine(session, url):
    async with session.get(url) as response:
        filename = os.path.basename(url)
        with open(filename, 'wb') as f_handle:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f_handle.write(chunk)
        return await response.release()


async def main(loop):
    urls = ["http://127.0.0.1:8000/books.html", "http://127.0.0.1:8000/sport.html"]

    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            await download_coroutine(session, url)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
