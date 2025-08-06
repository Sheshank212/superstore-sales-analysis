-- Superstore Sales Analysis Project
-- author: Sheshank


-- create database
CREATE DATABASE superstore;
USE superstore;

-- create table --
CREATE TABLE superstore_orders (
    Row_ID INT,
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Ship_Date DATE,
    Ship_Mode VARCHAR(50),
    Customer_ID VARCHAR(20),
    Customer_Name VARCHAR(100),
    Segment VARCHAR(50),
    Country VARCHAR(50),
    City VARCHAR(100),
    State VARCHAR(50),
    Postal_Code INT,
    Region VARCHAR(50),
    Product_ID VARCHAR(50),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name VARCHAR(255),
    Sales FLOAT,
    Quantity INT,
    Discount FLOAT,
    Profit FLOAT
);



-- test
SELECT * FROM superstore_orders LIMIT 10;

-- Top 10 Products by Total Sales
SELECT `Product Name`, SUM(Sales) AS Total_Sales
FROM superstore_orders
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;

-- Total Sales by Category (Descending)
SELECT Category, SUM(Sales) AS Total_Sales
FROM superstore_orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Sales by Year
SELECT YEAR(`Order Date`) AS Order_Year, SUM(Sales) AS Total_Sales
FROM superstore_orders
GROUP BY Order_Year
ORDER BY Order_Year;

-- Monthly Sales Trend in 2017
SELECT 
  DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
  SUM(Sales) AS Total_Sales
FROM superstore_orders
WHERE YEAR(`Order Date`) = 2017
GROUP BY Month
ORDER BY Month;

-- Top 5 States by Profit (if column exists)
SELECT State, SUM(Profit) AS Total_Profit
FROM superstore_orders
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 5;

-- Products with Most Discounts
SELECT `Product Name`, AVG(Discount) AS Avg_Discount
FROM superstore_orders
GROUP BY `Product Name`
ORDER BY Avg_Discount DESC
LIMIT 10;

-- Segment-Wise Profit Analysis
SELECT Segment, SUM(Profit) AS Total_Profit
FROM superstore_orders
GROUP BY Segment
ORDER BY Total_Profit DESC;

-- Most Ordered Products (by Quantity)
SELECT `Product Name`, SUM(Quantity) AS Total_Quantity
FROM superstore_orders
GROUP BY `Product Name`
ORDER BY Total_Quantity DESC
LIMIT 10;

-- Profit Margin by Category
SELECT Category,
       ROUND(SUM(Profit)/SUM(Sales) * 100, 2) AS Profit_Margin_Percentage
FROM superstore_orders
GROUP BY Category
ORDER BY Profit_Margin_Percentage DESC;

-- Loss-Making Products (Negative Profit)
SELECT `Product Name`, SUM(Profit) AS Total_Profit
FROM superstore_orders
GROUP BY `Product Name`
HAVING Total_Profit < 0
ORDER BY Total_Profit ASC
LIMIT 10;

-- Sales and Profit by Region
SELECT Region, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
FROM superstore_orders
GROUP BY Region;

-- Average Sales per Order
SELECT ROUND(AVG(Sales), 2) AS Avg_Sales_Per_Order
FROM superstore_orders;



