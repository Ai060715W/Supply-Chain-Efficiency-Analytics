-- ===============================
-- Supply Chain Efficiency Analytics
-- Schema for SQLite / MySQL
-- ===============================

-- ------------------------------
-- 产品表
-- ------------------------------
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    sku VARCHAR(50) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(20),
    unit VARCHAR(20),
    safety_stock INT
);

-- ------------------------------
-- 供应商表
-- ------------------------------
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    location VARCHAR(20),
    rating DECIMAL(3,2)
);

-- ------------------------------
-- 采购订单表
-- ------------------------------
CREATE TABLE purchase_orders (
    purchase_order_id INT PRIMARY KEY,
    product_id INT NOT NULL,
    supplier_id INT NOT NULL,
    quantity INT,
    lead_time_days INT,
    purchase_order_date DATETIME,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- ------------------------------
-- 库存表
-- ------------------------------
CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT,
    warehouse_location VARCHAR(50),
    last_updated DATETIME,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ------------------------------
-- 入库记录表
-- ------------------------------
CREATE TABLE inbound_records (
    inbound_id INT PRIMARY KEY,
    purchase_order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity_received INT,
    received_date DATETIME,
    FOREIGN KEY (purchase_order_id) REFERENCES purchase_orders(purchase_order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ------------------------------
-- 销售订单表
-- ------------------------------
CREATE TABLE sales_orders (
    sales_order_id INT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity_sold INT,
    sales_order_date DATETIME,
    customer_name VARCHAR(100),
    status VARCHAR(20),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
