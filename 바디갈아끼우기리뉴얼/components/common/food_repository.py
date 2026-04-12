from database.db import get_connection
from database.queries import Product


def fetch_food_rows(keyword=""):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        if keyword.strip():
            cursor.execute(
                Product.product_search_query,
                (f"%{keyword.strip()}%",),
            )
        else:
            cursor.execute(Product.product_list_query)

        rows = cursor.fetchall()
        return rows, None

    except Exception as err:
        if conn is not None:
            conn.rollback()
        return None, f"사료 조회 실패: {err}"

    finally:
        if cursor:
            cursor.close()
        if conn is not None and getattr(conn, "closed", 1) == 0:
            conn.close()