import os
import csv
import mysql.connector as mysql
import dotenv


dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


with open(okulik_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

select_query = '''
SELECT s.name AS name, s.second_name AS second_name, g.title AS group_title, b.title AS book_title,
        s2.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
FROM students s
JOIN books b
ON s.id = b.taken_by_student_id
JOIN `groups` g
ON s.group_id = g.id
JOIN marks m
ON s.id = m.student_id
JOIN lessons l
ON m.lesson_id = l.id
JOIN subjects s2
ON l.subject_id  = s2.id
'''
cursor = db.cursor(dictionary=True)
cursor.execute(select_query)
data_db = cursor.fetchall()

new_data = [row for row in data if row not in data_db]

for row in new_data:
    print(row)

db.close()
