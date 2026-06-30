from sqlalchemy import create_engine

DATABASE_URL = "postgresql://myai:myai123@localhost:5432/myai"

engine = create_engine(
    DATABASE_URL,
    future=True
)