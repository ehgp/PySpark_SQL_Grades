from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
if __name__ == '__main__':
    scSpark = SparkSession \
        .builder \
        .appName("HW9P5DATA603") \
        .getOrCreate()
sc = scSpark.sparkContext
sql = SQLContext(sc)
schema = StructType([ \
    StructField("Student_ID", StringType(), True), \
    StructField("Student_Name", StringType(), True), \
    StructField("Student_Phone_Number", StringType(), True), \
    StructField("GPA", DoubleType(), True)])
df = sql.read.csv(
    "data.csv", header=False, schema=schema, multiLine=True
)
df.createOrReplaceTempView("students")
result = sql.sql("SELECT Student_ID, Student_Name, Student_Phone_Number, "
"CASE WHEN GPA > 3.6 THEN 'A' WHEN GPA < 3.6 AND GPA > 3.2 THEN 'B' WHEN GPA < 3.2 AND GPA > 2.8 THEN 'C' END "
"AS Grade FROM students")
result.show()
