# Databricks notebook source
df = spark.table("cloud_data_analytics_pipeline.default.transactions").toPandas()
df

# COMMAND ----------

import pandas as pd
df["transaction_date"] = pd.to_datetime(df["transaction_date"], format='%Y-%m-%d')
df


# COMMAND ----------

df_Clean = df.dropna()
df_Clean["total_amount"] = df_Clean["total_amount"].astype(int)
df_Clean["quantity"] = df_Clean["quantity"].astype(int)
df_Clean["unit_price"] = df_Clean["unit_price"].astype(int)
df_Clean

# COMMAND ----------

df_Clean = df_Clean.drop_duplicates(subset=['transaction_id'], keep="first")
df_Clean

# COMMAND ----------

spark.createDataFrame(df_Clean).write.mode("overwrite").saveAsTable("cloud_data_analytics_pipeline.silver_data.transactions_clean")