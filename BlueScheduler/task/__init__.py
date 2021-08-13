from BlueScheduler.task.crontab_task import get_deley_tasks
from redis import Redis
from rq import Queue, queue
from rq_scheduler import Scheduler
from datetime import timedelta

scheduler = Scheduler(connection=Redis())

def register_crontab_task():
    scheduler.enqueue_in(timedelta(seconds=1), get_deley_tasks)
