import time
from datetime import datetime
import telethon
from telethon.sync import TelegramClient
import schedule


ANKETA = '''
your text
'''


channel_id1 = 'channel_id'
channel_id2 = 'channel_id'
channel_id3 = 'channel_id'
channel_id4 = 'channel_id'
channel_id5 = 'channel_id'
channel_id6 = 'channel_id'
channel_id7 = 'channel_id'
channel_id8 = 'channel_id'
channel_id9 = 'channel_id'
channel_id10 = 'channel_id'
channel_id11 = 'channel_id'
channel_id12 = 'channel_id'
channel_id13 = 'channel_id'
channel_id14 = 'channel_id'
channel_id15 = 'channel_id'

# Функция для отправки сообщения в канал
def send_message(channel_id, message):
    try:
        client.send_message(channel_id, message)
        # Выводим информацию о времени отправки сообщения
        print(f'Сообщение отправлено в канал с ID {channel_id} в {datetime.now()}')
    except telethon.errors.rpcerrorlist.SlowModeWaitError as e:
        wait_time = e.seconds
        # Если возникает ошибка SlowModeWaitError, ожидаем указанное время и затем повторно отправляем сообщение
        print(f'Ожидание {wait_time} секунд перед отправкой следующего сообщения...')
        time.sleep(wait_time)
    except telethon.errors.rpcerrorlist.FloodWaitError as e:
        # Если возникает ошибка FloodWaitError, вывести сообщение и подождать указанное время плюс 1 секунду перед продолжением
        print("Flood wait error:", e)
        delay_time = e.seconds + 1  # Добавим 1 секунду для надежности
        time.sleep(delay_time)

# Константы для подключения к аккаунту Telegram
api_id = 'api_id'
api_hash = 'api_hash'
phone_number = '+phone_number'  # Номер вашего телефона в формате '+1234567890'


# Определение списка чатов и времени отправки
channel_schedule = [
{'channel_id': channel_id1, 'send_time': '00:01', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '00:02', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '00:03', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '00:04', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '00:05', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '00:06', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '00:07', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '00:08', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '00:09', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '00:10', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '00:11', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '00:12', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '00:13', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '00:14', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '00:15', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '01:02', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '01:03', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '01:04', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '01:05', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '01:06', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '01:07', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '01:08', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '01:09', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '01:10', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '01:11', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '01:12', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '01:13', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '01:14', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '01:15', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '01:16', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '02:03', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '02:04', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '02:05', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '02:06', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '02:07', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '02:08', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '02:09', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '02:10', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '02:11', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '02:12', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '02:13', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '02:14', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '02:15', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '02:16', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '02:17', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '03:04', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '03:05', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '03:06', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '03:07', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '03:08', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '03:09', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '03:10', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '03:11', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '03:12', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '03:13', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '03:14', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '03:15', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '03:16', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '03:17', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '03:18', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '04:05', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '04:06', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '04:07', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '04:08', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '04:09', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '04:10', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '04:11', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '04:12', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '04:13', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '04:14', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '04:15', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '04:16', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '04:17', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '04:18', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '04:19', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '05:06', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '05:07', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '05:08', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '05:09', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '05:10', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '05:11', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '05:12', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '05:13', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '05:14', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '05:15', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '05:16', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '05:17', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '05:18', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '05:19', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '05:20', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '06:07', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '06:08', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '06:09', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '06:10', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '06:11', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '06:12', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '06:13', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '06:14', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '06:15', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '06:16', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '06:17', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '06:18', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '06:19', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '06:20', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '06:21', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '07:08', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '07:09', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '07:10', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '07:11', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '07:12', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '07:13', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '07:14', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '07:15', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '07:16', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '07:17', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '07:18', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '07:19', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '07:20', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '07:21', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '07:22', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '08:09', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '08:10', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '08:11', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '08:12', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '08:13', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '08:14', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '08:15', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '08:16', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '08:17', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '08:18', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '08:19', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '08:20', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '08:21', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '08:22', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '08:23', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '09:10', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '09:11', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '09:12', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '09:13', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '09:14', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '09:15', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '09:16', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '09:17', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '09:18', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '09:19', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '09:20', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '09:21', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '09:22', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '09:23', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '09:24', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '10:11', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '10:12', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '10:13', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '10:14', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '10:15', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '10:16', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '10:17', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '10:18', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '10:19', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '10:20', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '10:21', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '10:22', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '10:23', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '10:24', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '10:25', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '11:12', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '11:13', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '11:14', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '11:15', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '11:16', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '11:17', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '11:18', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '11:19', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '11:20', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '11:21', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '11:22', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '11:23', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '11:24', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '11:25', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '11:26', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '12:13', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '12:14', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '12:15', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '12:16', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '12:17', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '12:18', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '12:19', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '12:20', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '12:21', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '12:22', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '12:23', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '12:24', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '12:25', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '12:26', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '12:27', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '13:14', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '13:15', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '13:16', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '13:17', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '13:18', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '13:19', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '13:20', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '13:21', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '13:22', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '13:23', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '13:24', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '13:25', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '13:26', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '13:27', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '13:28', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '14:15', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '14:16', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '14:17', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '14:18', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '14:19', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '14:20', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '14:21', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '14:22', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '14:23', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '14:24', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '14:25', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '14:26', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '14:27', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '14:28', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '14:29', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '15:16', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '15:17', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '15:18', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '15:19', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '15:20', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '15:21', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '15:22', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '15:23', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '15:24', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '15:25', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '15:26', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '15:27', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '15:28', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '15:29', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '15:30', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '16:17', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '16:18', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '16:19', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '16:20', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '16:21', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '16:22', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '16:23', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '16:24', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '16:25', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '16:26', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '16:27', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '16:28', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '16:29', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '16:30', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '16:31', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '17:18', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '17:19', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '17:20', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '17:21', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '17:22', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '17:23', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '17:24', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '17:25', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '17:26', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '17:27', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '17:28', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '17:29', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '17:30', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '17:31', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '17:32', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '18:19', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '18:20', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '18:21', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '18:22', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '18:23', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '18:24', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '18:25', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '18:26', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '18:27', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '18:28', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '18:29', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '18:30', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '18:31', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '18:32', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '18:33', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '19:20', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '19:21', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '19:22', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '19:23', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '19:24', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '19:25', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '19:26', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '19:27', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '19:28', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '19:29', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '19:30', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '19:31', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '19:32', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '19:33', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '19:34', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '20:21', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '20:22', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '20:23', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '20:24', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '20:25', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '20:26', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '20:27', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '20:28', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '20:29', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '20:30', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '20:31', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '20:32', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '20:33', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '20:34', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '20:35', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '21:22', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '21:23', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '21:24', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '21:25', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '21:26', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '21:27', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '21:28', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '21:29', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '21:30', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '21:31', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '21:32', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '21:33', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '21:34', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '21:35', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '21:36', 'message': ANKETA},
{'channel_id': channel_id1, 'send_time': '22:23', 'message': ANKETA},
{'channel_id': channel_id2, 'send_time': '22:24', 'message': ANKETA},
{'channel_id': channel_id3, 'send_time': '22:25', 'message': ANKETA},
{'channel_id': channel_id4, 'send_time': '22:26', 'message': ANKETA},
{'channel_id': channel_id5, 'send_time': '22:27', 'message': ANKETA},
{'channel_id': channel_id6, 'send_time': '22:28', 'message': ANKETA},
{'channel_id': channel_id7, 'send_time': '22:29', 'message': ANKETA},
{'channel_id': channel_id8, 'send_time': '22:30', 'message': ANKETA},
{'channel_id': channel_id9, 'send_time': '22:31', 'message': ANKETA},
{'channel_id': channel_id10, 'send_time': '22:32', 'message': ANKETA},
{'channel_id': channel_id11, 'send_time': '22:33', 'message': ANKETA},
{'channel_id': channel_id12, 'send_time': '22:34', 'message': ANKETA},
{'channel_id': channel_id13, 'send_time': '22:35', 'message': ANKETA},
{'channel_id': channel_id14, 'send_time': '22:36', 'message': ANKETA},
{'channel_id': channel_id15, 'send_time': '22:37', 'message': ANKETA},
]

# Функция для отправки сообщения в указанный канал
def send_message(channel_id, message):
    try:
        # Отправляем сообщение через клиент Telegram
        client.send_message(channel_id, message)
        
        # Выводим информацию о времени отправки сообщения
        print(f'Сообщение от {phone_number} отправлено в канал с ID {channel_id} в {datetime.now()}')
    except telethon.errors.rpcerrorlist.SlowModeWaitError as e:
        # Обрабатываем ошибку SlowModeWaitError, если она возникает
        wait_time = e.seconds
        print(f'Ожидание {wait_time} секунд перед отправкой следующего сообщения...')
        time.sleep(wait_time)
        send_message(channel_id, message)

# Создание клиента Telegram с использованием 'session_name', 'api_id' и 'api_hash'
with TelegramClient('session_name', api_id, api_hash) as client:
    # Устанавливаем соединение с серверами Telegram
    client.connect()
    
    # Проверяем, авторизован ли аккаунт пользователя
    if not client.is_user_authorized():
        # Если не авторизован, запрашиваем код подтверждения и авторизуемся
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Введите код подтверждения: '))

    # Настройка задач планировщика для отправки сообщений
    for channel_data in channel_schedule:
        channel_id = channel_data['channel_id']
        send_time = channel_data['send_time']
        message_text = channel_data['message']
        # Запланировать отправку сообщения в указанное время
        schedule.every().day.at(send_time).do(send_message, channel_id=channel_id, message=message_text)

    # Бесконечный цикл выполнения задач планировщика
    while True:
        # Запуск задач планировщика, проверка выполнения задач
        schedule.run_pending()
        
        # Подождать 1 секунду перед следующей проверкой задач
        time.sleep(1)