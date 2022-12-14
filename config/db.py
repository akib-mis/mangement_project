import os

# DB_USER = os.getenv("AGRIM_DB_USER", "postgres")
DB_USER = os.getenv("DEMO_DB_USER", "demouser")
# DB_PASSWORD = os.getenv("AGRIM_DB_PASSWORD", "123456")
DB_PASSWORD = os.getenv("DEMO_DB_PASSWORD", "demopass")
DB_HOST = os.getenv("DEMO_HOST", "localhost")
DB_PORT = os.getenv("DEMO_PORT", "5432")
# DB_NAME = os.getenv("AGRIM_DB_NAME", "agrim")
DB_NAME = os.getenv("DEMO_DB_NAME", "demodb")
SECRET = os.getenv(
    "DEMO_SECRET",
    "e92d1aa5f67ce24713cf638550f5daa84ef5ea3466ae29af8b1ad16fbe6c5fbb",
)

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)