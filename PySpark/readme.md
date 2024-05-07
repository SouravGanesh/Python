# PySpark FAQs

This README provides answers to frequently asked questions about PySpark.

1. **How to read CSV file in PySpark?**
   
   - **Answer:** You can read a CSV file in PySpark using the `spark.read.csv()` method. Here's an example:
   
     ```python
     df = spark.read.csv("path/to/your/file.csv", header=True, inferSchema=True)
     ```

2. **How to Rename columns in DataFrame using PySpark?**

   - **Answer:** To rename columns in a DataFrame using PySpark, you can use the `withColumnRenamed()` method. Example:
   
     ```python
     df = df.withColumnRenamed("old_column_name", "new_column_name")
     ```

3. **How to ADD New Columns in DataFrame using PySpark?**

   - **Answer:** You can add new columns to a DataFrame using the `withColumn()` method. Example:
   
     ```python
     from pyspark.sql.functions import lit
     df = df.withColumn("new_column", lit(0))
     ```

4. **How to filter a DataFrame using PySpark?**

   - **Answer:** To filter a DataFrame in PySpark, you can use the `filter()` method or directly use boolean conditions within `df.select()`. Example:

     ```python
     filtered_df = df.filter(df["column"] > 5)
     ```

5. **How to Sort a DataFrame in PySpark?**

   - **Answer:** You can sort a DataFrame in PySpark using the `orderBy()` method. Example:
   
     ```python
     sorted_df = df.orderBy("column_name")
     ```

6. **How to remove Duplicates in DataFrame using PySpark?**

   - **Answer:** You can remove duplicates from a DataFrame using the `dropDuplicates()` method. Example:
   
     ```python
     df = df.dropDuplicates(["column_name"])
     ```

7. **How to use GroupBY in DataFrame using PySpark?**

   - **Answer:** To perform grouping in PySpark, you can use the `groupBy()` method. Example:
   
     ```python
     grouped_df = df.groupBy("column_name").agg({"other_column": "sum"})
     ```

8. **How to write into CSV?**

   - **Answer:** You can write a DataFrame into a CSV file using the `write.csv()` method. Example:
   
     ```python
     df.write.csv("path/to/save/file.csv", header=True)
     ```

9. **How to merge two DataFrame using PySpark?**

   - **Answer:** You can merge two DataFrames in PySpark using `join()` method. Example:
   
     ```python
     merged_df = df1.join(df2, on="common_column", how="inner")
     ```

10. **How to use WHEN Otherwise in PySpark?**

    - **Answer:** You can use `when()` and `otherwise()` functions in PySpark for conditional operations. Example:
    
      ```python
      from pyspark.sql.functions import when
      df = df.withColumn("new_column", when(df["column"] > 5, "high").otherwise("low"))
      ```

11. **How to join two DataFrames in PySpark?**

    - **Answer:** You can join two DataFrames in PySpark using the `join()` method. Example:

      ```python
      joined_df = df1.join(df2, df1["common_column"] == df2["common_column"], how="inner")
      ```

12. **How to use Window Functions in PySpark?**

    - **Answer:** Window functions in PySpark are used for performing calculations across a group of rows. Example:

      ```python
      from pyspark.sql.window import Window
      from pyspark.sql.functions import row_number

      windowSpec = Window.partitionBy("partition_column").orderBy("order_column")
      df = df.withColumn("row_number", row_number().over(windowSpec))
      ```

13. **Why to use Repartition Method in PySpark?**

    - **Answer:** The `repartition()` method in PySpark is used to increase or decrease the number of partitions in a DataFrame, which can help optimize data processing and parallelism.

14. **How to write Dataframe with Partitions using PartitionBy in PySpark?**

    - **Answer:** You can write a DataFrame with partitions using the `partitionBy()` method when writing to a file. Example:

      ```python
      df.write.partitionBy("partition_column").format("parquet").save("output/path")
      ```

15. **How to create UDF in PySpark?**

    - **Answer:** You can create User Defined Functions (UDFs) in PySpark using the `udf()` function. Example:

      ```python
      from pyspark.sql.functions import udf

      def square(x):
          return x * x

      square_udf = udf(square)

      df = df.withColumn("squared_column", square_udf(df["column"]))
      ```

16. **How to do casting of Columns in PySpark?**

    - **Answer:** You can cast columns to a specific data type in PySpark using the `cast()` method. Example:

      ```python
      df = df.withColumn("int_column", df["string_column"].cast("int"))
      ```

17. **How to handle NULLs in PySpark?**

    - **Answer:** You can handle NULL values in PySpark using functions like `fillna()` to fill NA values or `dropna()` to drop rows with NULL values.

18. **How to pivot a DataFrame in PySpark?**

    - **Answer:** You can pivot a DataFrame in PySpark using the `pivot()` method. Example:

      ```python
      pivoted_df = df.groupBy("column1").pivot("column2").agg({"agg_column": "sum"})
      ```

19. **Different types of mode while reading a file in Dataframe using PySpark?**

    - **Answer:** While reading a file in PySpark DataFrame, you can specify different modes like 'permissive', 'dropMalformed', or 'failFast' to handle corrupt records.

20. **Spark Streaming Example with PySpark Apache SPARK Structured STREAMING TUTORIAL with PySpark?**

    - **Answer:** Spark Structured Streaming is a scalable and fault-tolerant stream processing engine built on Spark SQL. Example:

      ```python
      from pyspark.sql import SparkSession

      spark = SparkSession.builder \
          .appName("StructuredNetworkWordCount") \
          .getOrCreate()

      lines = spark.readStream \
          .format("socket") \
          .option("host", "localhost") \
          .option("port", 9999) \
          .load()

      # Further processing
      ```

21. **File Spark Streaming Example Apache SPARK Structured STREAMING TUTORIAL with PySpark?**

    - **Answer:** In Spark Structured Streaming, you can read from various file formats as streaming sources. Example:

      ```python
      files = spark.readStream \
          .format("csv") \
          .option("path", "path/to/files") \
          .load()

      # Further processing
      ```

22. **Broadcast Join in PySpark?**

    - **Answer:** Broadcast join is a optimization technique in PySpark where the smaller DataFrame is broadcasted to all the worker nodes to reduce the shuffle data. Example:

      ```python
      from pyspark.sql.functions import broadcast

      joined_df = df1.join(broadcast(df2), on="common_column", how="inner")
      ```

23. **Dbutils commands in?**

    - **Answer:** Databricks provides `dbutils` commands for various utilities like file manipulation, notebook management, etc.

24. **Get Latest data from file using dbutils?**

    - **Answer:** You can use `dbutils.fs.head()` method to get the latest data from a file in Databricks.

25. **Parameterization of Notebook?**

    - **Answer:** Parameterization of notebooks in Databricks allows you to pass parameters to a notebook from another notebook or job.

26. **How to create scope in?**

    - **Answer:** In Databricks, you can create a scope to securely store and manage secrets, keys, and tokens.

27. **How to Clone,Push,Pull changes in Repo using Repos?**

    - **Answer:** You can clone, push, and pull changes in a Git repository using commands like `git clone`, `git push`, and `git pull`.

28. **Difference between TempView and GlobalTempView Azure?**

    - **Answer:** TempView is tied to a specific SparkSession, whereas GlobalTempView is tied to the Spark application lifecycle and accessible across sessions.

29. **How to use InsertInto in PySpark?**

    - **Answer:** You can use the `insertInto()` method to insert data into an existing table. Example:

      ```python
      df.write.insertInto("table_name")
      ```

30. **Difference Between Collect and Select in PySpark?**

    - **Answer:** `collect()` is an action that retrieves all data from the DataFrame and returns it to the driver, while `select()` is a transformation that selects specific columns from the DataFrame.

31. **Read Singleline and Multiline JSON in PySpark?**

    - **Answer:** You can read single-line and multi-line JSON files in PySpark using the `json()` method. Example:

      ```python
      singleline_df = spark.read.json("singleline.json")
      multiline_df = spark.read.json("multiline.json", multiLine=True)
      ```

32. **What are Success, Committed, started files in?**

    - **Answer:** In the context of Spark job monitoring, "success" files indicate successful completion, "committed" files are those that are finalized, and "started" files indicate that the job has started execution.

33. **How to Read and Write XML in?**

    - **Answer:** You can read and write XML files in PySpark using libraries like `spark-xml`. Example:

      ```python
      df.write.format("com.databricks.spark.xml").option("rootTag", "root").option("rowTag", "record").save("records.xml")
      ```

34. **How to fill NA, NULL in dataframe using PySpark in?**

    - **Answer:** You can fill NA or NULL values in a DataFrame using the `fillna()` method. Example:

      ```python
      df.fillna(0)
      ```

35. **How to use Map Transformation in PySpark using?**

    - **Answer:** You can use the `map()` transformation in PySpark to apply a function to each element of an RDD. Example:

      ```python
      rdd.map(lambda x: x * 2)
      ```

36. **What is Cache and Persist in PySpark And Spark-SQL using?**

    - **Answer:** `cache()` and `persist()` are used to persist RDDs or DataFrames in memory to speed up subsequent operations.

37. **How to connect Blob Storage using SAS token using?**

    - **Answer:** You can connect to Blob Storage using a Shared Access Signature (SAS) token in PySpark using the Azure Blob Storage connector. Example:

      ```python
      df = spark.read.format("csv").option("header", "true").load("wasbs://container@storage.blob.core.windows.net/path/to/file.csv?SAS_TOKEN")
      ```

38. **How to create Mount Point and connect Blob Storage using Access Keys?**

    - **Answer:** You can create a mount point in Databricks and connect Blob Storage using account access keys. Example:

      ```python
      dbutils.fs.mount(source="wasbs://<container-name>@<storage-account-name>.blob.core.windows.net/", mount_point="/mnt/<mount-name>", extra_configs={"<conf-key>":dbutils.secrets.get(scope="<scope-name>", key="<key-name>")})
      ```
