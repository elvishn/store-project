import sys
import os
from pathlib import Path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.append(str(project_root))
from src.order_service.models.database import get_db

conn = get_db()
cursor = conn.cursor()

cursor.execute("SELECT * FROM status")
statuses = cursor.fetchall()

print('Status table:')
for row in statuses:
    print(f'ID: {row["id"]}, Type: {row["type"]}')
conn.close()

