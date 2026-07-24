# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
df = spark.table("cloud_data_analytics_pipeline.silver_data.transactions_clean")

# COMMAND ----------

# DBTITLE 1,1. Daily Sales Summary
from pyspark.sql.functions import col, sum, count, countDistinct, to_date

# Create Daily Sales Summary
daily_sales = df.groupBy(to_date(col("transaction_date")).alias("transaction_date")) \
    .agg(
        sum("total_amount").alias("total_revenue"),
        sum("quantity").alias("total_quantity_sold"),
        countDistinct("transaction_id").alias("number_of_transactions"),
        countDistinct("customer_id").alias("unique_customers")
    ) \
    .orderBy(col("transaction_date").desc())

display(daily_sales)

# COMMAND ----------

# DBTITLE 1,2. Product Performance
from pyspark.sql.functions import avg

# Create Product Performance
product_perf = df.groupBy("product_id", "product_name", "category") \
    .agg(
        sum("quantity").alias("total_quantity_sold"),
        sum("total_amount").alias("total_revenue"),
        avg("unit_price").alias("average_unit_price")
    ) \
    .orderBy(col("total_revenue").desc())

display(product_perf)

# COMMAND ----------

# DBTITLE 1,3. Store Performance

# Create Store Performance
store_perf = df.groupBy("store_location") \
    .agg(
        sum("total_amount").alias("total_revenue"),
        sum("quantity").alias("items_sold"),
        countDistinct("customer_id").alias("number_of_customers")
    ) \
    .orderBy(col("total_revenue").desc())

display(store_perf)

# COMMAND ----------

# DBTITLE 1,4. Category Performance

# Create Category Performance
category_perf = df.groupBy("category") \
    .agg(
        sum("total_amount").alias("revenue"),
        sum("quantity").alias("quantity_sold")
    ) \
    .orderBy(col("revenue").desc())

display(category_perf)

# COMMAND ----------

# DBTITLE 1,5. Payment Method Analysis

# Create Payment Method Analysis
payment_analysis = df.groupBy("payment_method") \
    .agg(
        countDistinct("transaction_id").alias("total_transactions"),
        sum("total_amount").alias("total_sales")
    ) \
    .orderBy(col("total_sales").desc())

display(payment_analysis)