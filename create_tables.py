import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Run's all the drop table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: connection to the database
    :return: None

    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Run's all the create table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: connection to the database
    :return: None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Driver main function.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    print("Table dropped successfully!!")

    create_tables(cur, conn)
    print("Table created successfully!!")

    conn.close()


if __name__ == "__main__":
    main()