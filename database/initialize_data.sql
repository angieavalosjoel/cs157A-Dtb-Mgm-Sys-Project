-- Initialize Data for EduTrack

-- Insert students
INSERT INTO students (FirstName, LastName, Email, Username, Password) VALUES
('Alice', 'Anderson', 'alice.anderson@school.edu', 'alice.anderson', 'Pass123!Alice45'),
('Bob', 'Brown', 'bob.brown@school.edu', 'bob.brown', 'BrownBob!2024'),
('Charlie', 'Chen', 'charlie.chen@school.edu', 'charlie.chen', 'ChenChar!7890'),
('Diana', 'Davis', 'diana.davis@school.edu', 'diana.davis', 'DianaPass!2024'),
('Edward', 'Evans', 'edward.evans@school.edu', 'edward.evans', 'EdEvans!12345'),
('Fiona', 'Foster', 'fiona.foster@school.edu', 'fiona.foster', 'FionaFost!789'),
('George', 'Garcia', 'george.garcia@school.edu', 'george.garcia', 'GeorgeGar!2024'),
('Hannah', 'Harris', 'hannah.harris@school.edu', 'hannah.harris', 'HannahH!1234'),
('Ian', 'Ivanov', 'ian.ivanov@school.edu', 'ian.ivanov', 'IanIvan!5678'),
('Julia', 'Johnson', 'julia.johnson@school.edu', 'julia.johnson', 'JuliaJohn!90'),
('Kevin', 'Kim', 'kevin.kim@school.edu', 'kevin.kim', 'KevinKim!2024'),
('Laura', 'Lee', 'laura.lee@school.edu', 'laura.lee', 'LauraLee!123'),
('Michael', 'Martinez', 'michael.martinez@school.edu', 'michael.martinez', 'MikeMart!456'),
('Nancy', 'Nguyen', 'nancy.nguyen@school.edu', 'nancy.nguyen', 'NancyNg!7890'),
('Oliver', 'O''Connor', 'oliver.oconnor@school.edu', 'oliver.oconnor', 'OliveOc!1234'),
('Patricia', 'Parker', 'patricia.parker@school.edu', 'patricia.parker', 'PatPark!567'),
('Quinn', 'Quinn', 'quinn.quinn@school.edu', 'quinn.quinn', 'QuinnQu!8901');

-- Insert instructors
INSERT INTO instructors (FirstName, LastName, Department, Email) VALUES
('Dr. Sarah', 'Smith', 'Computer Science', 'sarah.smith@school.edu'),
('Prof. John', 'Jones', 'Mathematics', 'john.jones@school.edu'),
('Dr. Maria', 'Miller', 'Computer Science', 'maria.miller@school.edu'),
('Prof. David', 'Wilson', 'Physics', 'david.wilson@school.edu'),
('Dr. Emily', 'Moore', 'Computer Science', 'emily.moore@school.edu'),
('Prof. Robert', 'Taylor', 'Mathematics', 'robert.taylor@school.edu'),
('Dr. Lisa', 'Thomas', 'Computer Science', 'lisa.thomas@school.edu'),
('Prof. James', 'Jackson', 'Physics', 'james.jackson@school.edu'),
('Dr. Jennifer', 'White', 'Computer Science', 'jennifer.white@school.edu'),
('Prof. William', 'Harris', 'Mathematics', 'william.harris@school.edu'),
('Dr. Amanda', 'Martin', 'Computer Science', 'amanda.martin@school.edu'),
('Prof. Christopher', 'Thompson', 'Physics', 'christopher.thompson@school.edu'),
('Dr. Jessica', 'Garcia', 'Computer Science', 'jessica.garcia@school.edu'),
('Prof. Daniel', 'Martinez', 'Mathematics', 'daniel.martinez@school.edu'),
('Dr. Ashley', 'Robinson', 'Computer Science', 'ashley.robinson@school.edu'),
('Prof. Matthew', 'Clark', 'Physics', 'matthew.clark@school.edu'),
('Dr. Stephanie', 'Rodriguez', 'Computer Science', 'stephanie.rodriguez@school.edu');

-- Insert courses
INSERT INTO courses (CourseName, Credits, InstructorID) VALUES
('CS101', 3, 1),
('CS157A', 3, 3),
('CS146', 3, 5),
('CS149', 3, 7),
('CS160', 3, 9),
('CS161', 4, 11),
('CS162', 4, 13),
('CS163', 4, 15),
('CS166', 3, 1),
('CS174', 3, 3),
('MATH30', 3, 2),
('MATH31', 4, 6),
('MATH32', 4, 10),
('PHYS50', 3, 4),
('PHYS51', 4, 8),
('CS168', 3, 5),
('CS154', 3, 7),
('CS165', 3, 9);

-- Insert enrollments
INSERT INTO enrollments (StudentID, CourseID, Grade) VALUES
-- Student 1 enrollments
(1, 1, 'A'),
(1, 2, 'B+'),
(1, 3, 'A-'),
(1, 4, 'B'),
(1, 5, 'A'),
-- Student 2 enrollments
(2, 1, 'B+'),
(2, 2, 'A'),
(2, 3, 'B'),
(2, 6, 'A-'),
(2, 7, 'B+'),
-- Student 3 enrollments
(3, 2, 'A'),
(3, 3, 'A'),
(3, 4, 'B+'),
(3, 5, 'A-'),
(3, 8, 'B'),
-- Student 4 enrollments
(4, 1, 'C+'),
(4, 3, 'B'),
(4, 4, 'B-'),
(4, 6, 'C+'),
(4, 7, 'B'),
-- Student 5 enrollments
(5, 2, 'A-'),
(5, 4, 'A'),
(5, 5, 'B+'),
(5, 8, 'A'),
(5, 9, 'A-'),
-- Student 6 enrollments
(6, 1, 'B'),
(6, 2, 'B+'),
(6, 6, 'A'),
(6, 7, 'B'),
(6, 10, 'B+'),
-- Student 7 enrollments
(7, 3, 'A'),
(7, 4, 'A-'),
(7, 5, 'B+'),
(7, 8, 'A'),
(7, 9, 'B+'),
-- Student 8 enrollments
(8, 1, 'C'),
(8, 2, 'B'),
(8, 6, 'B-'),
(8, 7, 'C+'),
(8, 11, 'B'),
-- Student 9 enrollments
(9, 2, 'A'),
(9, 3, 'A-'),
(9, 5, 'A'),
(9, 8, 'B+'),
(9, 10, 'A'),
-- Student 10 enrollments
(10, 1, 'B+'),
(10, 4, 'A-'),
(10, 5, 'B'),
(10, 9, 'A'),
(10, 12, 'B+'),
-- Student 11 enrollments
(11, 3, 'B+'),
(11, 6, 'A'),
(11, 7, 'A-'),
(11, 10, 'B'),
(11, 13, 'B+'),
-- Student 12 enrollments
(12, 2, 'A-'),
(12, 4, 'B+'),
(12, 8, 'A'),
(12, 9, 'B'),
(12, 14, 'A-'),
-- Student 13 enrollments
(13, 1, 'B'),
(13, 5, 'A'),
(13, 6, 'B+'),
(13, 7, 'A-'),
(13, 15, 'B'),
-- Student 14 enrollments
(14, 3, 'A'),
(14, 4, 'A-'),
(14, 10, 'B+'),
(14, 11, 'A'),
(14, 16, 'B+'),
-- Student 15 enrollments
(15, 2, 'B+'),
(15, 5, 'A'),
(15, 8, 'A-'),
(15, 9, 'B'),
(15, 17, 'A'),
-- Student 16 enrollments
(16, 1, 'A-'),
(16, 6, 'B+'),
(16, 7, 'A'),
(16, 12, 'B'),
(16, 18, 'A-'),
-- Student 17 enrollments
(17, 4, 'B'),
(17, 5, 'A-'),
(17, 10, 'B+'),
(17, 11, 'A'),
(17, 13, 'B');

