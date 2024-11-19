from django.shortcuts import render

# 학생입력페이지 호출
def write(request):
  ## render : html파일 호출
  return render(request,'write.html')
