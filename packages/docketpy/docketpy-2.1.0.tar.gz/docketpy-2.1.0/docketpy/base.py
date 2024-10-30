import os
import time
import logging
import subprocess
import platform, socket, sys
import pickle
from enum import Enum

from datetime import datetime
from uuid import uuid4
from abc import ABC, abstractmethod

import redis

from docketpy.gcs import save_logs_to_bucket_from_redis
from docketpy.config import LOGS_BUCKET, REDIS_HOST, REDIS_PORT

# Initialize Redis client
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
try:
    redis_client.rpush('docket-log', f"{datetime.now()}: Connected to Redis at {REDIS_HOST}:{REDIS_PORT} from {socket.gethostname()}!") 
    redis_client.rpush('docket-log', f"{datetime.now()}: Docketpy Initializing from {socket.gethostname()}!")
except Exception as e:
    print(f"Failed to initialize Redis client: {e}")
    sys.exit(1)


# Initialize Redis logger
class RedisHandler(logging.Handler):
    def __init__(self, host='localhost', port=6379, key='app-logs'):
        logging.Handler.__init__(self)
        self.client = redis.Redis(host=host, port=port)
        self.key = key

    def emit(self, record):
        try:
            log_entry = self.format(record)
            self.client.rpush(self.key, log_entry)
            # print(f"RedisHandler: {self.key} {log_entry}")
        except Exception as e:
            print(f"An exception in RedisHandler: {str(e)}")


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, level):
       self.logger = logger
       self.level = level
       self.linebuf = ''
       self._in_write = False
    
    def write(self, message):
        # Avoid empty messages and recursion
        if not self._in_write and message.strip():  
            self._in_write = True
            try:
                self.logger.log(self.level, message.strip())
            finally:
                self._in_write = False

    def flush(self):
        pass


# Function to configure the Redis logger
def configure_redis_logger(name='redis_logger', host='localhost', port=6379, key='app-logs'):
    logger = logging.getLogger(name)
    redis_handler = RedisHandler(host=host, port=port, key=key)
    redis_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(redis_handler)
    logger.setLevel(logging.DEBUG)
    return logger


def close_logger(logger):
    """Close all handlers of the logger."""
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)


class TaskStatus(Enum):
    ERRORED = 0
    INITIATED = 10
    STARTED = 20
    RUNNING = 30
    WAITING = 40
    COMPLETED = 50


class BaseTask(ABC):
    def __init__(self):
        self.task_id = str(uuid4()).split('-')[-1]
        self.redis_logger_key = f"app-logs-{self.task_id}"
        self.task_status = TaskStatus.INITIATED
        self.redis_logger = configure_redis_logger(
            name=f"redis_logger-{self.task_id}", 
            host=REDIS_HOST, 
            port=REDIS_PORT, 
            key=self.redis_logger_key
            )

    def get_task_id(self):
        return self.task_id

    def set_status(self, status):
        self.task_status = status
    
    def log_platform_info(self):
        self.redis_logger.info(f"Running {self.__class__.__name__}")
        self.redis_logger.info(f"Platform: {platform.platform()}")
        self.redis_logger.info(f"Hostname: {socket.gethostname()}")
        self.redis_logger.info(f"IP: {socket.gethostbyname(socket.gethostname())}")
        self.redis_logger.info(f"Python: {platform.python_version()}")
        
    def close_and_save_logs(self):
        close_logger(self.redis_logger)
        save_logs_to_bucket_from_redis(REDIS_HOST, REDIS_PORT, self.redis_logger_key, LOGS_BUCKET, self.redis_logger_key)

    @abstractmethod
    def run(self):
        pass
        

if __name__ == "__main__":
    print("base.py")
    
    