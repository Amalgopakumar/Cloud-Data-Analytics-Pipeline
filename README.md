# 📊 Cloud Data Analytics Pipeline using Databricks & Power BI

An end-to-end **Cloud Data Analytics Pipeline** built using **Databricks, Delta Lake, PySpark, SQL, Power BI, and Databricks Genie**. This project demonstrates a modern **Medallion Architecture (Bronze, Silver & Gold)** for data ingestion, cleaning, transformation, and business intelligence reporting.

---

## 📌 Project Overview

The objective of this project was to simulate a real-world cloud analytics workflow by building an ETL pipeline that transforms raw retail transaction data into analytics-ready datasets for reporting.

> **Note:** The primary focus of this project was understanding **data pipeline architecture, ETL processing, Delta Lake, and PySpark-based data cleaning** rather than working with a very large dataset.

---

## 🛠️ Tech Stack

- Python
- PySpark
- SQL
- Databricks
- Delta Lake
- Medallion Architecture (Bronze, Silver & Gold)
- Power BI
- DAX
- Databricks Genie

---

## 🏗️ Architecture

```text
Raw Transaction Data
        │
        ▼
Bronze Layer
(Raw Data Ingestion)
        │
        ▼
Silver Layer
(Data Cleaning & Validation)
        │
        ▼
Gold Layer
(Business Ready Tables)
        │
        ▼
Power BI Dashboard
```

---

## 🥉 Bronze Layer

- Raw transaction data ingestion
- Initial schema validation
- Data stored in Delta format
- No business transformations

---

## 🥈 Silver Layer

- Missing value handling
- Duplicate removal
- Data type corrections
- Standardized column formats
- Data quality validation
- Business rule implementation

---

## 🥇 Gold Layer

- Analytics-ready dataset
- Business aggregations
- Optimized for reporting
- Connected directly to Power BI

---

## 📊 Dashboard Features

### Executive Overview

- Total Revenue KPI
- Total Quantity Sold
- Best Performing Category
- Revenue Trend Analysis
- Quantity Trend Analysis
- Store Performance
- Payment Method Distribution
- Customer Distribution by Location

### Drill-through Analysis

- Interactive Product Analysis
- Customer-Level Insights
- Store-Level Performance
- Dynamic Filtering
- Cross-Visual Interactions

### Business Insights

- Revenue Performance
- Product Performance
- Store Performance
- Customer Analysis
- Payment Behaviour
- Business Recommendations

---

## 🤖 Databricks Genie

Implemented **Databricks Genie** to explore business data using natural language queries, enabling quick analysis without writing SQL.

### Example Questions

- Which store generated the highest revenue?
- What is the best-selling product category?
- Show revenue by payment method.
- Which location has the highest customer count?

---

## 🔄 ETL Workflow

1. Load raw transaction data into the Bronze layer.
2. Clean and validate data using PySpark.
3. Transform cleaned data into the Silver layer.
4. Build business-ready Gold tables.
5. Connect the Gold layer to Power BI.
6. Create interactive dashboards using DAX.
7. Explore data using Databricks Genie.

---

## 📈 Key Learnings

- Built an end-to-end analytics pipeline using Medallion Architecture.
- Implemented ETL workflows using PySpark.
- Worked with Delta Lake tables.
- Applied SQL for analytical queries.
- Built interactive Power BI dashboards using DAX.
- Explored conversational analytics using Databricks Genie.
- Understood the complete flow from raw data ingestion to business reporting.

---

## 📂 Project Structure

```text
Cloud-Data-Analytics-Pipeline
│
├── Bronze_Notebook.py
├── Silver_Notebook.py
├── Gold_Notebook.py
├── Dataset
│   └── Retail_Transactions.csv
├── Power BI
│   └── Cloud_Analytics_Dashboard.pbix
├── Dashboard Screenshots
├── Architecture Diagram
└── README.md
```

---

## 🚀 Future Improvements

- Integrate AWS S3 for automated cloud data ingestion.
- Schedule ETL pipelines using Databricks Workflows.
- Implement incremental data loading.
- Add automated data quality checks.
- Develop real-time dashboards using DirectQuery.
- Expand business KPIs and reporting.

---

## 📸 Project Preview

### Dashboard Overview

<img width="1327" height="692" alt="image" src="https://github.com/user-attachments/assets/2f2099de-fa24-4b00-9f83-430d62207430" />

### Drill-through Analysis

<img width="1325" height="685" alt="image" src="https://github.com/user-attachments/assets/a9e81ed8-8f64-4318-80dc-ed577a2e7b6b" />

### Pipeline Architecture

<img width="1037" height="567" alt="image" src="https://github.com/user-attachments/assets/347383ef-0b79-4486-9856-6d0fb29e69db" />

<img width="1157" height="960" alt="image" src="https://github.com/user-attachments/assets/d11edd6a-8f06-46ae-83d8-d8f88d5f354d" />
<img width="1157" height="960" alt="image" src="https://github.com/user-attachments/assets/2a70a5a2-4e51-4091-a2db-f77f01ea1cae" />

---

## 👨‍💻 Author

**Amal Gopakumar**
---

⭐ If you found this project helpful, consider giving it a **Star**!
