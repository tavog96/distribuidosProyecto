import os
from datetime import datetime, date

def log (logType, msg):
    if (logType !='Info' and logType !='Warning' and logType !='Error'):
        raise ValueError('logType not valid')
    now = datetime.now()
    today = date.today()
    logFile = open(today.isoformat()+'.log', 'a')
    logFile.write(logType+': '+msg+'('+now.isoformat()+')'+'\n')
    logFile.close()