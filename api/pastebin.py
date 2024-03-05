# api/pastebin.py
import requests
from config.settings import API_DEV_KEY, EXTERNAL_SERVICE_URL
from utils.retry import retry
from logger import get_logger

logger = get_logger(__name__)

def create_pastebin(api_paste_code, api_paste_private='0', api_paste_name='result', api_paste_expire_date='1M', api_paste_format='json', api_user_key=''):
    """Создает новый пост на Pastebin и возвращает URL поста."""
    payload = {
        'api_dev_key': API_DEV_KEY,
        'api_paste_code': api_paste_code,
        'api_paste_private': api_paste_private,
        'api_paste_name': api_paste_name,
        'api_paste_expire_date': api_paste_expire_date,
        'api_paste_format': api_paste_format,
        'api_user_key': api_user_key,
        'api_option': 'paste'
    }

    def post_request():
        response = requests.post(EXTERNAL_SERVICE_URL, data=payload)
        print(f"Код ответа: {response.status_code} \n")

        if response.status_code == 200:
            with open('url.txt', 'a') as file:
                file.write(response.text + '\n')
            print('Пост успешно создан. URL:', response.text)
            return response.text
        else:
            print('что то пошло не так\n')
            response.raise_for_status()
        
    return retry(post_request)
