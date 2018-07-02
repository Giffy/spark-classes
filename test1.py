from pyspark.sql import SparkSession

spark = SparkSession.builder \
          .master("local") \
          .appName("Hello World!") \
          .getOrCreate()

df = spark.read.option("header","true").csv("data/titanic_dataset.csv")
df.show()
