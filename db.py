import psycopg2
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)

    
def add_product(name: str, photo_path: str, price: float, old_price: float, url_product: str, sex: str, brand: str):
    conn = psycopg2.connect('postgres://isrzeyjx:P4wzfAfwaiJmP_zCdYuvVPp0fcMkBvXl@cornelius.db.elephantsql.com/isrzeyjx')
    cursor = conn.cursor()
    sql = """INSERT INTO products (name, photo_path, price, old_price, url_product, date, sex, brand) VALUES ('%s', '%s', %s, %s, '%s', '%s', '%s', '%s') ON CONFLICT (url_product) DO NOTHING""" % (name, photo_path, price, old_price, url_product, formatted_date, sex, brand)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return conn.close()
