import psycopg
from app.config import settings

with psycopg.connect(settings.database_url, prepare_threshold=None) as conn:
    print("Connected.")

    ext = conn.execute("SELECT extname FROM pg_extension WHERE extname='vector'").fetchone()
    print("vector extension:", ext)

    tables = conn.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY 1"
    ).fetchall()
    print("tables:", [t[0] for t in tables])

    dim = conn.execute(
        "SELECT atttypmod FROM pg_attribute WHERE attrelid='chunks'::regclass AND attname='embedding'"
    ).fetchone()
    print("embedding dimension:", dim[0])

    print("resumes rows:", conn.execute("SELECT count(*) FROM resumes").fetchone()[0])
    print("chunks rows:", conn.execute("SELECT count(*) FROM chunks").fetchone()[0])