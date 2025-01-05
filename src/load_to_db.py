import psycopg2 as psycopg
import os
from dotenv import load_dotenv
import uuid
from extract_csv import extract_csv
from transform_data import get_products_menu, transform_data

extracted_csv = extract_csv('belfast_17-12-2024_09-00-00.csv') #example
data = transform_data(extracted_csv) #example


load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")


def db_connect():
    try: 
        with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:
            print('successfully connected')
            return connection
    except Exception as ex:
        print('Failed to:', ex)


def write_products(data, connection=db_connect()):
    cursor = connection.cursor()
    products = get_products_menu(data)
    
    for item in products:
        products_id = str(uuid.uuid4())
        sql=f"""SELECT EXISTS(SELECT 1 FROM products WHERE product_name='{item['name']}')"""
        cursor.execute(sql)
        result = cursor.fetchone()[0]

        if result:
            continue
        else:
            sql= f"""
                INSERT into products (product_id, product_name, price) VALUES ('{products_id}','{item['name']}', {float(item['price'])});
                """
            cursor.execute(sql)
    connection.commit()
    cursor.close()

write_products(data) # -- example


def write_transactions_and_ordered_products(data, connection=db_connect()):
    cursor = connection.cursor()

    for item in data: 
        transaction_id = str(uuid.uuid4())
        transaction_sql= f"""
            INSERT into transactions (transaction_id, "timestamp", total_amount, payment_method, store_name) VALUES ('{transaction_id}','{item['Timestamp']}', {float(item['total_amount'])}, '{item['payment_method']}', '{item['location']}');
            """
        cursor.execute(transaction_sql)

        products = item['item_purchased']
        for item in products: 
            product_sql = f"""
            SELECT product_id, price FROM products WHERE product_name = '{item['name']}';
            """
            cursor.execute(product_sql)
            products = cursor.fetchone()
            product_id = products[0]

            ordered_product_sql = f"""
                INSERT INTO ordered_products (transaction_id, product_id, product_quantity)
                VALUES ('{transaction_id}', '{product_id}', {item['quantity']});
                """
            cursor.execute(ordered_product_sql)
    connection.commit()
    cursor.close()

write_transactions_and_ordered_products(data) # -- example