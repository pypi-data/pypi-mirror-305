# Databricks notebook source
# MAGIC %md
# MAGIC ## Table Of Contents
# MAGIC 0. check logging enabled
# MAGIC 1. import sdutilites
# MAGIC 2. initiatlize logger
# MAGIC 3. initiatize futures logger
# MAGIC

# COMMAND ----------

# 0. Check if cluster logger is enabled
print(f"Logging enabled at cluster-level: {spark.conf.get('spark.logConf')}")
print(f"ClusterID: {spark.conf.get('spark.databricks.clusterUsageTags.clusterId')}")

# COMMAND ----------


# 1. install sdutilities logger only module
%pip install "/dbfs/internal/users/data_science/dist/sdutilities_log-1.0.0-py3-none-any.whl" #--force-reinstall 
#dbutils.library.restartPython()

# COMMAND ----------

# 2. import and initialize logger
from sdutilities_log import logger as sdu

test_logger = sdu.SDLogger(log_level="INFO")

test_logger.info("logger initialized")
test_logger.info(f"logger path name: {test_logger._get_default_save_path()}\nnotebook name: {test_logger._get_notebook_name()}")
test_logger.info(f"All logs are compiled at a system location here: {test_logger._get_default_save_path()}\nUser logs are in {test_logger._get_notebook_name()}*.log")


# COMMAND ----------

# 1. install sdutilities module
!pip install "/dbfs/internal/users/data_science/dist/sdutilities-1.2.8-py3-none-any.whl" #--force-reinstall 
dbutils.library.restartPython()

# COMMAND ----------

# 2. import and initialize logger
#from sdutilities_log import logger as sdu
import sdutilities as sdu

test_logger = sdu.SDLogger(log_level="INFO")

test_logger.info("logger initialized")
test_logger.info(f"logger path name: {test_logger._get_default_save_path()}\nnotebook name: {test_logger._get_notebook_name()}")
test_logger.info(f"All logs are compiled at a system location here: {test_logger._get_default_save_path()}\nUser logs are in {test_logger._get_notebook_name()}*.log")

# COMMAND ----------


# 3. import and initialize futures logger
from sdutilities import futures as sdu
import time
logger_util = sdu.SDLogger(logger_name="test_logger", log_level="INFO", use_coloredlogs=False) # Set to False if coloredlogs is not available

@logger_util.progress_decorator(total_steps=3)
@logger_util.log_function_call
@logger_util.handle_errors
def example_function(update_progress=None):
    for _ in range(3):
        test_logger.info(f"Run iter: {_}")
        time.sleep(0.1)  # Simulate work
        if update_progress:
            update_progress()

example_function()
