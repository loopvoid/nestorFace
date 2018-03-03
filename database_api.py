import sqlite3
import numpy as np


def create_table(db_name, table_name_list):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        for i in range(0, len(table_name_list)):
            c.execute("CREATE TABLE {} ([ID] INTEGER PRIMARY KEY AUTOINCREMENT,[KEYPOINT] TEXT NOT NULL);".format(
                table_name_list[i]))

        conn.commit()
        conn.close()

    except Exception as e:
        print(e)


def drop_table(db_name, table_name_list):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        for i in range(0, len(table_name_list)):
            c.execute("DROP TABLE {};".format(table_name_list[i]))

        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def append_data(db_name, table_name, data_list):
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        for i in range(0, len(data_list)):
            c.execute("INSERT INTO {} VALUES (NULL, \'{}\');".format(table_name, data_list[i]))

        conn.commit()
        conn.close()

        print("Append data success!")
    except Exception as e:
        print(e)


def read_one_table_data(db_name, table_name):
    try:
        key_point_list = []

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        cursor = c.execute("SELECT KEYPOINT from {};".format(table_name))
        for i in cursor:
            data_core = np.array(i[0].split())
            key_point_list.append(data_core.astype(np.float))

        conn.commit()
        conn.close()

        return key_point_list

    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_table("test.db", ["Aen", "Ben"])
    drop_table("test.db", ["Ben"])
    create_table("test.db", ["Ben"])
    append_data("test.db", "Ben", [1, 2, 3])
    print(read_one_table_data("test.db", "Ben"))
