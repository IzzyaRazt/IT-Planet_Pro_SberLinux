import schedule
import time

def backup():
    print("Backing up files...")
    # Здесь код для выполнения резервного копирования

schedule.every().day.at("01:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)