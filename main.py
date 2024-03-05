import json
from multiprocessing import Pool
import database.redis_client as redis_client
import api.pastebin as pastebin
import database.clickhouse_client as clickhouse
from utils.retry import retry
from logger import get_logger

logger = get_logger(__name__)

def process_data(data):
    """Обработка полученных данных."""
    ipv4 = data['ipv4']
    mac = data['mac']
    
    try:
        # Обработка данных
        clickhouse_client = clickhouse.get_clickhouse_client()

        result = clickhouse_client.query("SELECT username FROM search_service.user_data WHERE ipv4 = %s AND mac = %s LIMIT 1", [ipv4, mac])
        result_data = result.result_rows
        username = result_data[0][0]
        database_entry = {'username': username, 'ipv4': ipv4, 'mac': mac}
        print(f"Найдено совпадение, публекуем: {database_entry}")

        # Ведем лог
        logger.info(f"Query result: {result_data}")
  
        # Публикация результата на Pastebin
        pastebin_response = pastebin.create_pastebin(json.dumps(database_entry))
        logger.info(f"Pastebin URL: {pastebin_response}")

    except Exception as e:
        logger.error(f"Error processing data: {e}")

def listen_redis_queue():
    """Прослушивание очереди Redis и обработка данных."""
    client = redis_client.get_redis_client()
    while True:
        message = client.blpop('search_queue')
        data = json.loads(message[1])
        logger.info(f"Received data: {data}")
        print(f"что то нашли: {data}... \n")
        process_data(data)

if __name__ == '__main__':
    try:
        with Pool(1) as pool:  
        # Во время тестирования используется один рабочий процесс, для недежности
            pool.apply_async(listen_redis_queue)
            pool.close()
            pool.join()
    except KeyboardInterrupt:
        logger.info("Process stopped by the user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
