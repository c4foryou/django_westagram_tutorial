import json
from django.views import View
from django.http  import JsonResponse, HttpResponse
from .models      import Users
'''
class MainView(View):
    def post(self, request):
        data = json.loads(request.body)
        Users(
              name     = data['name'],
              email    = data['email'],
		password = data['password']
        ).save()
        
        return JsonResponse({'message':'SUCCESS'}, status=200)

	def get(self, request):
		user_data = Users.objects.values()
		return JsonResponse({'users':list(user_data)}, status=200)
'''

class Signin(View):
	def post(self, request):
		account_data = json.loads(request.body)
		try:
			if Users.objects.filter(name=account_data['name']).exists():
				user = Users.objects.get(name=account_data['name'])
				if user.password == account_data['password']:
					return JsonResponse({'message':'Hello!'}, status=200)
					#return HttpResponse(status=200)
				return HttpResponse(status=401)
			return HttpResponse(status=400)
		except KeyError:
			return HttpResponse(status=400)
			


class Signup(View):
	def post(self, request):
		account_data = json.loads(request.body)

		try:
			if not Users.objects.filter(name=account_data['name']).exists():
				Users(
				    name=account_data['name'],
				    email=account_data['email'],
				    password=account_data['password']
				).save()
			else:
				return HttpResponse(status=409)
		except KeyError:
			return HttpResponse(status=400)

		return JsonResponse({'message':'SUCCESS'}, status=200)
		


