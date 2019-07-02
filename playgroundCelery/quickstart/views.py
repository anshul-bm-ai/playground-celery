from django.shortcuts import render
from rest_framework.views import APIView
from .tasks import FirstTask, SecondTask
from celery.result import AsyncResult
from rest_framework.response import Response

# Create your views here.

class FirstView(APIView):

	def post(self, request):

		result = FirstTask.delay()
		print(result.task_id)
		return Response({
			'message': 'FirstTask finished!',
			'task_id': result.task_id
		})

class SecondView(APIView):

	def post(self, request):
		task_id = request.data.get('task_id')
		res = AsyncResult(task_id)
		print(res.ready())
		while(not res.ready()):
			continue
		result = SecondTask.delay()
		print(result.task_id)
		return Response({
			'message': 'SecondTask finished!',
			'task_id': result.task_id
		})