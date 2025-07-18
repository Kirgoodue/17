import os
import psycopg2
import time

# Получаем переменные окружения
db_host = os.getenv("POSTGRES_HOST")
db_user = os.getenv("POSTGRES_USER")
db_name = os.getenv("POSTGRES_DB")

# Читаем пароль из файла секрета
with open('/run/secrets/DB_PASSWORD', 'r') as file:
    db_password = file.read().strip()

print(f"Connecting to: host={db_host}, user={db_user}, password={db_password}, db={db_name}")

# Подключение к базе данных
conn = psycopg2.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    port=5432
)
print("Connected to DB!")
conn.close()