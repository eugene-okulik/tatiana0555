import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1. Создайте студента (student)
cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ('Mark', 'Anderson'))
student_id = cursor.lastrowid

# 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_books_query, [
        ('Full Stack Testing', student_id),
        ('Effective Software Testing', student_id)
    ]
)

# 3. Создайте группу (group) и определите своего студента туда
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Python_for_AQA','may 2025', 'sep 2025' )")
group_id = cursor.lastrowid
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

# 4. Создайте несколько учебных предметов (subjects)
cursor.execute("INSERT INTO subjects (title) VALUES ('Python OOP Practice')")
subject1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('SQL Advanced')")
subject2_id = cursor.lastrowid

# 5. Создайте по два занятия для каждого предмета (lessons)
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('lesson1', subject1_id))
lesson1_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('lesson2', subject1_id))
lesson2_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('lesson3', subject2_id))
lesson3_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('lesson4', subject2_id))
lesson4_id = cursor.lastrowid

# 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
insert_marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_marks_query, [
        (5, lesson1_id, student_id),
        (4, lesson2_id, student_id),
        (5, lesson3_id, student_id),
        (4, lesson4_id, student_id)
    ]
)

db.commit()

# Получите информацию из базы данных:
# Все оценки студента
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
all_marks = cursor.fetchall()
print(f'All marks of the student: {all_marks}')

# Все книги, которые находятся у студента
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
all_books = cursor.fetchall()
print(f'All books assigned to the student: {all_books}')

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий
# и предметов (всё одним запросом с использованием Join)
select_query = '''
SELECT
    s.id AS student_id,
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    sub.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark_value
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = %s
'''
cursor.execute(select_query, (student_id,))
full_information = cursor.fetchall()
print(f'All information related to the student is: {full_information}')

db.close()
