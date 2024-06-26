import aiosqlite
from database import sql_quaries


class AsyncDatabase:
    def __init__(self, db_path='db.sqlite3'):
        self.db_path = db_path

    async def create_table(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(sql_quaries.CREATE_USER_TABLE_QUERY)

            await db.commit()
            print("Database connected successfully")

    async def execute_query(self, query, params=None, fetch="none"):
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query, params or ())

            if fetch == "none":
                await db.commit()
                return
            elif fetch == "all":
                data = await cursor.fetchall()
                return [dict(row) for row in data] if data else []