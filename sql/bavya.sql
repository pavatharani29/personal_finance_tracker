CREATE TABLE Employees (
    EmpID INT,
    EmpName VARCHAR(50),
    Salary INT,
    Bonus INT
);

-- Inserting sample data
INSERT INTO Employees (EmpID, EmpName, Salary, Bonus)
VALUES
(1, 'Amit', 40000, 5000),
(2, 'Neha', 50000, 7000),
(3, 'Ravi', 30000, 3000);

-- Using Arithmetic Operators
SELECT
    EmpName,
    Salary,
    Bonus,
    Salary + Bonus AS Total_Income,          -- Addition
    Salary - Bonus AS After_Bonus_Deduction, -- Subtraction
    Salary * 0.10 AS Ten_Percent_Salary,     -- Multiplication
    Salary / 12 AS Monthly_Salary,           -- Division
    Salary % 10000 AS Salary_Remainder       -- Modulus
FROM Employees;
