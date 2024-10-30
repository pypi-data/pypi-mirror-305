from typing import Any, List

import sqlalchemy as sa

from .utils import compile_statement, get_connection_pool, logger


class PgPoolConn:
    @classmethod
    async def create(cls, pg_url: str, max_conn: int = 10):
        self = cls()
        self.pool = await get_connection_pool(pg_url, max_conn=max_conn)
        return self

    async def execute(self, query: Any) -> List[Any]:
        async with self.pool.acquire() as conn:
            return await conn.execute(compile_statement(query))

    async def fetch(self, query: sa.Select) -> List[Any]:
        async with self.pool.acquire() as conn:
            return await conn.fetch(compile_statement(query))

    async def fetchrow(self, query: sa.Select) -> List[Any]:
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(compile_statement(query))

    async def fetchval(self, query: sa.Select) -> List[Any]:
        async with self.pool.acquire() as conn:
            return await conn.fetchval(compile_statement(query))

    async def close(self):
        logger.info("Closing asyncpg connection pool.")
        await self.pool.close()
