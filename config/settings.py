# config/settings.py
import os

# Настройки Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# Настройки ClickHouse
CLICKHOUSE_HOST = 'localhost'
CLICKHOUSE_PORT = 8123
CLICKHOUSE_USER = 'default'
CLICKHOUSE_PASSWORD = '123'
CLICKHOUSE_DB = 'search_service'

# yAMu96g8htI5R4dDmLh6PfZmhyKRJd-Q                      
# Настройки API
API_DEV_KEY = 'yAMu96g8htI5R4dDmLh6PfZmhyKRJd-Q'
EXTERNAL_SERVICE_URL = 'https://pastebin.com/api/api_post.php'

# Настройки логирования
LOGGING_FILENAME = 'srvs.log'
LOGGING_LEVEL = 'INFO'
