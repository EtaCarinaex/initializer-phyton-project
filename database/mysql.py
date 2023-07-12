import pymysql.cursors


def _mysql_local_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='Sametbegg1',
                           db='ngta',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)


def _fetch_all(connection, select_script):
    connection.connect()
    try:
        with connection.cursor() as mysql:
            mysql.execute(select_script)
            data = mysql.fetchall()
            print(data)
    finally:
        mysql.close()
        connection.close()

    return data


def _fetch_one(connection, select_script):
    connection.connect()
    try:
        with connection.cursor() as mysql:
            mysql.execute(select_script)
            data = mysql.fetchall()
            print(data)
    finally:
        mysql.close()
        connection.close()

    return data


def _insert_data(connection, insertscript, data):
    connection.connect()
    try:
        with connection.cursor() as db:
            row_size = db.executemany(insertscript, data)
    finally:
        db.close()
        connection.close()
    return row_size


def _delete_data(connection, delete_script):
    connection.connect()
    try:
        with connection.cursor() as db:
            row_size = db.execute(delete_script)
            db.commit()
    finally:
        db.close()
        connection.close()

    return row_size


def _update_data(connection, update_script):
    connection.connect()
    try:
        with connection.cursor() as db:
            row_size = db.execute(update_script)
    finally:
        db.close()
        connection.close()

    return row_size
