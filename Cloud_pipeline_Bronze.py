# Databricks notebook source
import pandas as pd

df = spark.table("cloud_data_analytics_pipeline.default.transactions").toPandas()
df

# COMMAND ----------

df.describe()

# COMMAND ----------

df.shape

# COMMAND ----------

df.head

# COMMAND ----------

