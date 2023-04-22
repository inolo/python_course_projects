import sqlite3
import random
import hashlib


# [75, 236, 233, 395, 90, 362, 202, 375]


# def create_code_table(c):
#     try:
#         c.execute('''
#         CREATE TABLE SECRET_CODE (
#             CODE VARCHAR2(200),
#             CODE_NUMBER NUMBER
#         );
#                   ''')
#     except sqlite3.OperationalError as e:
#         pass



if __name__ == '__main__':

    """Create/Connect to DB"""
    try:
        conn = sqlite3.connect('./sqlite.db')
        c = conn.cursor()
    except Exception as e:
        print("UNABLE TO CONNECT TO DATABASE")
        print(e)


    # conn.execute("""DROP TABLE SUCCESS_MESSAGE;""")

    # conn.execute("""CREATE TABLE SUCCESS_MESSAGE
    #                 (success_message varchar2(100), success_hash varchar2(200));""")




    phrase_1 = c.execute("""SELECT CODE FROM SECRET_CODE where code_number = 75 """).fetchone()
    phrase_2 = c.execute("""SELECT CODE FROM SECRET_CODE where code_number = 202 """).fetchone()
    phrase_3 = c.execute("""SELECT CODE FROM SECRET_CODE where code_number = 233 """).fetchone()


    phrase_joined = phrase_1[0] + phrase_2[0] + phrase_3[0]
    hash_phrase = hashlib.sha256(phrase_joined.encode("utf-8")).hexdigest()

    success_phrase = "Jordan Love is MVP"
    print(hash_phrase)
    conn.execute(f"""INSERT INTO SUCCESS_MESSAGE
                    (success_message, success_hash)
                    values
                    (?,?) 
                   """,(success_phrase, hash_phrase))
    conn.commit()









