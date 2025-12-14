# 📦 End-to-End Supply Chain Efficiency Analytics Platform

**端到端供应链效率分析系统**

---

## 📘 项目简介

本项目构建了一个完整的 **供应链效率分析系统**，涵盖从数据生成、ETL、数据库、SQL 分析到交互式可视化 Dashboard 的端到端流程。

通过模拟真实供应链数据（采购 → 入库 → 库存 → 销售 → 供应商绩效），本系统能够帮助企业快速定位效率瓶颈，并提供数据驱动的决策支持。

---

## 🚀 功能特点（Features）

### ✅ **1. 数据生成**

* 自动生成高质量模拟供应链数据（产品、供应商、库存、采购、入库、销售）
* 可调整规模用于测试或建模

### 🔧 **2. 数据清洗 & ETL**

* 将结果写入 SQLite 数据库（supply_chain.db）
* 完整 ETL 流程可复用

### 📊 **3. SQL 分析**

* 多维度供应链效率指标与分析：
  
  * 产品采购与销售数量统计
  * 库存余量与分布情况
  * 产品入库及时率分析
  * 库存不足报警（低于安全库存的产品）
  * 供应商绩效评估（评分、采购数量）
  * 库存周转率计算
  * 仓库库存占用率分析
  * 供应商交货及时率统计

### 📈 **4. 可视化 Dashboard（Plotly）**

* **KPI 概览面板**：SKU总数、正常SKU、积压SKU、严重积压SKU、异常率等指标卡片
* **库存热力图扫描**：全SKU月度库存天数热力图，直观展示库存健康状况
* **积压原因分析**：异常SKU积压原因分布饼图、各品类库存健康度对比柱状图
* **单品深度分析**：异常SKU的详细分析图表，包括库存趋势与销售对比
* **品类对比分析**：同类目异常SKU的对比分析
* **优化建议清单**：所有异常SKU的落地优化建议表格

生成的 Dashboard 会导出为：

```
dashboards/supply_chain_dashboard.html
dashboards/styles.css
```

---

## 🛠️ 技术栈（Tech Stack）

| 模块   | 技术                        |
| ---- | ------------------------- |
| 编程语言 | Python                    |
| 数据处理 | Pandas、NumPy             |
| 数据库  | SQLite                    |
| 数据查询 | SQL                       |
| 可视化  | Plotly                    |
| 日期处理 | python-dateutil           |
| 前端展示 | HTML5、CSS3   |
| 数据分析 | Jupyter Notebook（.ipynb）|

---

## 📂 项目结构

```
Supply-Chain-Efficiency-Analytics/
├── dashboards/
│ ├── inventory_analysis_results.pkl
│ ├── modeling_results.pkl
│ ├── style.css
│ └── supply_chain_dashboard.html
├── data/
│ └── raw/
│ ├── inbound_records.csv
│ ├── inventory.csv
│ ├── products.csv
│ ├── purchase_orders.csv
│ ├── sales_orders.csv
│ └── suppliers.csv
├── notebooks/
│ ├── EDA.ipynb
│ └── Modeling.ipynb
├── sql/
│ ├── analysis_queries.sql
│ └── schema.sql
├── src/
│ ├── dashboard.py
│ ├── etl_pipeline.py
│ └── generate_mock_data.py
├── README.md
├── requirements.txt
└── supply_chain.db
```

---

## ⚙️ 环境配置

### 1️⃣ 克隆项目

```bash
git clone https://github.com/Ai060715W/Supply-Chain-Efficiency-Analytics.git
cd Supply-Chain-Efficiency-Analytics
```

### 2️⃣ 创建虚拟环境

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# MacOS/Linux:
source venv/bin/activate
```

### 3️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

---

## 🚀 快速开始（Quick Start）

运行完整端到端流程（生成数据 → ETL → Dashboard）：

```bash
python src/generate_mock_data.py
python src/etl_pipeline.py
python src/dashboard.py
```

生成可交互 Dashboard：

```
dashboards/efficiency_dashboard.html
dashboards/style.css
```

可直接使用浏览器打开查看最终分析效果。

---

## 📸 Dashboard 示例

<img width="1911" height="706" alt="image" src="https://github.com/user-attachments/assets/7f93361f-f884-4f1a-a72b-dd4f2edf0898" />
<img width="1357" height="741" alt="image" src="https://github.com/user-attachments/assets/d64df813-f511-44f4-be0f-b4884efd618e" />
<img width="1354" height="720" alt="image" src="https://github.com/user-attachments/assets/9a808b7f-2b0b-4f42-b0c0-50c510c99724" />
<img width="1356" height="937" alt="image" src="https://github.com/user-attachments/assets/7ce1c4c8-12d5-4f93-91dd-4b837339f37b" />
<img width="1227" height="357" alt="image" src="https://github.com/user-attachments/assets/4dc0360f-7a12-4115-821f-1e3d2ce6ad72" />

---

## 🤝 贡献指南（Contribution）

欢迎贡献代码！

1. Fork 本项目
2. 创建分支：

   ```bash
   git checkout -b feature-branch
   ```
3. 提交更改：

   ```bash
   git commit -m "Add new feature"
   ```
4. 推送分支：

   ```bash
   git push origin feature-branch
   ```
5. 创建 Pull Request

---

## 📬 联系方式

如有问题欢迎在 GitHub 提 Issue 或联系作者：
👉 [Ai060715W](https://github.com/Ai060715W)

---
