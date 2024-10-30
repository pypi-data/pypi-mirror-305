import logging
import functools
from typing import Callable, Any
from tqdm import tqdm
import inspect
import traceback

class SDLogger:
    def __init__(self, logger_name=__name__, log_level='INFO', use_coloredlogs=True):
        """
        Initialize the LoggerUtility class with a logger and optionally install colored logs.

        Note: This new class is intended to replace the deprecated `SDLogger` class in future versions. Additionally, usage of this class should be only in develop environment and not in production because it requires thorough review and testing before being used in production.
        
        Args:
            logger_name (str, optional): Name of the logger. Defaults to __name__.
            log_level (str, optional): Logging level. Defaults to 'INFO'.
            use_coloredlogs (bool, optional): Flag to use coloredlogs if available. Defaults to True.
        """
        self.logger = logging.getLogger(logger_name)
        if use_coloredlogs:
            try:
                import coloredlogs
                coloredlogs.install(level=log_level, logger=self.logger, fmt='%(asctime)s [%(levelname)s] %(message)s')
            except ImportError:
                self.logger.setLevel(log_level)
                self.logger.warning("coloredlogs package not available. Proceeding without colored logs.")
        else:
            self.logger.setLevel(log_level)

    def progress_decorator(self, total_steps: int) -> Callable:
        """
        Decorator to show a progress bar for the decorated function.

        Args:
            total_steps (int): Total number of steps for the progress bar.

        Returns:
            Callable: Wrapped function with a progress bar.
        """
        def decorator_progress(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper_progress(*args, **kwargs) -> Any:
                with tqdm(total=total_steps) as progress_bar:
                    def update_progress(step=1):
                        progress_bar.update(step)
                    
                    kwargs['update_progress'] = update_progress
                    result = func(*args, **kwargs)
                    progress_bar.update(total_steps - progress_bar.n)  # Ensure the progress bar completes
                    return result
            return wrapper_progress
        return decorator_progress

    def log_function_call(self, func: Callable) -> Callable:
        """
        Decorator to log the function call details and the result.

        Args:
            func (Callable): Function to be decorated.

        Returns:
            Callable: Wrapped function with logging.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            frame = inspect.currentframe()
            if frame:
                frame = frame.f_back
            if frame:
                frame = frame.f_back
            if frame:
                file_name = frame.f_code.co_filename
                line_number = frame.f_lineno
                link = f"file://{file_name}:{line_number}"
                self.logger.info(f"\033[34mCalling function '{func.__name__}' at {file_name}:{line_number} ({link}) with arguments {args} and {kwargs}\033[0m")
            result = func(*args, **kwargs)
            self.logger.info(f"\033[32mFunction '{func.__name__}' returned {result}\033[0m")
            return result
        return wrapper

    def handle_errors(self, func: Callable) -> Callable:
        """
        Decorator to handle errors in the function and log them.

        Args:
            func (Callable): Function to be decorated.

        Returns:
            Callable: Wrapped function with error handling and logging.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                frame = inspect.currentframe()
                if frame:
                    frame = frame.f_back
                if frame:
                    frame = frame.f_back
                if frame:
                    file_name = frame.f_code.co_filename
                    line_number = frame.f_lineno
                    link = f"file://{file_name}:{line_number}"
                    self.logger.error(f"\033[31mError in function '{func.__name__}' at {file_name}:{line_number} ({link}): {e}\033[0m")
                    # Log the full traceback
                    tb_str = traceback.format_exc()
                    self.logger.error(f"\033[31m{tb_str}\033[0m")
                return "An error occurred. Please try again."
        return wrapper

# Example usage:
# 3. import and initialize futures logger
# from sdutilities import futures as sdu
# import time
# logger_util = sdu.SDLogger(logger_name="test_logger", log_level="INFO", use_coloredlogs=False) # Set to False if coloredlogs is not available

# @logger_util.progress_decorator(total_steps=3)
# @logger_util.log_function_call
# @logger_util.handle_errors
# def example_function(update_progress=None):
#     for _ in range(3):
#         test_logger.info(f"Run iter: {_}")
#         time.sleep(0.1)  # Simulate work
#         if update_progress:
#             update_progress()

# example_function()