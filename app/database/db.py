# from psycopg2 import sql
# generic access to database should be implemented here
# but more specific ones should be implemented in their respective class folders

# eg. Function to pick the best card for an user should be implemented at user/db.py


'''eg of a generic function:
def count_rows(table_name: str) -> int:
    with connection.cursor() as cursor:
        stmt = sql.SQL("""
            SELECT
                count(*)
            FROM
                {table_name}
        """).format(
            table_name = sql.Identifier(table_name),
        )
        cursor.execute(stmt)
        result = cursor.fetchone()

    rowcount, = result
    return rowcount
'''