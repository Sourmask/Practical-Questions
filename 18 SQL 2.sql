-- i. To list the names of female patients who are in ENT department.
SELECT Name FROM HOSPITAL WHERE Gender='F' AND Department='ENT';

-- ii. To list the details of patients in descending order of their Date of admission.
SELECT * FROM HOSPITAL ORDER BY Dateofadm DESC;

-- iii. To display patient’s name, Charges, Age for only female patients.
SELECT Name, Charges, Age FROM HOSPITAL WHERE Gender='F';

-- iv. To display the details patients whose department ends with the letter ‘c’.
SELECT * FROM HOSPITAL WHERE Department LIKE '%c';

-- v. To count the number of male patients in Surgery department
SELECT COUNT(*) FROM HOSPITAL WHERE Gender='M' AND Department='Surgery';

-- vi. To display total charges for male and female patients separately.
SELECT Gender, SUM(Charges) FROM HOSPITAL GROUP BY Gender;

-- vii. To display the different departments in the table HOSPITAL.
SELECT DISTINCT Department FROM HOSPITAL;
