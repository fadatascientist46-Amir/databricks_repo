# Retail Sales Data Engineering Pipeline with Databricks

## Project Overview

This project is a **Retail Sales Data Engineering Pipeline** built using **Databricks Lakeflow Declarative Pipelines (formerly Delta Live Tables)**.

The pipeline processes raw retail sales data through three layers:

Bronze → Silver → Gold

The goal is to clean the raw sales data and create business-ready data for reporting and analytics.



##  Architecture

```text
Sales CSV File
      │
      ▼
   BRONZE
Raw Sales Data
      │
      ▼
   SILVER
Cleaned & Transformed Data
      │
      ▼
    GOLD
Business KPIs & Aggregations


##  Technologies Used

Databricks
PySpark
Lakeflow Declarative Pipelines
Delta Tables
Python
SQL
GitHub



## Project Structure

text
retail-sales-databricks/
│
├── README.md
│
├── pipelines/
│   ├── sales_bronze.py
│   ├── sales_silver.py
│   └── sales_gold.py
│
└── data/
    └── sales_data.csv




#  Bronze Layer

The Bronze layer reads the original CSV file and stores the raw sales data.

 Main tasks

* Read CSV data
* Use the first row as column headers
* Automatically detect data types
* Store the raw data as a Bronze table

 Source


/Volumes/company_data/bronze/saledata/sales_data.csv


### Bronze Table


company_data.bronze.sales_bronze




#  Silver Layer

The Silver layer cleans and transforms the Bronze data.

### Main transformations

*Remove extra spaces
* Remove duplicate rows
* Convert date columns
* Convert numeric columns
* Handle missing values
* Split Region and Sales Representative
* Calculate Revenue
* Select the required columns

### Example

The `Region_and_Sales_Rep` column is split into:

```text
Region_New
Sales_Rep_New
```

### Revenue Calculation

```text
Revenue = Unit_Price × Quantity_Sold - Discount


### Silver Table

```text
company_data.silver.sales_silver




#  Gold Layer

The Gold layer contains business-ready data for reporting and analytics.

The data is grouped by:

```text
Region_New
Product_Category
```

### KPIs Created

#### Total Revenue

Total revenue generated.

#### Total Quantity Sold

Total number of products sold.

#### Average Unit Price

Average selling price of products.

### Gold Table

```text
company_data.gold.sales_gold
```

---

##  Example Gold Output

| Region | Product Category | Total Revenue | Total Quantity Sold | Average Unit Price |
| ------ | ---------------- | ------------: | ------------------: | -----------------: |
| North  | Electronics      |        125000 |                 450 |             320.50 |
| South  | Furniture        |         98000 |                 310 |             275.20 |
| East   | Clothing         |         76000 |                 520 |             145.80 |

*Example values only.*

---

##  Data Flow

```text
sales_data.csv
      │
      ▼
┌──────────────┐
│    Bronze    │
│ Raw Data     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Silver    │
│ Clean Data   │
│ Transform    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     Gold     │
│ Business KPI │
└──────────────┘
       │
       ▼
 Reporting / Analytics
```

---

##  Business Questions

The Gold layer can help answer questions such as:

* Which region generates the most revenue?
* Which product category sells the most?
* What is the average product price?
* How many products are sold in each region?
* Which region and product category combination performs best?
* What is the total revenue by product category?

---

##  How to Run the Project

### Step 1: Open Databricks

Open your Databricks workspace.

### Step 2: Create the Catalog and Schemas

```text
company_data
│
├── bronze
├── silver
└── gold
```

### Step 3: Upload the CSV

Upload:

```text
sales_data.csv
```

to:

```text
/Volumes/company_data/bronze/saledata/
```

### Step 4: Create the Pipeline

Create a **Lakeflow Declarative Pipeline** in Databricks.

Add these Python files:

```text
sales_bronze.py
sales_silver.py
sales_gold.py
```

### Step 5: Run the Pipeline

The pipeline processes the data in this order:

```text
Bronze → Silver → Gold
```

### Step 6: Check the Tables

```sql
SELECT * FROM company_data.bronze.sales_bronze;

SELECT * FROM company_data.silver.sales_silver;

SELECT * FROM company_data.gold.sales_gold;
```

---

##  What I Learned

Through this project, I practiced:

* Databricks Lakeflow Declarative Pipelines
* Medallion Architecture
* Bronze, Silver and Gold layers
* PySpark DataFrame transformations
* Data cleaning
* Data type conversion
* Handling duplicate data
* Handling missing values
* Feature engineering
* Aggregations
* Business KPI creation
* Delta tables
* Data engineering pipeline design



##  Real-World Use Case

This type of pipeline can be used by a retail company to process sales data from different sources.

The pipeline first stores the raw data, then cleans and transforms it, and finally creates business-level KPIs for analytics and reporting.

---

## Author

**Farhan Aamir**

Data Engineering | PySpark | Databricks | SQL | Data Analytics

---

##  Project Goal

The main goal of this project is to demonstrate a practical **end-to-end data engineering workflow using Databricks and PySpark**, following the **Bronze → Silver → Gold Medallion Architecture**.


