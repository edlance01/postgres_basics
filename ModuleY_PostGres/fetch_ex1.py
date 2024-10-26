import psycopg2
from config import load_config
import random
import string


def get_vendors_with_fetch_one():
    """Retrieve data from the vendors table"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name"
                )
                print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_vendors_with_fetch_all():
    """Retrieve data from the vendors table"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name"
                )
                rows = cur.fetchall()
                print("The number of parts: ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)




if __name__ == "__main__":
    print("\nGet Vendors with Fetch One:")
    get_vendors_with_fetch_one()
    print("\nGet Vendors with Fetch All:")
    get_vendors_with_fetch_all()
