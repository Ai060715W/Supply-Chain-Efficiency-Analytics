# src/etl_pipeline.py

import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 项目根目录
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
DB_PATH = os.path.join(BASE_DIR, "supply_chain.db")


def load_csv(file_name):
    path = os.path.join(RAW_DIR, file_name)
    df = pd.read_csv(path)
    print(f"[OK] 加载 {file_name} -> {df.shape[0]} 行")
    return df


def clean_dates(df, date_columns):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df


def etl():
    # 1. 连接 SQLite
    conn = sqlite3.connect(DB_PATH)
    print(f"[OK] 连接数据库：{DB_PATH}")

    # ----------------- 读取 CSV -----------------
    products_df = load_csv("products.csv")
    suppliers_df = load_csv("suppliers.csv")
    purchase_orders_df = load_csv("purchase_orders.csv")
    inventory_df = load_csv("inventory.csv")
    inbound_records_df = load_csv("inbound_records.csv")
    sales_orders_df = load_csv("sales_orders.csv")

    # ----------------- 数据清洗 -----------------
    purchase_orders_df = clean_dates(purchase_orders_df, ["purchase_order_date"])
    inventory_df = clean_dates(inventory_df, ["last_updated"])
    inbound_records_df = clean_dates(inbound_records_df, ["received_date"])
    sales_orders_df = clean_dates(sales_orders_df, ["sales_order_date"])

    # ----------------- 写入数据库 -----------------
    # 1. 产品表
    products_df.to_sql("products", conn, if_exists="replace", index=False)
    print("[OK] 写入 products 表")

    # 2. 供应商表
    suppliers_df.to_sql("suppliers", conn, if_exists="replace", index=False)
    print("[OK] 写入 suppliers 表")

    # 3. 采购订单表
    purchase_orders_df.to_sql("purchase_orders", conn, if_exists="replace", index=False)
    print("[OK] 写入 purchase_orders 表")

    # 4. 库存表
    inventory_df.to_sql("inventory", conn, if_exists="replace", index=False)
    print("[OK] 写入 inventory 表")

    # 5. 入库记录表
    inbound_records_df.to_sql("inbound_records", conn, if_exists="replace", index=False)
    print("[OK] 写入 inbound_records 表")

    # 6. 销售订单表
    sales_orders_df.to_sql("sales_orders", conn, if_exists="replace", index=False)
    print("[OK] 写入 sales_orders 表")

    conn.close()
    print("[OK] ETL 完成，数据库已生成。")


if __name__ == "__main__":
    print("=== 开始 ETL 流程 ===")
    etl()
    print("=== ETL 流程结束 ===")
