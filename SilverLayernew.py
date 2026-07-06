# Databricks notebook source
# MAGIC %md
# MAGIC #Silver Layer Script

# COMMAND ----------

# MAGIC %md
# MAGIC ###Data Access Using App

# COMMAND ----------



spark.conf.set("fs.azure.account.auth.type.awstoragesadikdatalake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.awstoragesadikdatalake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.awstoragesadikdatalake.dfs.core.windows.net","<YOUR_AZURE_CLIENT_SECRET>")
spark.conf.set("fs.azure.account.oauth2.client.secret.awstoragesadikdatalake.dfs.core.windows.net", "<YOUR_AZURE_CLIENT_SECRET>")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.awstoragesadikdatalake.dfs.core.windows.net", "https://login.microsoftonline.com/"<YOUR_AZURE_CLIENT_SECRET>"")

# COMMAND ----------

# MAGIC %md
# MAGIC ####Reading The Data
# MAGIC

# COMMAND ----------


df_cal = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_calenders")


# COMMAND ----------

df_customer = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Customers")



# COMMAND ----------

df_Products = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/Products")

# COMMAND ----------

df_prodcat = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Product_Categories")

# COMMAND ----------

df_prodsubcat = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories")

# COMMAND ----------

df_Sales2016 = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/AdventureWork_Sales_2016")

# COMMAND ----------

df_Terret = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Territories")

# COMMAND ----------

df_ret = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("abfss://bronze@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Returns")

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

# MAGIC %md
# MAGIC #Transformations

# COMMAND ----------

# MAGIC %md
# MAGIC ###calenders

# COMMAND ----------

df_cal.display()

# COMMAND ----------

df_cal = df_cal.withColumn('Month',month(col('Date')))\
               .withColumn('Year',year(col('Date')))\
                   .withColumn('DAY',day(col('Date')))
df_cal.display()

# COMMAND ----------

df_cal.write.format("parquet").mode("append").option("path","abfss://silver@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Calendar").save()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Customers

# COMMAND ----------

df_customer.display()

# COMMAND ----------

df_customer = df_customer.withColumn('Full_Name',concat_ws(' ',col("Prefix"),col("FirstName"),col("LastName")))
df_customer.display()


# COMMAND ----------

df_customer.write.format("parquet").mode("append").option("path","abfss://silver@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Customer").save()



# COMMAND ----------

# MAGIC %md 
# MAGIC ###sub Categories

# COMMAND ----------

df_prodsubcat.display()

# COMMAND ----------

df_prodsubcat.write.format("parquet").mode("append").option("path","abfss://silver@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_ProductSubcategory").save()


# COMMAND ----------

# MAGIC %md
# MAGIC ###Products

# COMMAND ----------

df_Products.display()

# COMMAND ----------

df_Products = df_Products.withColumn("ProductSKU",split(col("ProductSKU"),"-")[0])\
                         .withColumn("ProductName",split(col("ProductName")," ")[0] )

                        

# COMMAND ----------

df_Products.display()

# COMMAND ----------

df_Products.write.format("parquet").mode("append").option("path","abfss://silver@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Products").save()



# COMMAND ----------

df_ret.write.format("parquet").mode("append").option("path","abfss://silver@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Return").save()

# COMMAND ----------

df_Terret.write.format("parquet").mode("append").option("path","abfss://silver@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Territory").save()


# COMMAND ----------

# MAGIC %md
# MAGIC ###Sales

# COMMAND ----------

df_Sales2016.display()

# COMMAND ----------

df_Sales2016 = df_Sales2016.withColumn("OrderNumber",regexp_replace(col("OrderNumber"),'S','T'))



# COMMAND ----------

df_Sales2016 = df_Sales2016.withColumn("Multiply",col("OrderLineItem")*col("TerritoryKey"))

# COMMAND ----------

df_Sales2016.display()

# COMMAND ----------

df_Sales2016= df_Sales.groupBy("OrderDate").agg(count("OrderNumber")).alias('Total_sales').display()

# COMMAND ----------

df_Sales2016.write.format("parquet").mode("append").option("path","abfss://silver@awstoragesadikdatalake.dfs.core.windows.net/AdventureWorks_Sales_2016").save()

# COMMAND ----------

