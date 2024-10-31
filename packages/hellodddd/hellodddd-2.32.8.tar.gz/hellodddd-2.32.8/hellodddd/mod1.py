import os
import datetime


log_file_path = '/tmp/log11.txt'
def log_message(message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message}\n")

log_message("hello log111111111.txt!")

