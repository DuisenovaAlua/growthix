from django.shortcuts import *
from .forms import SignUp1Form,SignUp2Form
from .models import Test,User2
import random
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index2.html'); 


def Save(request):
    if request.method == 'POST':
        form = SignUp1Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = instance.first_name+instance.last_name
            instance.save()
            return redirect('reg2',instance.user)
    else:
        form = SignUp1Form()
    return render(request, 'reg1.html', {'form': form})

def reg2(request,user):
    error=False;
    if request.method == 'POST':
        form = SignUp2Form(request.POST)
        form.user=user
        form.score=0
        if form.is_valid():    
            form.cleaned_data['user']=user
            form.cleaned_data['score']=0
            if User2.objects.filter(email=form.cleaned_data['email'],checking=False).exists():
                user=form.cleaned_data['user']
                university=form.cleaned_data['university']
                speciality=form.cleaned_data['speciality']
                to_update = User2.objects.filter(email=form.cleaned_data['email']).update(user=user,university=university,speciality=speciality,checking=True)
                return render(request,'reg4.html',{'user':user})
            else:
                error=True
                print(error)
                

    else:
        form = SignUp2Form()
    return render(request, 'reg2.html', {'form': form,'user':user,'error':error})

def reg4(request,user):
    return render(request,'reg4.html',{'user':user}); 

def no(request,user):
    return render(request,'not_available.html',{'user':user}); 


def reg3(request,user):
    a=request.GET['root']
    print(a)
    return render(request,'reg3.html',{'user':user,'root':a}); 

def Test_view(request,user,root):
    finance=Test.objects.filter(sections=root).order_by('?')[:25];
    market=Test.objects.filter(sections=root)[25:50];
    sd=Test.objects.filter(sections=root)[51:75]
    ede=Test.objects.filter(sections=root)[75:100];
    return render(request,'finance.html',{'finance':finance,'markets':market,'calc':sd,'theory':ede,"root":root,'user':user})
def result(request,user,root):
    a = request.GET['res']
    correct = 0;
    ta=''
    a = a.replace(",", "")
    a=" "+a;
    print(a)
    j=3
    for i in range(1,int(len(a)/3)):
        if (j<int(len(a)/3)):
            if j<57:
                ta=a[j]
            elif (j==57):
                j+=1
                ta=10
            elif(j+1<len(a)/3):
                ta=a[j]+a[j+1]
            ans=Test.objects.filter(number=int(ta),sections=root)
            if(a[i*6] is str(ans[0])):
                print(ta)
                correct+=1;
            j+=6;
    install = User2.objects.get(user=user)
    install.score=correct;
    install.save()
    return render(request, 'result.html', {'result': correct,'all':int(len(a)/7)})
