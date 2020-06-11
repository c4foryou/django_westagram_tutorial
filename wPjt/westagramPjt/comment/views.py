import json
from django.views import View
from django.http  import JsonResponse, HttpResponse
from .models      import Comment


class CommentView(View):
	def post(self, request):
		comment_data = json.loads(request.body)
		Comment(
			    name=comment_data['name'],
			    comments=comment_data['comments'],
				).save()
		return JsonResponse({'message':'uploaded'}, status=200)
		
	def get(self, request):
		return JsonResponse({'comments':list(Comment.objects.values())}, status=200)
		
