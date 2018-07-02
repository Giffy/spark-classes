from pyspark.sql import SparkSession

spark = SparkSession.builder \
          .master("local") \
          .appName("Hello World!") \
          .getOrCreate()

df = spark.read.option("header","true").option("sep",";").csv("data/metarCloudInformation_Facts.csv")
df.show()
