from django.shortcuts import render, redirect
from students.models import Student

def view(request,name):
  qs = Student.objects.get(name = name)
  context = {"stu":qs}
  return render(request,'view.html',context)


def list(request):

  # 학생전체정보 가져오기
  qs = Student.objects.all()

  context = {"slist":qs,}

  return render(request, 'list.html', context)


def write(request):
  # templates 에서 찾음

  if request.method == "POST":
    name = request.POST.get('name')             #데이터가 없을때 None 으로 리턴
    major = request.POST.get('major')
    grade = request.POST['grade']              #데이터가 없으면 error
    age = request.POST['age']
    gender = request.POST['gender']
    # hobby = request.POST['hobby']
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)                    #str 타입으로 변경
    hobby_list = hobby.split(",")               #list 타입으로 변경

    print(name)
    # print("hobby 단수 : " + hobby)
    print("hobbys 복수 : " + hobbys)

    # qs = Student(name=name,major = major, grade = grade, age = age , gender = gender, hobby = hobbys)
    # qs.save()

    # save() 가 필요 없음
    Student.objects.create(name=name,major = major, grade = grade, age = age , gender = gender, hobby = hobbys) 


    return redirect('/')

    pass
  else:       # GET 호출
    return render(request, 'write.html')



# Create your views here.
