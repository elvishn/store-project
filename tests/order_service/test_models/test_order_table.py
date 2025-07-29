import sys
import os
from pathlib import Path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.append(str(project_root))
from src.order_service.models.database import get_db

conn = get_db()
cursor = conn.cursor()

cursor.execute("PRAGMA table_info('orders')")
columns = cursor.fetchall()
print('Orders table columns:')
for col in columns:
    print(f'{col["name"]}: {col["type"]}')

cursor.execute("""
SELECT sql FROM sqlite_master
WHERE tbl_name = 'orders' and type = 'table'
""")
print('\nTable Definition')
print(cursor.fetchone()[0])
conn.close()