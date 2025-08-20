-- Создайте в базе данных полный набор информации о студенте, заполнив все таблички:

-- 1. Создайте студента (student)

INSERT INTO students (name, second_name) VALUES ('Август', 'Августинин')

-- 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

INSERT INTO books (title, taken_by_student_id) VALUES ('Python for AQA', 21040)
INSERT INTO books (title, taken_by_student_id) VALUES ('Java for AQA', 21040)
INSERT INTO books (title, taken_by_student_id) VALUES ('SQL for AQA', 21040)
INSERT INTO books (title, taken_by_student_id) VALUES ('JS for AQA', 21040)

-- 3. Создайте группу (group) и определите своего студента туда

INSERT INTO `groups` (title, start_date, end_date) VALUES ('AQA_tester', 'may 2025', 'sep 2025')
UPDATE students SET group_id = 5563 where id = 21040

-- 4. Создайте несколько учебных предметов (subjects)

INSERT INTO subjects (title) VALUES ('Basics of programming')
INSERT INTO subjects (title) VALUES ('SQL Basics')

-- 5. Создайте по два занятия для каждого предмета (lessons)

INSERT INTO lessons (title, subject_id) VALUES ('lesson_1', 11720)
INSERT INTO lessons (title, subject_id) VALUES ('lesson_2', 11720)
INSERT INTO lessons (title, subject_id) VALUES ('lesson_1', 11721)
INSERT INTO lessons (title, subject_id) VALUES ('lesson_2', 11721)

-- 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 11820, 21040)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 11821, 21040)
INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 11822, 21040)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 11823, 21040)

-- Получите информацию из базы данных:
-- Все оценки студента

SELECT value FROM marks WHERE student_id = 21040

-- Все книги, которые находятся у студента

SELECT title FROM books WHERE taken_by_student_id = 21040

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

SELECT s.id, s.name, s.second_name, g.title, g.start_date, g.end_date, b.title, m.value, l.title, sub.title
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 21040