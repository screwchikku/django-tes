from django.http import HttpResponse
def hello(request):
      text = """<h1>Welcome to my app !</h1>""" """<h2>Thanks for visiting !</h2>"""
      return HttpResponse(text)
def action(request):
      text = """<h1>welcome to my app number !</h1>"""
      return HttpResponse(text)
