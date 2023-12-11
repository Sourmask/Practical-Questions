-- i. To display Customer name and corresponding set name from the tables Customer and Mobile
SELECT A.Cname, B.SetName FROM CUSTOMER A, MOBILE B WHERE A.ID = B.ID AND A.Connection = 'Jio';

-- ii. To display the customer name, connection and the corresponding set name with price more than 250.
SELECT A.Cname, A.Connection, B.SetName FROM CUSTOMER A, MOBILE B WHERE A.ID = B.ID AND B.Price > 250;

-- iii. To display the details of all Iphone customers.
SELECT A.* FROM CUSTOMER A, MOBILE B WHERE A.ID = B.ID AND B.SetName = 'Iphone';

-- iv. To count the number of customers with BSNL connection who uses Samsung phone.
SELECT COUNT(*) FROM CUSTOMER A, MOBILE B WHERE A.ID = B.ID AND A.Connection = 'BSNL' AND B.SetName = 'Samsung';

-- v. To display the Cname, Validity and SetName of all Jio customers.
SELECT A.Cname, A.Validity, B.SetName FROM CUSTOMER A, MOBILE B WHERE A.ID = B.ID AND A.Connection = 'Jio';
