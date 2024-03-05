# utils/retry.py
import time
from logger import get_logger

logger = get_logger(__name__)

def retry(func, max_retries=3, delay=2, exceptions=(Exception,)):
    """Повторяет попытку выполнения функции до достижения максимального количества попыток."""
    for attempt in range(max_retries):
        try:
            return func()
        except exceptions as e:
            logger.error(f"Attempt {attempt + 1} failed with error: {e}")
            time.sleep(delay)
    raise RuntimeError("Maximum retry attempts reached")
