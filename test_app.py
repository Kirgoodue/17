import unittest
import psycopg2
import os

class TestDatabaseConnection(unittest.TestCase):
    def test_db_connection(self):
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            database=os.getenv("POSTGRES_DB"),
            port=5432
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()[0]
        self.assertEqual(result, 1, "Database query did not return expected result")
        conn.close()

if __name__ == '__main__':
    unittest.main()