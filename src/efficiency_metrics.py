import sqlite3
import pandas as pd

def get_avg_lead_time():
    conn = sqlite3.connect("supply_chain.db")
    df = pd.read_sql("SELECT AVG(lead_time_days) AS avg_lead_time FROM purchase_orders", conn)
    conn.close()
    return df

if __name__ == "__main__":
    print(get_avg_lead_time())
