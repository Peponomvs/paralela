import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="isekaidb",
        user="isekai",
        password="Fr9tL28mQxD7vKcp",
        host="159.223.200.213",
        port=5432
    )
