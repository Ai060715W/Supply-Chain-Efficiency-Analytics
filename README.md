# 📦 端到端供应链效率分析系统

**End-to-End Supply Chain Efficiency Analytics Platform**

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

* 使用 Pandas 清洗原始 CSV 数据
* 将清洗结果写入 SQLite 数据库（supply_chain.db）
* 完整 ETL 流程可复用

### 📊 **3. SQL 分析**

* 多维度供应链效率指标：

  * 库存周转率
  * 缺货率
  * 平均采购提前期
  * 订单履约率
  * 供应商准时交货率

### 📈 **4. 可视化 Dashboard（Plotly）**

* KPI 指标卡
* 库存趋势图（折线图）
* 采购提前期分布（箱线图 / 分布图）
* 订单履约漏斗（Funnel）
* SKU 积压/畅销热力图（Heatmap）
* 供应商绩效排行榜

生成的 Dashboard 会导出为：

```
dashboards/efficiency_dashboard.html
```

---

## 🛠️ 技术栈（Tech Stack）

| 模块   | 技术                        |
| ---- | ------------------------- |
| 编程语言 | Python                    |
| 数据处理 | Pandas                    |
| 数据库  | SQLite                    |
| 可视化  | Plotly（本地 JS 版本，可离线打开）    |
| 运行环境 | VS Code  |

---

## 📂 项目结构

```
Supply-Chain-Efficiency-Analytics/
├── dashboards/
│   ├── eda_results.pkl
│   ├── modeling_results.pkl
│   └── efficiency_dashboard.html
├── data/
│   └── raw/
│       ├── inbound_records.csv
│       ├── inventory.csv
│       ├── products.csv
│       ├── purchase_orders.csv
│       ├── sales_orders.csv
│       └── suppliers.csv
├── notebooks/
│   ├── EDA.ipynb
│   └── Modeling.ipynb
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
├── src/
│   ├── dashboard.py
│   ├── efficiency_metrics.py
│   ├── etl_pipeline.py
│   └── generate_mock_data.py
├── supply_chain.db
└── README.md
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
```

可直接使用浏览器打开查看最终分析效果。

---

## 📸 Dashboard 示例（截图建议你后续自己加）



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
