import os
import psycopg2
import streamlit as st


def _get_url():
    try:
        return st.secrets["database"]["url"]
    except (KeyError, AttributeError, FileNotFoundError):
        pass
    url = os.environ.get("DATABASE_URL")
    if url is None:
        raise RuntimeError(
            "No database URL found. Add it to .streamlit/secrets.toml as:\n"
            "[database]\nurl = \"postgresql://...\""
        )
    return url


def _get_connection():
    return psycopg2.connect(_get_url())


def _ensure_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id        SERIAL PRIMARY KEY,
                run_id    TEXT    NOT NULL,
                trial     INTEGER,
                difficulty INTEGER,
                side      TEXT,
                response  TEXT,
                correct   TEXT,
                participant TEXT,
                condition TEXT,
                comment   TEXT
            )
        """)
    conn.commit()


def commit_run(dataframe, run_id, comment):
    conn = _get_connection()
    try:
        _ensure_table(conn)
        with conn.cursor() as cur:
            for _, row in dataframe.iterrows():
                cur.execute(
                    """
                    INSERT INTO results
                        (run_id, trial, difficulty, side, response, correct,
                         participant, condition, comment)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        run_id,
                        row.get("trial_history"),
                        row.get("difficulty_history"),
                        row.get("side_history"),
                        row.get("response_history"),
                        row.get("correct_history"),
                        row.get("participant"),
                        row.get("condition"),
                        comment,
                    ),
                )
        conn.commit()
    finally:
        conn.close()
