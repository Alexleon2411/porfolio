from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE BYTEA USING "image"::BYTEA;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE VARCHAR(255) USING "image"::VARCHAR(255);
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE VARCHAR(255) USING "image"::VARCHAR(255);
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE VARCHAR(255) USING "image"::VARCHAR(255);
        ALTER TABLE "skills" ALTER COLUMN "image" TYPE VARCHAR(255) USING "image"::VARCHAR(255);"""
