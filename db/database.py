from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL="postgresql+psycopg2://postgres:postgres@db:5432"
user_name = "user"
password = "password"
host = "db"
database_name = "sample_db"

SQLALCHEMY_DATABASE_URL = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)


# engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf-8', echo=True)

engine = create_engine('mysql+pymysql://user:password@db:3306/sample_db', encoding='utf-8', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()