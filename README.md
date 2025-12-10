端到端供应链效率分析系统  
---

## 项目介绍
本项目旨在分析供应链效率，提供从数据生成、清洗、存储到可视化的完整解决方案。通过模拟供应链数据，结合 SQL 分析和 Plotly Dashboard，可快速生成可视化报告，帮助用户优化供应链管理。

## Features
- **数据生成**：模拟供应链数据
- **数据清洗**：处理原始数据，生成分析所需的结构化数据
- **ETL 管道**：将清洗后的数据加载到 SQLite 数据库
- **SQL 分析**：通过 SQL 查询计算供应链效率指标
- **可视化**：使用 Plotly 构建交互式 Dashboard

## 技术栈
- **编程语言**：Python
- **数据处理**：Pandas
- **数据库**：SQLite
- **可视化**：Plotly

## 项目结构
```
Supply-Chain-Efficiency-Analytics/
├── dashboards/
│   ├── eda_results.pkl
│   ├── efficiency_dashboard.html
│   └── modeling_results.pkl
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
│   ├── analysis_queries.sql
│   └── schema.sql
├── src/
│   ├── dashboard.py
│   ├── efficiency_metrics.py
│   ├── etl_pipeline.py
│   └── generate_mock_data.py
├── supply_chain.db
└── README.md
```

## 配置环境
1. **克隆项目**
   ```bash
   git clone https://github.com/Ai060715W/Supply-Chain-Efficiency-Analytics.git
   cd Supply-Chain-Efficiency-Analytics
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 使用 venv\Scripts\activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start
运行以下命令以生成数据并启动 Dashboard：

```bash
python src/generate_mock_data.py
python src/etl_pipeline.py
python src/dashboard.py
```

## 示例输出
运行完上述命令后，交互式 Dashboard 将生成在 `dashboards/efficiency_dashboard.html` 文件中。使用浏览器打开即可查看供应链效率分析结果。

## 贡献指南
欢迎贡献代码！请参考以下步骤：
1. Fork 本仓库
2. 创建新分支：`git checkout -b feature-branch`
3. 提交更改：`git commit -m "Add new feature"`
4. 推送分支：`git push origin feature-branch`
5. 创建 Pull Request

## 联系方式
如有任何问题，请联系 [Ai060715W](https://github.com/Ai060715W)。