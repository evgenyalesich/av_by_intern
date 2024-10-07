import telebot
import db_connector
import schedule
import time


bot = telebot.TeleBot("6804030085:AAEODu2L_L1F2tXf0EAHLodG4YXFB9rXqX8")


def send_all(to_sent):
    users = db_connector.get_all_not_blocked_users()
    for user_id in users:
        print(f"{user_id}: {to_sent}")
        bot.send_message(user_id, to_sent)


def schedule_jobs():
    all_jobs = db_connector.get_all_planed_job()
    for job in all_jobs:
        every_period = job[0]
        period_time = job[1]
        message = job[2]
        if every_period == 'seconds':
            schedule.every(period_time).seconds.do(send_all, to_sent=message)
        elif every_period == 'minutes':
            schedule.every(period_time).minutes.do(send_all, to_sent=message)


schedule_jobs()

while True:
    schedule.run_pending()
    time.sleep(5)
