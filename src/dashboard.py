import os
import pickle
import plotly.express as px
import plotly.graph_objects as go

PROJECT_ROOT = r'D:\Supply-Chain-Efficiency-Analytics'
DASHBOARD_DIR = os.path.join(PROJECT_ROOT,'dashboards')
os.makedirs(DASHBOARD_DIR,exist_ok=True)
OUTPUT_FILE = os.path.join(DASHBOARD_DIR,'efficiency_dashboard.html')

# 读取 Pickle
with open(os.path.join(DASHBOARD_DIR,'eda_results.pkl'),'rb') as f:
    eda_results = pickle.load(f)
with open(os.path.join(DASHBOARD_DIR,'modeling_results.pkl'),'rb') as f:
    modeling_results = pickle.load(f)

# KPI 示例
inventory_turnover = 10
stock_alert_products = eda_results['stock_alert_products']
stockout_rate = len(stock_alert_products)/200
avg_lead_time = 12
fulfillment_rate = 0.92
on_time_rate = eda_results['supplier_delivery_rate']['on_time'].mean()

# KPI HTML
kpi_html = f"""
<div style="display:flex; justify-content:space-around; margin-bottom:20px;">
    <div style="padding:20px; background-color:{'lightgreen' if inventory_turnover>5 else 'lightcoral'}; border-radius:10px;">
        <h3>库存周转率</h3><p>{inventory_turnover:.2f}</p>
    </div>
    <div style="padding:20px; background-color:{'lightgreen' if stockout_rate<0.1 else 'lightcoral'}; border-radius:10px;">
        <h3>缺货率</h3><p>{stockout_rate:.2%}</p>
    </div>
    <div style="padding:20px; background-color:{'lightgreen' if avg_lead_time<15 else 'lightcoral'}; border-radius:10px;">
        <h3>平均采购提前期</h3><p>{avg_lead_time:.1f} 天</p>
    </div>
    <div style="padding:20px; background-color:{'lightgreen' if fulfillment_rate>0.9 else 'lightcoral'}; border-radius:10px;">
        <h3>订单履约率</h3><p>{fulfillment_rate:.2%}</p>
    </div>
    <div style="padding:20px; background-color:{'lightgreen' if on_time_rate>0.9 else 'lightcoral'}; border-radius:10px;">
        <h3>供应商准时率</h3><p>{on_time_rate:.2%}</p>
    </div>
</div>
"""

# 图表 HTML
charts_html = ""
charts_html += eda_results['fig_sales_trend'].to_html(full_html=False, include_plotlyjs='cdn')
charts_html += eda_results['fig_stock_alert'].to_html(full_html=False, include_plotlyjs=False)
charts_html += eda_results['fig_supplier_performance'].to_html(full_html=False, include_plotlyjs=False)
charts_html += modeling_results['fig_sales_forecast'].to_html(full_html=False, include_plotlyjs=False)
charts_html += eda_results['funnel_fig'].to_html(full_html=False, include_plotlyjs=False)
charts_html += eda_results['fig_sku_heatmap'].to_html(full_html=False, include_plotlyjs=False)

# 输出 HTML
html_content = f"""
<html>
<head>
    <title>供应链效率 Dashboard</title>
</head>
<body>
    <h1 style="text-align:center;">供应链效率 Dashboard</h1>
    {kpi_html}
    {charts_html}
</body>
</html>
"""

with open(OUTPUT_FILE,'w',encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] 完整 Dashboard 已生成：{OUTPUT_FILE}")
