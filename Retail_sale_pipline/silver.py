from pyspark import pipelines as dp
from pyspark.sql.functions import (
    col, trim, to_date, split, when
)

@dp.table
def sales_silver():


    # STEP 1: Read data from Bronze layer
    
    df = spark.read.table("company_data.bronze.sales_bronze")


    # STEP 2: Basic Cleaning


    # Remove leading/trailing spaces in string columns
    df = df.select(
        [trim(col(c)).alias(c) if dict(df.dtypes)[c] == "string" else col(c)
         for c in df.columns]
    )

    # Remove duplicate rows
    df = df.dropDuplicates()

    
    # STEP 3: Handle Data Types (Type Casting)
  

    # Convert Sale_Date to proper DATE format
    df = df.withColumn("Sale_Date", to_date(col("Sale_Date"), "MM-dd-yy"))

    # Convert numeric columns to proper types
    df = df.withColumn("Sales_Amount", col("Sales_Amount").cast("double")) \
           .withColumn("Quantity_Sold", col("Quantity_Sold").cast("int")) \
           .withColumn("Unit_Cost", col("Unit_Cost").cast("double")) \
           .withColumn("Unit_Price", col("Unit_Price").cast("double")) \
           .withColumn("Discount", col("Discount").cast("double"))

    # STEP 4: Feature Engineering (Useful for analytics)
   

    # Extract Region and Sales Rep from combined column
    df = df.withColumn("Region_Rep_Split", split(col("Region_and_Sales_Rep"), "-")) \
           .withColumn("Region_New", col("Region_Rep_Split")[0]) \
           .withColumn("Sales_Rep_New", col("Region_Rep_Split")[1]) \
           .drop("Region_Rep_Split")

    # Calculate Revenue (business metric)
    df = df.withColumn(
        "Revenue",
        col("Unit_Price") * col("Quantity_Sold") - col("Discount")
    )

    # STEP 5: Handle Missing Values


    df = df.fillna({
        "Sales_Amount": 0,
        "Quantity_Sold": 0,
        "Discount": 0
    })


    # STEP 6: Final Clean Selection (Silver Schema)


    silver_df = df.select(
        "Product_ID",
        "Sale_Date",
        "Sales_Rep",
        "Region_New",
        "Sales_Rep_New",
        "Sales_Amount",
        "Quantity_Sold",
        "Product_Category",
        "Unit_Cost",
        "Unit_Price",
        "Customer_Type",
        "Discount",
        "Payment_Method",
        "Sales_Channel",
        "Revenue"
    )

    # Return cleaned Silver table
    return silver_df