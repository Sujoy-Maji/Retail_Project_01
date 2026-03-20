-- 1. Create Enterprise Schema
CREATE TABLE sales_data (
    order_id INT PRIMARY KEY,
    transaction_date DATETIME,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10, 2),
    store_location VARCHAR(100),
    hour_of_day INT,
    month VARCHAR(20),
    total_revenue DECIMAL(10, 2)
);

-- 2. Time-Series Trend (Revenue by Month)
SELECT month, SUM(total_revenue) AS monthly_revenue
FROM sales_data
GROUP BY month
ORDER BY monthly_revenue DESC;

-- 3. Product Performance (Top Revenue Generators)
SELECT product_name, category, SUM(total_revenue) AS total_revenue, SUM(quantity) AS units_sold
FROM sales_data
GROUP BY product_name, category
ORDER BY total_revenue DESC;

-- 4. Peak Hour Foot Traffic (For Heatmap Design)
SELECT store_location, hour_of_day, COUNT(order_id) AS foot_traffic, SUM(total_revenue) AS hourly_revenue
FROM sales_data
GROUP BY store_location, hour_of_day
ORDER BY store_location, hour_of_day;
