import sqlite3
import numpy as np


def creat_table(tabel_name_list, db_name):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        for i in range(0, len(tabel_name_list)):
            c.execute("CREATE TABLE {} ([ID] INTEGER PRIMARY KEY AUTOINCREMENT,[KEYPOINT] TEXT NOT NULL);".format(
                tabel_name_list[i]))

        conn.commit()
        conn.close()

    except Exception as e:
        print(e)


def drop_table(tabel_name_list):
    try:
        conn = sqlite3.connect('face.db')
        c = conn.cursor()

        for i in range(0, len(tabel_name_list)):
            c.execute("DROP TABLE {};".format(tabel_name_list[i]))

        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def append_data(tabel_name, data_list):
    try:
        conn = sqlite3.connect('face.db')
        c = conn.cursor()

        for i in range(0, len(data_list)):
            c.execute("INSERT INTO {} VALUES (NULL, \'{}\');".format(tabel_name, data_list[i]))

        conn.commit()
        conn.close()

        print("Append data success!")
    except Exception as e:
        print(e)


def read_one_tabel_data(tabel_name):
    try:
        keypoint_list = []

        conn = sqlite3.connect('face.db')
        c = conn.cursor()

        cursor = c.execute("SELECT KEYPOINT from {};".format(tabel_name))
        for i in cursor:
            data_core = np.array(i[0].split())
            keypoint_list.append(data_core.astype(np.float))

        conn.commit()
        conn.close()

        return (keypoint_list)

    except Exception as e:
        print(e)
