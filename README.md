📊 Cloud Data Analytics Pipeline using Databricks & Power BI

An end-to-end Cloud Data Analytics project demonstrating a modern Medallion Architecture (Bronze, Silver, Gold) using Databricks Delta Lake, PySpark, SQL, Power BI, and Databricks Genie. This project focuses on building a robust data pipeline, performing data cleaning and transformation, and delivering business insights through an interactive dashboard.

📌 Project Overview

The objective of this project was to simulate a real-world analytics workflow by building an ETL pipeline that transforms raw retail transaction data into analytics-ready datasets for reporting.

Note: The primary focus of this project was understanding data pipeline architecture, ETL processing, Delta Lake, and PySpark-based data cleaning rather than working with a very large dataset.

🛠️ Tech Stack
Python
PySpark
SQL
Databricks
Delta Lake
Medallion Architecture (Bronze, Silver & Gold)
Power BI
DAX
Databricks Genie
🏗️ Architecture
📂 Medallion Architecture
🥉 Bronze Layer
Raw transaction data ingestion
Initial schema validation
Data stored in Delta format
No business transformations
🥈 Silver Layer
Missing value handling
Duplicate removal
Data type corrections
Standardized column formats
Data quality validation
Business rule implementation
🥇 Gold Layer
Analytics-ready dataset
Business aggregations
Optimized for reporting
Connected directly to Power BI
📊 Dashboard Features
Executive Overview
Total Revenue KPI
Total Quantity Sold
Best Performing Category
Revenue Trend Analysis
Quantity Trend Analysis
Store Performance
Payment Method Distribution
Customer Distribution by Location
Drill-through Analysis
Interactive Product Analysis
Customer-Level Insights
Store-Level Performance
Dynamic Filtering
Cross-Visual Interactions
Business Insights
Revenue Performance
Product Performance
Store Performance
Customer Analysis
Payment Behaviour
Business Recommendations
🤖 Databricks Genie

Implemented Databricks Genie to explore business data using natural language queries, enabling quick analysis without writing SQL for common business questions.

Example questions:

Which store generated the highest revenue?
What is the best-selling product category?
Show revenue by payment method.
Which location has the highest customer count?
🔄 ETL Workflow
Load raw transaction data into Bronze layer.
Clean and validate data using PySpark.
Transform cleaned data into the Silver layer.
Build business-ready Gold tables.
Connect Gold layer to Power BI.
Create interactive dashboards and KPIs.
Analyze data using Databricks Genie.
📈 Key Learnings
Built an end-to-end analytics pipeline using Medallion Architecture.
Implemented ETL workflows with PySpark.
Worked with Delta Lake tables.
Applied SQL for analytical queries.
Developed interactive Power BI dashboards using DAX.
Explored conversational analytics with Databricks Genie.
Understood data flow from ingestion to business reporting.
📁 Repository Structure
🚀 Future Improvements
Integrate AWS S3 for automated cloud data ingestion.
Schedule ETL pipelines using Databricks Workflows.
Implement incremental data loading.
Add automated data quality monitoring.
Create real-time dashboards using DirectQuery.
Expand business KPI coverage.

📷 Project Preview

