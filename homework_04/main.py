"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции):
- инициализация бд
- создание таблиц
- загрузка пользователей и постов
- добавление пользователей и постов в базу данных
- закрытие соединения с БД
"""
import asyncio
from models import create_tables, fill_users_table, fill_posts_table
from jsonplaceholder_requests import fetch_users, fetch_posts


async def async_main():
    await create_tables()
    async with asyncio.TaskGroup() as tg:
        users_task = tg.create_task(fetch_users())
        posts_task = tg.create_task(fetch_posts())

    users_data = users_task.result()
    posts_data = posts_task.result()
    await fill_users_table(users_data)
    await fill_posts_table(posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
