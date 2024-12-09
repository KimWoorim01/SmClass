from django.shortcuts import render


def index(request):
  # templates 에서 찾음
  return render(request, 'index.html')

# Create your views here.
