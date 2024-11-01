# Standard Library
import logging
import time


class LogTimeMessageMixin:
    logger = logging.getLogger("execution_time")

    def __init__(self, start_time=None, logging_level="info"):
        self.start_time = start_time or time.time()
        self.logging_level = logging_level
        super().__init__()

    def log_message(self, message, logging_level=None):
        logging_level = logging_level or self.logging_level
        current_time = time.time() - self.start_time
        current_time_seconds = int(current_time)
        getattr(self.logger, logging_level)(
            f"[{current_time_seconds} seconds] {message}"
        )
