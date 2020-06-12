
<img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="san" height="200"/>

# Complete example to run unitests locally for Spark Transformations

Install
* `pyspark`
* `pandas`
* `unittest`

# Install PySpark
Based on 
* [this post](https://medium.com/beeranddiapers/installing-apache-spark-on-mac-os-ce416007d79f)
* [and this post](https://medium.com/tinghaochen/how-to-install-pyspark-locally-94501eefe421)

Note: You don't actually have to _start_ Spark Locally in order to run unit tests.

Install Java, XCode, Scala, Spark, then set the Environment Variables.

Be sure to use Java8 _or else_ 💥🔥💥 

## Install
```bash
brew cask install homebrew/cask-versions/adoptopenjdk8
xcode-select --install
brew install scala
brew install apache-spark
```

## Set Environment Variables
Add this to `.bash_profile`

Check the versions to get the correct path.

```bash
export SPARK_HOME="/usr/local/Cellar/apache-spark/{CHECK VERSION HERE}/libexec/"
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-{CHECK VERSION HERE}-src.zip:$PYTHONPATH

# As per https://github.com/jupyter/jupyter/issues/248#issuecomment-382191665
# This is a tricky spot here, be sure to use Java8. There are a bunch of ways to get this done.
export JAVA_HOME="$(/usr/libexec/java_home -v 1.8)"
```

Be sure to restart any IDEs to pull in these new environment variables.

## Test Pyspark installation

```python
from pyspark import SparkContext
sc = SparkContext()
```

# Troubleshooting Tips

## Connection refused
If you get this error on osx `localhost: ssh: connect to host localhost port 22: Connection refused`
1. Settings
2. Sharing
3. ☑️ Remote Login

as per https://stackoverflow.com/a/22255174/2596363

## http://localhost:8080/
With the above setup, Spark isn't actually running on your laptop, so this url won't resolve.

## JAVA_HOME Tips
If you have install Java, but can't find the directory to set for `JAVA_HOME`,

Note: Inside directory `JAVA_HOME` should be directories `bin`, `bundle`, `include`, `jre`, `lib`, `man`, `release`
