from celery.task import Task
from celery.registry import tasks
import time

class FirstTask(Task):
	def run(self, **kwargs):
		time.sleep(30)
		return 'completed'

class SecondTask(Task):
	def run(self, **kwargs):
		time.sleep(10)
		return 'completed'

tasks.register(FirstTask)
tasks.register(SecondTask)
