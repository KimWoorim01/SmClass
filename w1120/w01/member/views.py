from django.shortcuts import render

# Create your views here.

def mlist(request):
  return render(request, 'mlist.html')