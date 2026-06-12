from pyspark import pipelines as dp
from pyspark.sql.functions import sum, avg

@dp.table
def sales_gold():

    # Read data from Silver layer
    df = spark.read.table("company_data.silver.sales_silver")

    # Create business KPIs
    gold_df = df.groupBy(
        "Region_New",
        "Product_Category"
    ).agg(
        sum("Revenue").alias("Total_Revenue"),
        sum("Quantity_Sold").alias("Total_Quantity_Sold"),
        avg("Unit_Price").alias("Average_Unit_Price")
    )

    return gold_df