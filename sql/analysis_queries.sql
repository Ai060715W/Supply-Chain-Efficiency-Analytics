-- ------------------------------
-- 1. 每个产品的总采购数量
-- ------------------------------
SELECT product_id, SUM(quantity) AS total_purchased
FROM purchase_orders
GROUP BY product_id
ORDER BY total_purchased DESC;

-- ------------------------------
-- 2. 每个产品的总销售数量
-- ------------------------------
SELECT product_id, SUM(quantity_sold) AS total_sold
FROM sales_orders
GROUP BY product_id
ORDER BY total_sold DESC;

-- ------------------------------
-- 3. 库存余量（每个产品在所有仓库的总库存）
-- ------------------------------
SELECT product_id, SUM(quantity) AS total_inventory
FROM inventory
GROUP BY product_id
ORDER BY total_inventory DESC;

-- ------------------------------
-- 4. 产品入库及时率（采购到入库平均天数）
-- ------------------------------
SELECT po.product_id,
       AVG(JULIANDAY(ir.received_date) - JULIANDAY(po.purchase_order_date)) AS avg_lead_days
FROM purchase_orders po
JOIN inbound_records ir ON po.purchase_order_id = ir.purchase_order_id
GROUP BY po.product_id
ORDER BY avg_lead_days;

-- ------------------------------
-- 5. 库存不足报警（库存小于安全库存的产品）
-- ------------------------------
SELECT i.product_id, i.quantity, p.safety_stock
FROM inventory i
JOIN products p ON i.product_id = p.product_id
WHERE i.quantity < p.safety_stock;

-- ------------------------------
-- 6. 每个供应商的平均评分和采购数量
-- ------------------------------
SELECT s.supplier_id, s.supplier_name, s.rating, SUM(po.quantity) AS total_purchased
FROM suppliers s
LEFT JOIN purchase_orders po ON s.supplier_id = po.supplier_id
GROUP BY s.supplier_id, s.supplier_name, s.rating
ORDER BY total_purchased DESC;

-- ------------------------------
-- 7. 最近30天销售情况
-- ------------------------------
SELECT product_id, SUM(quantity_sold) AS sold_last_30_days
FROM sales_orders
WHERE sales_order_date >= DATE('now', '-30 days')
GROUP BY product_id
ORDER BY sold_last_30_days DESC;


-- ------------------------------
-- 8. 产品库存周转率（Stock Turnover Rate）
-- ------------------------------
WITH avg_inventory AS (
    SELECT product_id, AVG(quantity) AS avg_qty
    FROM inventory
    GROUP BY product_id
),
total_sales AS (
    SELECT product_id, SUM(quantity_sold) AS total_sold
    FROM sales_orders
    GROUP BY product_id
)
SELECT t.product_id,
       t.total_sold,
       a.avg_qty,
       CASE WHEN a.avg_qty > 0 THEN ROUND(t.total_sold*1.0 / a.avg_qty,2) ELSE NULL END AS stock_turnover_ratio
FROM total_sales t
JOIN avg_inventory a ON t.product_id = a.product_id
ORDER BY stock_turnover_ratio DESC;

-- ------------------------------
-- 9. 仓库库存占用率
-- ------------------------------
WITH total_inventory AS (
    SELECT SUM(quantity) AS total_qty
    FROM inventory
)
SELECT warehouse_location,
       SUM(quantity) AS warehouse_qty,
       ROUND(SUM(quantity)*1.0 / (SELECT total_qty FROM total_inventory), 4) AS inventory_ratio
FROM inventory
GROUP BY warehouse_location
ORDER BY inventory_ratio DESC;

-- ------------------------------
-- 10. 供应商交货及时率（On-time Delivery Rate）
-- ------------------------------
SELECT s.supplier_id, s.supplier_name,
       COUNT(ir.inbound_id) AS total_orders,
       SUM(CASE WHEN JULIANDAY(ir.received_date) <= JULIANDAY(po.purchase_order_date) + po.lead_time_days THEN 1 ELSE 0 END) AS on_time_deliveries,
       ROUND(SUM(CASE WHEN JULIANDAY(ir.received_date) <= JULIANDAY(po.purchase_order_date) + po.lead_time_days THEN 1 ELSE 0 END)*1.0 / COUNT(ir.inbound_id),4) AS on_time_rate
FROM suppliers s
JOIN purchase_orders po ON s.supplier_id = po.supplier_id
JOIN inbound_records ir ON po.purchase_order_id = ir.purchase_order_id
GROUP BY s.supplier_id, s.supplier_name
ORDER BY on_time_rate DESC;

-- ------------------------------
-- 11. 最近 7 天库存告急产品
-- ------------------------------
SELECT i.product_id, p.product_name, SUM(i.quantity) AS total_inventory, p.safety_stock
FROM inventory i
JOIN products p ON i.product_id = p.product_id
JOIN sales_orders s ON i.product_id = s.product_id
WHERE s.sales_order_date >= DATE('now', '-7 days')
GROUP BY i.product_id, p.product_name, p.safety_stock
HAVING total_inventory < p.safety_stock
ORDER BY total_inventory ASC;
