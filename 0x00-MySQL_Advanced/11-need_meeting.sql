-- script creates a view, named need_meeting that lists all students that have a score under 80 and 
CREATE VIEW need_meeting AS SELECT name FROM students WHERE score < 80 AND last_meeting IS NULL OR last_meeting > CURDATE() - 30;
