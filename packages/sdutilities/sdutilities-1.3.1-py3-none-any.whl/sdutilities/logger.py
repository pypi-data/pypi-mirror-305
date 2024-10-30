'''
 #####
#     #  ####   ####  #   ##   #      #      #   #
#       #    # #    # #  #  #  #      #       # #
 #####  #    # #      # #    # #      #        #
      # #    # #      # ###### #      #        #
#     # #    # #    # # #    # #      #        #
 #####   ####   ####  # #    # ###### ######   #

######
#     # ###### ##### ###### #####  #    # # #    # ###### #####
#     # #        #   #      #    # ##  ## # ##   # #      #    #
#     # #####    #   #####  #    # # ## # # # #  # #####  #    #
#     # #        #   #      #####  #    # # #  # # #      #    #
#     # #        #   #      #   #  #    # # #   ## #      #    #
######  ######   #   ###### #    # #    # # #    # ###### #####
'''
import logging
import os
import time
from warnings import warn
from typing import Optional
import json

try:
    from pyspark.sql import SparkSession
except ImportError:
    raise ImportError("PySpark is not installed. Please install PySpark to proceed.")


class SDLogger:
    """
    Class used for logging in all scripts.

    Note: This class is deprecated and will be replaced by `futures.SDLogger` in future versions.
    """

    def __init__(self, log_level=None, log_file=True, file_log_level=None,
                 log_file_prefix=None, save_path: Optional[str] = None):
        """
        Initialize the SDLogger class.

        Args:
            log_level (str, optional): Logging level ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
            log_file (bool, optional): Whether to log to a file. Defaults to True.
            file_log_level (str, optional): Logging level for the file. Defaults to log_level.
            log_file_prefix (str, optional): Prefix for the log file name.
            save_path (str, optional): Path to save log files. Defaults to a path based on cluster configuration.
        """
        warn("SDLogger is deprecated and will be replaced by futures.SDLogger in future versions.", FutureWarning)

        # Determine the save path for logs
        if save_path is None:
            save_path = self._get_default_save_path()

        # Ensure the save path exists
        if log_file and not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok=True)

        # Generate the log file name
        date_str = time.strftime('%Y%m%d_%H%M%S')
        if log_file_prefix is None:
            log_file_prefix = self._get_notebook_name()
        log_filename = os.path.join(save_path, f'{log_file_prefix}_{date_str}.log')

        # Set up the logger
        self._logger = self._initialize_logger(log_level, file_log_level, log_filename, log_file)

    def _get_default_save_path(self) -> str:
        """
        Retrieve the default save path for log files based on cluster configuration.
        """
        try:  # This is the new behavior of saving logs to cluster-logs folder
            spark = SparkSession.builder.getOrCreate()
            save_path = f"/dbfs/cluster-logs/{spark.conf.get('spark.databricks.clusterUsageTags.clusterId')}"
        except Exception as e:  # this is the old behavior of saving logs hard-coded path of sd_internal/logs folder
            print(f"Failed to retrieve cluster ID: {e}")
            save_path = '/dbfs/sd_internal/logs'
            print(f"Defaulting the save logs path to {save_path}")
        return save_path

    def _get_notebook_name(self) -> str:
        """
        Retrieve the current notebook's name for use as a log file prefix.
        """
        try:
            spark = SparkSession.builder.getOrCreate()
            dbutils = self._get_dbutils(spark)
            notebook_info = json.loads(
                dbutils.notebook.entry_point.getDbutils().notebook().getContext().toJson())
            return notebook_info['extraContext']['notebook_path'].split('/')[-1]
        except Exception as e:
            print(f"Failed to retrieve notebook name: {e}")
            return "default_log"

    def _get_dbutils(self, spark):
        """
        Retrieve the Databricks DBUtils instance.

        Args:
            spark (SparkSession): The active Spark session.

        Returns:
            DBUtils: Databricks utility instance.
        """
        dbutils = None
        if spark.conf.get("spark.databricks.service.client.enabled") == "true":
            from pyspark.dbutils import DBUtils
            dbutils = DBUtils(spark)
        else:
            import IPython
            dbutils = IPython.get_ipython().user_ns["dbutils"]

        return dbutils

    def _initialize_logger(self, log_level, file_log_level, log_filename, log_file):
        """
        Initialize the logger with the specified configurations.

        Args:
            log_level (str): The logging level for the console.
            file_log_level (str): The logging level for the log file.
            log_filename (str): The name of the log file.
            log_file (bool): Whether to log to a file.

        Returns:
            Logger: Configured logger instance.
        """
        log_vals = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO,
                    'WARNING': logging.WARNING, 'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL}

        log_level = log_vals.get(log_level.upper(), logging.INFO) if log_level else logging.INFO
        file_log_level = log_vals.get(file_log_level.upper(),
                                      log_level) if file_log_level else log_level
        low_log_level = min(log_level, file_log_level)

        logger = logging.getLogger(__name__)
        logger.setLevel(low_log_level)

        if not logger.hasHandlers():
            screen_handler = logging.StreamHandler()
            screen_handler.setLevel(log_level)
            screen_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                                                          datefmt='[%Y/%m/%d-%H:%M:%S]'))
            logger.addHandler(screen_handler)

            if log_file:
                file_handler = logging.FileHandler(log_filename)
                file_handler.setLevel(file_log_level)
                file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                                            datefmt='[%Y/%m/%d-%H:%M:%S]'))
                logger.addHandler(file_handler)

        return logger

    def info(self, msg, *args, **kwargs):
        """Logs a message with level INFO on this logger."""
        self._log_message(logging.INFO, msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """Logs a message with level DEBUG on this logger."""
        self._log_message(logging.DEBUG, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """Logs a message with level WARNING on this logger."""
        self._log_message(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """Logs a message with level ERROR on this logger."""
        self._log_message(logging.ERROR, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """Logs a message with level CRITICAL on this logger."""
        self._log_message(logging.CRITICAL, msg, *args, **kwargs)

    def _log_message(self, level, msg, *args, **kwargs):
        """Helper method to log messages at the specified log level."""
        if self._logger.isEnabledFor(level):
            self._logger._log(level, msg, args, **kwargs)

    def set_log_level(self, log_level=None):
        """
        Sets the threshold level for this logger's screen messages.
        """
        log_level = self._get_log_level(log_level, default=logging.INFO)
        self._logger.setLevel(log_level)
        self._set_handler_level(0, log_level)  # Update screen handler level

    def set_file_log_level(self, file_log_level=None):
        """
        Sets the threshold level for the log file.
        """
        file_log_level = self._get_log_level(file_log_level)
        self._set_handler_level(1, file_log_level)  # Update file handler level

    def _get_log_level(self, log_level_str, default=None):
        """
        Convert log level string to logging level.
        """
        log_vals = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        return log_vals.get(log_level_str.upper(), default) if log_level_str else default

    def _set_handler_level(self, handler_index, level):
        """
        Set the log level for a specific handler.
        """
        if handler_index < len(self._logger.handlers):
            self._logger.handlers[handler_index].setLevel(level)
