import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 项目根目录
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

def ensure_dirs():
    os.makedirs(RAW_DIR, exist_ok=True)
    print(f"[OK] 目录已确保：{RAW_DIR}")

# ----------------- 生成产品 -----------------
def generate_products(n=200):
    df = pd.DataFrame({
        "product_id": range(1, n + 1),
        "sku": [f"SKU{1000+i}" for i in range(n)],
        "product_name": [f"Product {i}" for i in range(n)],
        "category": np.random.choice(["A", "B", "C"], n),
        "unit": ["pcs"] * n,
        "safety_stock": np.random.randint(50, 200, n)
    })
    out = os.path.join(RAW_DIR, "products.csv")
    df.to_csv(out, index=False)
    print(f"[OK] 生成 products.csv -> {out}")
    return df

# ----------------- 生成供应商 -----------------
def generate_suppliers(n=50):
    df = pd.DataFrame({
        "supplier_id": range(1, n + 1),
        "supplier_name": [f"Supplier {i}" for i in range(n)],
        "location": np.random.choice(["CN", "US", "EU"], n),
        "rating": np.random.uniform(3, 5, n).round(2),
    })
    out = os.path.join(RAW_DIR, "suppliers.csv")
    df.to_csv(out, index=False)
    print(f"[OK] 生成 suppliers.csv -> {out}")
    return df

# ----------------- 生成采购订单 -----------------
def generate_purchase_orders(products_df, suppliers_df, n=5000):
    df = pd.DataFrame({
        "purchase_order_id": range(1, n + 1),
        "product_id": np.random.choice(products_df["product_id"], n),
        "supplier_id": np.random.choice(suppliers_df["supplier_id"], n),
        "quantity": np.random.randint(1, 500, n),
        "lead_time_days": np.random.randint(1, 40, n),
        "purchase_order_date": pd.date_range("2023-01-01", periods=n, freq="H")
    })
    out = os.path.join(RAW_DIR, "purchase_orders.csv")
    df.to_csv(out, index=False)
    print(f"[OK] 生成 purchase_orders.csv -> {out}")
    return df

# ----------------- 生成库存 -----------------
def generate_inventory(products_df, n_warehouses=5):
    records = []
    inventory_id = 1
    for pid in products_df["product_id"]:
        for wid in range(1, n_warehouses + 1):
            records.append({
                "inventory_id": inventory_id,
                "product_id": pid,
                "quantity": np.random.randint(0, 1000),
                "warehouse_location": f"WH{wid}",
                "last_updated": pd.Timestamp("2023-12-01") - pd.to_timedelta(np.random.randint(0, 30), unit='d')
            })
            inventory_id += 1
    df = pd.DataFrame(records)
    out = os.path.join(RAW_DIR, "inventory.csv")
    df.to_csv(out, index=False)
    print(f"[OK] 生成 inventory.csv -> {out}")
    return df

# ----------------- 生成入库记录 -----------------
def generate_inbound_records(purchase_orders_df):
    records = []
    inbound_id = 1
    for _, row in purchase_orders_df.iterrows():
        received_qty = np.random.randint(int(row["quantity"]*0.8), row["quantity"]+1)
        received_date = row["purchase_order_date"] + pd.to_timedelta(row["lead_time_days"], unit='d')
        records.append({
            "inbound_id": inbound_id,
            "purchase_order_id": row["purchase_order_id"],
            "product_id": row["product_id"],
            "quantity_received": received_qty,
            "received_date": received_date
        })
        inbound_id += 1
    df = pd.DataFrame(records)
    out = os.path.join(RAW_DIR, "inbound_records.csv")
    df.to_csv(out, index=False)
    print(f"[OK] 生成 inbound_records.csv -> {out}")
    return df

# ----------------- 生成销售订单 -----------------
def generate_sales_orders(products_df, n=3000):
    statuses = ["Pending", "Shipped", "Delivered", "Cancelled"]
    records = []
    for sales_order_id in range(1, n + 1):
        pid = np.random.choice(products_df["product_id"])
        quantity_sold = np.random.randint(1, 100)
        sales_order_date = pd.Timestamp("2023-01-01") + pd.to_timedelta(np.random.randint(0, 365), unit='d')
        customer_name = f"Customer {np.random.randint(1, 500)}"
        status = np.random.choice(statuses)
        records.append({
            "sales_order_id": sales_order_id,
            "product_id": pid,
            "quantity_sold": quantity_sold,
            "sales_order_date": sales_order_date,
            "customer_name": customer_name,
            "status": status
        })
    df = pd.DataFrame(records)
    out = os.path.join(RAW_DIR, "sales_orders.csv")
    df.to_csv(out, index=False)
    print(f"[OK] 生成 sales_orders.csv -> {out}")
    return df

if __name__ == "__main__":
    print("=== 开始生成 Mock 数据 ===")
    ensure_dirs()
    products_df = generate_products()
    suppliers_df = generate_suppliers()
    purchase_orders_df = generate_purchase_orders(products_df, suppliers_df)
    inventory_df = generate_inventory(products_df)
    inbound_records_df = generate_inbound_records(purchase_orders_df)
    sales_orders_df = generate_sales_orders(products_df)
    print("=== Mock 数据生成完毕 ===")
