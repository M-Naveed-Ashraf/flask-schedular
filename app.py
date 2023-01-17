# import sched
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

app = Flask(__name__)

scheduler = BackgroundScheduler()

jobs = [
    {
        'expiry': '2023-01-17T11:48:32.788',
        'status': True
    },
    {
        'expiry': '2023-01-17T13:10:32.788',
        'status': False
    },
    {
        'expiry': '2023-01-17T13:11:32.788',
        'status': False
    },
    {
        'expiry': '2023-01-18T11:48:32.788',
        'status': False
    },
]

@app.route('/')

def scheduleJob():
    for obj in jobs:
        formatedExpiry = datetime.datetime.fromisoformat(obj['expiry']).timestamp()
        currentTime = datetime.datetime.now().timestamp()
        if formatedExpiry-currentTime <= 0 and obj['status'] != True:
            print('deleting a post', obj['expiry'])

scheduler.add_job(func=scheduleJob, trigger='interval', seconds=10)
scheduler.start()
if __name__ == '__main__':
    app.run()