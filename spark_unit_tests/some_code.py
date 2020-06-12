
import pyspark.sql.functions as f


def transformation(spark_df):
    """
    Function that does data transformations in spark.
    :param spark_df: A Spark DataFrame with columns 'col1', and 'col2'
    :return: spark_df filtered to where col2 >= 200
    """
    return spark_df.filter(f.col('col2') >= 200)
