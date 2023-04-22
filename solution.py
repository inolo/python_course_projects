import sqlite3
import hashlib

if __name__ == '__main__':

    """Create/Connect to DB"""
    try:
        conn = sqlite3.connect('./sqlite.db')
        c = conn.cursor()
    except Exception as e:
        print("UNABLE TO CONNECT TO DATABASE")
        print(e)

    phrase_1 = c.execute("""SELECT CODE FROM SECRET_CODE where code_number = 75 """).fetchone()
    phrase_2 = c.execute("""SELECT CODE FROM SECRET_CODE where code_number = 202 """).fetchone()
    phrase_3 = c.execute("""SELECT CODE FROM SECRET_CODE where code_number = 233 """).fetchone()

    phrase_joined = phrase_1[0] + phrase_2[0] + phrase_3[0]
    print(phrase_joined)
    hash_phrase = hashlib.sha256(phrase_joined.encode("utf-8")).hexdigest()

    success_phrase = c.execute(f"""SELECT SUCCESS_MESSAGE from SUCCESS_MESSAGE WHERE success_hash = '{hash_phrase}'""").fetchone()
    print(success_phrase[0])
