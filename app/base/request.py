from app.base.database import async_session
from app.base.database import User
from sqlalchemy import select

# Writing a user id to the database
async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(Users).where(Users.tg_id == tg_id))
        
        #If the user is not in the database, then he will write it down.
        #This database was created for fun, it can be removed.
        if not user:
            session.add(Users(tg_id=tg_id))
            await session.commit()
