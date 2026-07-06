# Azure-end-to-end-data-engineering-project
Project Overview

This project demonstrates the development of a complete end-to-end data engineering solution on Microsoft Azure. It covers the entire data lifecycle—from ingesting raw data and building a modern data warehouse to creating a business-ready dimensional model for reporting and analytics.

The primary objective was to consolidate data from multiple sources into a centralized platform, perform data cleansing and transformation, apply business logic, and deliver high-quality data for business intelligence and advanced analytics.

Azure Services Used

The following Microsoft Azure services were utilized throughout the project:

Azure Data Factory (ADF): Automated data ingestion using dynamic pipelines to move data from the source repository into Azure Data Lake Storage Gen2.
Azure Data Lake Storage Gen2 (ADLS Gen2): Centralized storage for raw, transformed, and curated data.
Azure Databricks: Performed data cleansing, transformation, and enrichment using PySpark and Spark SQL.
Unity Catalog: Managed data governance, access control, and metadata across the lakehouse.
Azure Synapse Analytics: Enabled high-performance querying and served as the reporting layer.
Power BI: Connected to Azure Synapse Analytics to build interactive dashboards and business reports.
