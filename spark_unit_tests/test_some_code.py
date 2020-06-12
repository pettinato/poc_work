
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
import some_code


class UnitTestSpark:
    """
    Building the SparkContext is timeconsuming, so this test is a Singleton to support multiple unit tests without
    rebuilding the SparkContext.
    As an enhancement to support a _bunch_ of tests, this can be moved into a test utility.
    """
    class __UnitTestSpark:
        def __init__(self):
            from pyspark import SparkConf, SparkContext
            conf = (SparkConf().setMaster("local[2]").setAppName("pyspark-local-testing"))
            self.sc = SparkContext(conf=conf)
            self.spark = SparkSession.builder.master("local").appName("pyspark-local-testing-session").getOrCreate()

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not UnitTestSpark.instance:
            UnitTestSpark.instance = UnitTestSpark.__UnitTestSpark()
        self.sc = UnitTestSpark.instance.sc
        self.spark = UnitTestSpark.instance.spark


class TestPOC(unittest.TestCase):

    def test_1(self):
        """Just a basic test here"""
        input_df = pd.DataFrame([
            ['hello', 100],
            ['world', 200],
            ['earth', 300],
        ], columns=['col1', 'col2'])

        raw_output_df = some_code.transformation(UnitTestSpark().spark.createDataFrame(input_df))
        output_df = raw_output_df.toPandas()

        exp_df = pd.DataFrame([
            ['world', 200],
            ['earth', 300],
        ], columns=['col1', 'col2'])

        assert_frame_equal(output_df, exp_df)
