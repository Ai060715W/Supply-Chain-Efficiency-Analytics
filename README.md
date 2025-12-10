# Supply Chain Efficiency Analytics

端到端供应链效率分析系统  
包含 Python + SQL + Dashboard，全流程可复现。

## Features
- 模拟供应链数据（5000+ 行）
- 数据清洗
- SQLite 数据库 ETL
- SQL 指标分析
- Plotly Dashboard 可视化

## Quick Start
```bash
python src/generate_mock_data.py
python src/data_cleaning.py
python src/etl_pipeline.py
python src/dashboard.py

技术栈
Python / Pandas / SQLite / Plotly

---

Supply-Chain-Efficiency-Analytics
├── data
│   ├── raw/
│   └── processed/
├── dashboards/
│   └── efficiency_dashboard.html        # 运行 dashboard.py 新生成
├── notebooks/
│   ├── EDA.ipynb
│   └── Modeling.ipynb
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
├── src/
│   ├── generate_mock_data.py
│   ├── data_cleaning.py
│   ├── etl_pipeline.py
│   ├── efficiency_metrics.py
│   └── dashboard.py
├── supply_chain.db                     
├── requirements.txt
└── README.md
