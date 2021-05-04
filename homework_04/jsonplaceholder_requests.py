from dataclasses import dataclass
from aiohttp import ClientSession
from loguru import logger


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class Service:
    name: str
    url: str


users_service = Service("users", USERS_DATA_URL)
posts_service = Service("posts", POSTS_DATA_URL)


async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_json_list(service: Service):
    """
    :param service:
    :return:
    """
    async with ClientSession() as session:
        result = await fetch(session, service.url)

    logger.info("Got {} results for {}, result {}", len(result), service.name, result)
    return result


async def fetch_users():
    return await fetch_json_list(users_service)


async def fetch_posts():
    return await fetch_json_list(posts_service)
