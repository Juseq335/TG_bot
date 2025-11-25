from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger

# Сreating a database
engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

# Connecting to the database
async_session = async_sessionmaker(engine)

# Сreating a child class in relation to AsyncAttrs and DeclarativeBase
class Base(AsyncAttrs, DeclarativeBase):
    pass

# Child class in relation to Base
class Users(Base):
    __tablename__ = 'users'             # Name of the database table
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

# Function for initializing database tables
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)    # Creating all the classes in the database described above
