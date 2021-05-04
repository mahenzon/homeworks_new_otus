"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="", server_default="")
    username = Column(String, nullable=False, default="", server_default="")
    email = Column(String, nullable=False, default="", server_default="")

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, user_id={self.user_id}, title={self.title!r}, body={self.body!r})"

    def __repr__(self):
        return str(self)


async def create_tables():
    print("Creating tables for users and posts")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("Done creating tables for users and posts")


async def fill_users_table(users_data):
    print("Adding users to users table")
    async with Session() as session:
        session: AsyncSession

        async with session.begin():
            for user_ in users_data:
                user_added = User(name=user_['name'], username=user_['username'], email=user_['email'])
                session.add(user_added)
    print("Done adding users to users table")


async def fill_posts_table(posts_data):
    print("Adding posts to posts table")
    async with Session() as session:
        session: AsyncSession

        async with session.begin():
            for post_ in posts_data:
                post_added = Post(user_id=post_['userId'], title=post_['title'], body=post_['body'])
                session.add(post_added)
    print("Done adding posts to posts table")
