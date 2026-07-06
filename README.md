# 🚀 Azure End-To-End Data Engineering Project

> Welcome to the **Azure End-To-End Data Engineering Project!**

This project demonstrates the development of an end-to-end data pipeline solution, from building a data warehouse from scratch to generating a business-ready data model using Microsoft Azure tools.

The main goal was to bring all data into one system, clean it, apply business logic, and make it available for reporting and analytics.

---

## 🧩 Data Architecture

The Microsoft Azure resources utilized for this project are:

| Azure Service | Purpose |
|---------------|---------|
| 🔹 **Azure Data Factory (ADF)** | Data ingestion from source to destination. |
| ⚡ **Azure Databricks** | Data transformations using PySpark and Spark-SQL. |
| 💾 **Azure Data Lake Storage Gen2 (ADLS)** | Storing all the data. |
| 📊 **Azure Synapse Analytics** | Reporting and querying. |
| 📈 **Power BI** | Creating dashboards (Established connection between Synapse and Power BI). |

---

<img width="1536" height="1024" alt="ChatGPT Image Jul 6, 2026, 07_38_33 PM" src="https://github.com/user-attachments/assets/2c5bd568-d1a8-46db-a902-b7c78e21aaf7" />



## 🏛️ Medallion Architecture

This project follows the **Medallion Architecture** consisting of **Bronze**, **Silver**, and **Gold** layers.

```text
                 Source Data
                      │
                      ▼
        🥉 Bronze Layer (Raw Data)
                      │
                      ▼
      🥈 Silver Layer (Cleaned Data)
                      │
                      ▼
    🥇 Gold Layer (Business Model)
                      │
                      ▼
     📊 Synapse Analytics & Power BI
```

---

### 🥉 Bronze Layer

- Stored raw data as **CSV** format from the source systems.
- Data is ingested from the Git Repository to Azure Data Lake Storage Gen2 using **Azure Data Factory Dynamic Pipelines**.

---

### 🥈 Silver Layer

- Data cleansing
- Standardization
- Normalization
- Business rule implementation
- Data transformations using **PySpark** and **Spark-SQL**
- Stored transformed data in **Parquet** format under the **Silver** schema.

---

### 🥇 Gold Layer

- Created final **Fact** and **Dimension** tables.
- Built a **Star Schema** for reporting and analytics.
- Stored business-ready data under the **Gold** schema for BI and Data Science teams.

---

## ⭐ Business Impact

This project helped business leaders to:

- 📈 Track product performance across different regions.
- 💰 Monitor pricing trends.
- 📊 Generate business-ready dashboards.
- 🤖 Enable analysts and data scientists to build ML models using clean and reliable data.

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Cloud Platform | Microsoft Azure |
| Data Ingestion | Azure Data Factory |
| Data Storage | Azure Data Lake Storage Gen2 |
| Data Processing | Azure Databricks |
| Data Transformation | PySpark, Spark-SQL |
| Data Format | Parquet, Delta Lake |
| Data Warehouse | Azure Synapse Analytics |
| Data Visualization | Power BI |

---

## 📌 Architecture Flow

```text
Git Repository
      │
      ▼
Azure Data Factory
      │
      ▼
Azure Data Lake Storage Gen2
      │
      ▼
Azure Databricks
      │
      ▼
Bronze ➜ Silver ➜ Gold
      │
      ▼
Azure Synapse Analytics
      │
      ▼
Power BI Dashboard
```

---

## ✨ Key Highlights

- End-to-End Azure Data Engineering Project
- Dynamic Data Ingestion using Azure Data Factory
- Data Transformation using PySpark & Spark-SQL
- Medallion Architecture (Bronze, Silver & Gold)
- Azure Synapse Analytics Integration
- Power BI Reporting & Dashboards
