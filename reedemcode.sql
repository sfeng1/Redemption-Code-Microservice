-- Read all relevant data from customers table
SELECT customerID, customerName, customerEmail, totalRevenue, count (DISTINCT  ) as salesCount 
     FROM Customers 
     JOIN Sales
