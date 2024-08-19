from sqlalchemy.orm import relationship,mapped_column,Mapped,Session,DeclarativeBase
from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,AsyncAttrs,async_sessionmaker

from config import MYSQL_URL

engine = create_async_engine(MYSQL_URL, echo=True)

async_session = async_sessionmaker(engine)


class Base(DeclarativeBase,AsyncAttrs):
    pass 


class Category(Base):
    __tablename__ = 'category'

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(50))

    games = relationship('Game',back_populates='category')


class GameKey(Base):
    __tablename__ = 'game_key'

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    key:Mapped[str] = mapped_column(String(50))
    count:Mapped[int] = mapped_column(Integer, default=0)
    price:Mapped[int] = mapped_column(Integer, default=0)


    game = relationship('Game',back_populates='key', uselist=False)


class Game(Base):
    __tablename__ = 'game'

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(50))
    description:Mapped[str] = mapped_column(String(250))
    image:Mapped[str] = mapped_column(String(250))
    category_id:Mapped[int] = mapped_column(ForeignKey('category_id'))
    key_id:Mapped[int] = mapped_column(ForeignKey('game_key.id', unique=True))

    category = relationship('Category',back_populates='games')
    key = relationship('GameKey',back_populates='game', uselist=False)
















