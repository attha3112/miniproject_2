import sqlite3
from typing import Optional, Dict, Any


#membuat database terlebih dahulu untuk login dan register

db_name = "log_reg.db"

#Membuat database awal
def init_db():
    '''Creating A table'''
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    #membuat table 
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS log_reg(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nama TEXT,
            password TEXT)
            ''')
    conn.commit()
    conn.close()



#fungsi untuk menyimpan hasil reg kedalam database
def save_reg(nama : str, password : str):
    '''Save register result'''
    conn  = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO log_reg(nama, password)
        VALUES(?, ?)''', (nama, password))

    conn.commit()
    conn.close()


#fungsi untuk check apakah ada username sudah terdaftar atau belum di database untuk menghindari duplikasi
def check_user_exist(nama):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    #mencari user berdasarkan nama, tidak di proses di file 'login' karena proses looping berada di database
    cursor.execute('SELECT nama FROM log_reg WHERE nama =?', (nama))
    result = cursor.fetchone()

    conn.close()

    #jika nilai return bukan None, maka username sudah ada
    return result is not None


#fungsi untuk verifikasi user
def verify_user(nama, password):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM log_reg WHERE nama = ? AND password = ?", (nama, password))
    result = cursor.fetchone()

    #jika hasil return match(cocok), maka login valid atau success
    return result is not None



# ==== DATABASE SERVER ====


db_name2 = "server.db"


def init_db2():
    '''Membuat table untuk Data server'''
    conn = sqlite3.connect(db_name2)
    cursor = conn.cursor()

    #membuat table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS server.db(
        server_id TEXT
        SSH_Port INTEGER PRIMARY KEY AUTOINCREMENT,
        STATUS TEXT)
        ''')
    conn.commit()
    conn.close()