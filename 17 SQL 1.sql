-- i. To list names, department and date of hiring of all teachers in ascending order of date of joining.
SELECT NAME, DEPARTMENT, HIREDATE FROM TEACHER ORDER BY HIREDATE ASC;

-- ii. To count the number of teachers in English department.
SELECT COUNT(*) FROM TEACHER WHERE DEPARTMENT = 'English';

-- iii. Display the department and hire date of all the female teachers whose salary is more than 25000.
SELECT DEPARTMENT, HIREDATE FROM TEACHER WHERE GENDER = 'F' AND SALARY > 25000;

-- iv. Display the list of teachers whose name starts with ‘S’.
SELECT NAME FROM TEACHER WHERE NAME LIKE 'S%';

-- v. Display the total salary of female teachers from Hindi department.
SELECT SUM(SALARY) FROM TEACHER WHERE GENDER = 'F' AND DEPARTMENT = 'Hindi';

-- vi. Display the maximum, average, minimum and total salary of teacher department wise.
SELECT DEPARTMENT, MAX(SALARY), AVG(SALARY), MIN(SALARY), SUM(SALARY) FROM TEACHER GROUP BY DEPARTMENT;

-- vii. Display the sum of salary of teacher who have joined after ‘2018-01-01’.
SELECT SUM(SALARY) FROM TEACHER WHERE HIREDATE > '2018-01-01';

-- viii. To increase the salary by 5% of all PGT teachers.
UPDATE TEACHER SET SALARY = SALARY * 1.05 WHERE CATEGORY = 'PGT';

