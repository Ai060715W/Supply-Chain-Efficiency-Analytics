import os
import pickle
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

PROJECT_ROOT = r'D:\Supply-Chain-Efficiency-Analytics'
DASHBOARD_DIR = os.path.join(PROJECT_ROOT, 'dashboards')
os.makedirs(DASHBOARD_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(DASHBOARD_DIR, 'supply_chain_dashboard.html')

# 模板和静态文件路径
TEMPLATE_DIR = os.path.join(PROJECT_ROOT, 'src', 'templates')
STATIC_DIR = os.path.join(PROJECT_ROOT, 'src', 'static')
TEMPLATE_FILE = os.path.join(TEMPLATE_DIR, 'dashboard_template.html')
CSS_FILE = os.path.join(DASHBOARD_DIR, 'styles.css')

# 确保模板和静态文件目录存在
os.makedirs(TEMPLATE_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

# ============================================
# 读取 EDA 分析结果
# ============================================
pkl_path = os.path.join(DASHBOARD_DIR, 'inventory_analysis_results.pkl')
if not os.path.exists(pkl_path):
    raise FileNotFoundError(f"找不到分析结果文件：{pkl_path}，请先运行 EDA.ipynb")

with open(pkl_path, 'rb') as f:
    eda_results = pickle.load(f)

# 解析结果
fig_heatmap_full = eda_results['fig_heatmap_full']
abnormal_sku_charts = eda_results['abnormal_sku_charts']
category_comparison_charts = eda_results['category_comparison_charts']
abnormal_sku_list = eda_results['abnormal_sku_list']
health_summary = eda_results['health_summary']
abnormal_analysis = eda_results['abnormal_analysis']
optimization_suggestions = eda_results['optimization_suggestions']

# ============================================
# 生成 KPI 统计
# ============================================
total_skus = len(abnormal_sku_list['sku'].unique())
abnormal_count = len(optimization_suggestions)
abnormal_rate = abnormal_count / total_skus if total_skus > 0 else 0

health_stats = health_summary.sum(numeric_only=True)
normal_count = int(health_stats.get('正常（<100天）', 0))
warning_count = int(health_stats.get('积压（100-500天）', 0))
critical_count = int(health_stats.get('严重积压（500+天）', 0))

reason_count = {}
for analysis in abnormal_analysis:
    primary_reason = analysis['reason'][0] if analysis['reason'] else '其他原因'
    reason_count[primary_reason] = reason_count.get(primary_reason, 0) + 1

# ============================================
# 生成各个图表
# ============================================

# 1. 积压原因分布饼图
fig_reason_distribution = go.Figure(data=[go.Pie(
    labels=list(reason_count.keys()),
    values=list(reason_count.values()),
    hole=0.3,
    textposition='inside',
    textinfo='label+percent'
)])
fig_reason_distribution.update_layout(
    title="异常 SKU 积压原因分布",
    height=500,
    font=dict(size=11)
)

# 2. 品类健康度对比柱状图
fig_health_by_category = go.Figure()
categories = health_summary['category'].tolist()
for status in ['正常（<100天）', '积压（100-500天）', '严重积压（500+天）']:
    if status in health_summary.columns:
        values = health_summary[status].tolist()
        fig_health_by_category.add_trace(go.Bar(
            x=categories,
            y=values,
            name=status,
            marker_color={'正常（<100天）': '#66bb6a', 
                         '积压（100-500天）': '#ffa726', 
                         '严重积压（500+天）': '#ef5350'}.get(status)
        ))

fig_health_by_category.update_layout(
    title="各品类库存健康度分布",
    xaxis_title="品类",
    yaxis_title="SKU 数量",
    barmode='stack',
    height=500,
    font=dict(size=11)
)

# ============================================
# 构建 HTML 标签页内容
# ============================================

# Tab 1: 概览面板 - KPI 卡片
overview_html = f"""
<div class="tab-content active" id="overview">
    <div class="kpi-container">
        <div class="kpi-card kpi-normal">
            <h4>异常 SKU 总数</h4>
            <p class="kpi-value">{total_skus}</p>
        </div>
        <div class="kpi-card kpi-success">
            <h4>正常 SKU</h4>
            <p class="kpi-value">{normal_count}</p>
            <span class="kpi-percent">{normal_count/total_skus*100:.1f}%</span>
        </div>
        <div class="kpi-card kpi-warning">
            <h4>积压 SKU</h4>
            <p class="kpi-value">{warning_count}</p>
            <span class="kpi-percent">{warning_count/total_skus*100:.1f}%</span>
        </div>
        <div class="kpi-card kpi-danger">
            <h4>严重积压 SKU</h4>
            <p class="kpi-value">{critical_count}</p>
            <span class="kpi-percent">{critical_count/total_skus*100:.1f}%</span>
        </div>
        <div class="kpi-card kpi-info">
            <h4>异常率</h4>
            <p class="kpi-value">{abnormal_rate:.1%}</p>
            <span class="kpi-percent">{abnormal_count}/{total_skus}</span>
        </div>
    </div>
</div>
"""

# Tab 2: 全 SKU 热力图 
heatmap_html = f"""
<div class="tab-content" id="heatmap">
    <h2>SKU 库存天数热力图（全局扫描）</h2>
    <p style="color:#666; margin-bottom:20px; font-size:13px;">
        <span style="display:inline-block; margin-right:20px;">✓ <span style="color:#1e90ff;">浅蓝</span> = 0-100天（正常库存）</span>
        <span style="display:inline-block; margin-right:20px;">✓ <span style="color:#ff8c00;">橙色</span> = 100-500天（积压）</span>
        <span style="display:inline-block;">✓ <span style="color:#dc143c;">红色</span> = 500+天（严重积压）</span>
    </p>
    <div style="overflow-x: auto; background: white; padding: 15px; border-radius: 8px;">
        {fig_heatmap_full.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
</div>
"""

# Tab 3: 分析概览 
analysis_overview_html = f"""
<div class="tab-content" id="analysis">
    <h2>积压原因分析</h2>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:30px; margin-top:20px;">
        <div style="background:white; padding:15px; border-radius:8px;">
            {fig_reason_distribution.to_html(full_html=False, include_plotlyjs=False)}
        </div>
        <div style="background:white; padding:15px; border-radius:8px;">
            {fig_health_by_category.to_html(full_html=False, include_plotlyjs=False)}
        </div>
    </div>
</div>
"""

# Tab 4: 单 SKU 分析
single_sku_html = """<div class="tab-content" id="single-sku"><h2>异常 SKU 单品深度分析</h2>"""

if abnormal_sku_charts:
    single_sku_html += """<div style="margin-top:20px;">"""
    for idx, (sku, fig) in enumerate(list(abnormal_sku_charts.items()), 1):
        single_sku_html += f"""
        <div style="margin-bottom:30px; background:white; padding:15px; border-radius:8px;">
            <h3 style="color:#764ba2; margin-bottom:15px;">分析 {idx}: {sku}</h3>
            {fig.to_html(full_html=False, include_plotlyjs=False)}
        </div>
        """
    single_sku_html += """</div>"""
else:
    single_sku_html += """<div style="padding:20px; color:#666; text-align:center;">无法生成单品分析图表，请检查数据完整性</div>"""

single_sku_html += """</div>"""

# Tab 5: 品类对比
category_comparison_html = """<div class="tab-content" id="category-compare"><h2>品类异常 SKU 对比分析</h2>"""

if category_comparison_charts:
    category_comparison_html += """<div style="margin-top:20px;">"""
    for category, fig in category_comparison_charts.items():
        category_comparison_html += f"""
        <div style="margin-bottom:30px; background:white; padding:15px; border-radius:8px;">
            <h3 style="color:#764ba2; margin-bottom:15px;">品类：{category}</h3>
            {fig.to_html(full_html=False, include_plotlyjs=False)}
        </div>
        """
    category_comparison_html += """</div>"""
else:
    category_comparison_html += """<div style="padding:20px; color:#666; text-align:center;">无法生成品类对比图表，请检查数据完整性</div>"""

category_comparison_html += """</div>"""


# Tab 6: 优化建议表格
suggestions_table_html = """<div class="tab-content" id="suggestions">
    <h2>异常 SKU 优化建议清单</h2>
    <table class="suggestions-table">
        <thead>
            <tr>
                <th>SKU</th>
                <th>产品名称</th>
                <th>品类</th>
                <th>主要原因</th>
                <th>建议动作</th>
            </tr>
        </thead>
        <tbody>
"""

for idx, item in enumerate(optimization_suggestions, 1):
    row_color = '#f9f9f9' if idx % 2 == 0 else '#ffffff'
    suggestions_text = '<br>'.join([f"• {sug}" for sug in item['suggestions']])
    suggestions_table_html += f"""
            <tr style="background-color:{row_color};">
                <td class="sku-cell"><strong>{item['sku']}</strong></td>
                <td>{item['product_name']}</td>
                <td><span class="category-badge">{item['category']}</span></td>
                <td><span class="reason-badge">{item['primary_reason']}</span></td>
                <td class="suggestion-cell">{suggestions_text}</td>
            </tr>
    """

suggestions_table_html += """
        </tbody>
    </table>
</div>
"""

def render_template(template_file, **kwargs):
    """渲染模板文件，替换占位符"""
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 替换占位符
    for key, value in kwargs.items():
        placeholder = f"{{{{{key}}}}}"
        template_content = template_content.replace(placeholder, str(value))
    
    return template_content

# 复制 CSS 文件到输出目录
static_css_path = os.path.join(STATIC_DIR, 'styles.css')
if os.path.exists(static_css_path):
    import shutil
    shutil.copy2(static_css_path, CSS_FILE)
    print(f"✅ 已复制样式表：{CSS_FILE}")
else:
    print(f"⚠️  警告：静态 CSS 文件不存在：{static_css_path}")

# 渲染 HTML
timestamp = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
html_content = render_template(
    TEMPLATE_FILE,
    overview_html=overview_html,
    heatmap_html=heatmap_html,
    analysis_overview_html=analysis_overview_html,
    single_sku_html=single_sku_html,
    category_comparison_html=category_comparison_html,
    suggestions_table_html=suggestions_table_html,
    timestamp=timestamp
)

# 保存 HTML
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ [完成] 供应链库存效率一体化 Dashboard 已生成")
print(f"\n📑 Dashboard 包含 6 个 Tab 页面：")
print(f"   1️⃣  KPI 概览 - 库存健康度统计卡片")
print(f"   2️⃣  热力图扫描 - 全 SKU 月度库存天数热力图")
print(f"   3️⃣  原因分析 - 积压原因分布 + 品类健康度对比")
print(f"   4️⃣  单品分析 - 异常 SKU 深度分析（{len(abnormal_sku_charts)} 个双轴图）")
print(f"   5️⃣  品类对比 - 同类目异常 SKU 对比分析（{len(category_comparison_charts)} 个）")
print(f"   6️⃣  优化建议 - 所有异常 SKU 的落地建议清单（{len(optimization_suggestions)} 个）")
