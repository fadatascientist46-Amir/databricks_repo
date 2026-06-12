from pyspark import pipelines as dp

@dp.table
def sales_bronze():
    return spark.read.csv(
        "/Volumes/company_data/bronze/saledata/sales_data.csv",
        header=True,
        inferSchema=True
    )