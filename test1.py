spark = SparkSession.builder \
          .master("local") \
          .appName("Hello World!") \
          .getOrCreate()

df = spark.read.csv("/Users/liananapalkova/Desktop/UNIVERSITY/spark-tests/data/titanic_dataset.csv")

df.show()
