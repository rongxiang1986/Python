from pyspark.sql.types import StructType,StructField,IntegerType,Row
from pyspark.sql import functions
from pyspark import SparkContext, SQLContext

sc = SparkContext()
sql_context = SQLContext(sc)

df = sql_context.createDataFrame([("Alive", 4)], ["Name", "Number"])


schema = StructType([
    StructField("Out1", IntegerType(), False),
    StructField("Out2", IntegerType(), False)])


@functions.udf(returnType=schema)
def example(n):
    return Row('Out1', 'Out2')(n + 2, n - 2)


newDF = df.withColumn("Output", example("Number"))
newDF = newDF.select("Name", "Number", "Output.*")

newDF.show(truncate=False)

