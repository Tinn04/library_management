-- 10 users 
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (1, 'Alice', 'Smith', 'alice95@gmail.com', '604-555-5315', '2011-08-24', 'Adult');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (2, 'Bob', 'Johnson', 'bob2@outlook.com', '604-973-6808', '2016-10-17', 'Child');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (3, 'Calvin', 'Weng', 'calvincoolweng@shaw.ca', '604-153-5875', '1903-12-06', 'Youth');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (4, 'Diana', 'Williams', 'dianawillnot@hotmail.com', '604-456-6002', '2023-09-22', 'Child');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (5, 'Eri', 'Snow', 'erinotsnow@hotmail.com', '604-494-4148', '2021-05-12', 'Toddler');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (6, 'Fiona', 'Garcia', 'fiona46@shaw.ca', '604-808-2706', '2015-04-27', 'Adult');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (7, 'George', 'Haunted', 'georgeisnothaunted@hotmail.com', '604-839-8665', '2014-06-10', 'Adult');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (8, 'Hannah', 'Banana', 'hannahbanana1@hotmail.com', '604-759-2062', '2015-07-07', 'Youth');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (9, 'Ian', 'Kim', 'iankimk@telus.net', '604-372-7969', '2019-10-14', 'Adult');
INSERT INTO User(userID, firstName, lastName, email, phone, membershipDate, category) VALUES (10, 'Julia', 'Xingming', 'juliahero27@hotmail.com', '604-399-9147', '2017-02-12', 'Senior');
-- 10 employees
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (1, 'Alison', 'Swift', 'alice99@library.org', '604-594-4859', '2014-10-13', 'Manager');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (2, 'Bob', 'Builder', 'bob10@library.org', '604-586-7409', '2012-11-24', 'Technician');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (3, 'Colton', 'Johns', 'coltbolt@library.org', '604-381-2678', '2024-02-20', 'Receptionist');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (4, 'Diana', 'Leonas', 'dianaff15@library.org', '604-276-7701', '2018-03-06', 'Assistant');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (5, 'Erickson', 'Jonas', 'ericksonnotjonas@library.org', '604-610-1601', '2021-07-29', 'Receptionist');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (6, 'Ferris', 'Mason', 'ferriswheel@library.org', '604-370-3616', '2012-05-03', 'Manager');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (7, 'Garry', 'Jerrison', 'garrywithg@library.org', '604-465-7224', '2018-06-09', 'Assistant');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (8, 'Hannah', 'Veranda', 'hannahbanana2@library.org', '604-189-1557', '2017-05-02', 'Receptionist');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (9, 'Ivern', 'Forest', 'grompkrugs@library.org', '604-498-7437', '2017-01-24', 'Assistant');
INSERT INTO Employee(employeeID, firstName, lastName, email, phone, hireDate, role) VALUES (10, 'Jerry', 'Garrison', 'jerrywithj@library.org', '604-781-6562', '2011-07-01', 'Technician');
-- 10 rooms
INSERT INTO Room(roomID, roomName, capacity) VALUES (1, 'Multipurpose Room', 88);
INSERT INTO Room(roomID, roomName, capacity) VALUES (2, 'The ROOM!', 68);
INSERT INTO Room(roomID, roomName, capacity) VALUES (3, 'Lecture Room', 73);
INSERT INTO Room(roomID, roomName, capacity) VALUES (4, 'Theatre Room', 95);
INSERT INTO Room(roomID, roomName, capacity) VALUES (5, 'Green Room', 57);
INSERT INTO Room(roomID, roomName, capacity) VALUES (6, 'Break Room', 52);
INSERT INTO Room(roomID, roomName, capacity) VALUES (7, 'Study Room 1', 17);
INSERT INTO Room(roomID, roomName, capacity) VALUES (8, 'Study Room 2', 20);
INSERT INTO Room(roomID, roomName, capacity) VALUES (9, 'Office Room', 54);
INSERT INTO Room(roomID, roomName, capacity) VALUES (10, 'Board Room', 53);
-- 10 items
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (1, 'Tin Talks', 'CD', 'Calvin Weng', '2005-06-25', 'Tin', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (2, 'Life as a Frog', 'Journal', 'Publisher 2', '2000-03-28', 'Frogadier', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (3, 'Bizarre News at the Castle', 'Magazine', 'Maggy Publishing', '2001-09-11', 'Maggy', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (4, 'Solemn Journey', 'Journal', 'Nova Nexus', '2009-12-18', 'Nolan N', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (5, 'How To Tie a Tie', 'CD', 'Dad Tutorials', '2015-11-23', 'Dad', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (6, "Chef Jo's Cookbook", 'Book', 'Chef Publishing', '2018-10-25', 'Jojo', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (7, 'Mora the Explorer', 'DVD', 'Nora', '2016-11-30', 'Flora', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (8, 'Fast and Angry', 'DVD', 'Anger', '2022-06-19', 'Dominos', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (9, 'LeBron: The Chosen One', 'Book', 'King', '2022-05-07', 'James', 'Available');
INSERT INTO Item(itemID, title, format, publisher, publishDate, author, status) VALUES (10, 'The Number 10', 'CD', 'Two Hands Publishing', '1991-08-22', 'Greeky', 'Available');
-- 10 events
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (1, 'Clay Mugs', 'Description 1', '2025-04-15', '14:00', '16:00', 'Workshop', 'Senior', 10);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (2, 'Tech Startup', 'Description 2', '2025-11-24', '14:00', '16:00', 'Networking', 'Adult', 4);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (3, 'Tin Talks', 'Description 3', '2024-10-04', '14:00', '16:00', 'Presentation', 'Toddler', 2);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (4, 'Woodworking', 'Description 4', '2024-02-25', '14:00', '16:00', 'Workshop', 'Senior', 10);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (5, 'Shrek', 'Description 5', '2025-06-28', '14:00', '16:00', 'Movie', 'Child', 1);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (6, "Calvin's Communications", 'Description 6', '2024-03-20', '14:00', '16:00', 'Presentation', 'Adult', 2);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (7, 'Fire Safety', 'Description 7', '2025-03-01', '14:00', '16:00', 'Presentation', 'Child', 4);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (8, 'Turkey Drawings', 'Description 8', '2025-04-02', '14:00', '16:00', 'Workshop', 'Child', 4);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (9, 'El Camino', 'Description 9', '2024-10-29', '14:00', '16:00', 'Movie', 'Adult', 5);
INSERT INTO Event(eventID, title, description, date, startTime, endTime, type, targetAudience, roomID) VALUES (10, 'Social Skills', 'Description 10', '2025-02-27', '14:00', '16:00', 'Workshop', 'Child', 10);
-- 10 attendance
INSERT INTO Attendance(userID, eventID) VALUES (8, 5);
INSERT INTO Attendance(userID, eventID) VALUES (8, 4);
INSERT INTO Attendance(userID, eventID) VALUES (3, 8);
INSERT INTO Attendance(userID, eventID) VALUES (8, 6);
INSERT INTO Attendance(userID, eventID) VALUES (5, 2);
INSERT INTO Attendance(userID, eventID) VALUES (2, 10);
INSERT INTO Attendance(userID, eventID) VALUES (1, 10);
INSERT INTO Attendance(userID, eventID) VALUES (10, 1);
INSERT INTO Attendance(userID, eventID) VALUES (1, 5);
INSERT INTO Attendance(userID, eventID) VALUES (7, 6);
-- 10 instances of borrows
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (1, 1, 2, '2023-09-24', '2023-10-08', '2023-10-08', 0.30);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (2, 9, 3, '2024-02-29', '2024-03-14', '2024-03-20', 3.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (3, 2, 1, '2023-08-20', '2023-09-03', '2023-09-03', 0.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (4, 6, 5, '2024-12-16', '2024-12-30', '2024-12-23', 0.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (5, 8, 4, '2023-08-02', '2023-08-16', '2023-08-09', 5.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (6, 7, 7, '2023-03-06', '2023-03-20', '2023-03-26', 3.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (7, 3, 8, '2024-08-24', '2024-09-07', '2024-09-07', 0.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (8, 5, 10, '2023-05-27', '2023-06-10', '2023-06-10', 0.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (9, 10, 9, '2024-03-08', '2024-03-22', '2024-03-28', 3.00);
INSERT INTO Borrow(borrowID, userID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (10, 4, 6, '2023-08-02', '2023-08-16', '2023-08-22', 3.00);
-- 10 volunteers
INSERT INTO Volunteer(userID, eventID, role) VALUES (1, 3, 'Guide')
INSERT INTO Volunteer(userID, eventID, role) VALUES (1, 6, 'Guide')
INSERT INTO Volunteer(userID, eventID, role) VALUES (1, 9, 'Translator')
INSERT INTO Volunteer(userID, eventID, role) VALUES (3, 6, 'Leader')
INSERT INTO Volunteer(userID, eventID, role) VALUES (6, 3, 'Guide')
INSERT INTO Volunteer(userID, eventID, role) VALUES (7, 1, 'Helper')
INSERT INTO Volunteer(userID, eventID, role) VALUES (4, 2, 'Leader')
INSERT INTO Volunteer(userID, eventID, role) VALUES (10, 8, 'Translator')
INSERT INTO Volunteer(userID, eventID, role) VALUES (9, 6, 'Guide')
INSERT INTO Volunteer(userID, eventID, role) VALUES (9, 4, 'Translator')