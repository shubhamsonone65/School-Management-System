from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . forms import user_log
from django.contrib import messages


# Create your views here.
def signup(request):
    form=user_log()
    allowed=['superuser','teacher','student']
    if request.method=='POST':
        try:
            ch=request.POST.get('select')
            form=user_log(request.POST)
            if (form.is_valid):
                # saving form to database if valid
                user=form.save()
                grp=Group.objects.get(name=ch)
                user.groups.add(grp)
                messages.success(request,'account is successfully created...')
        except:
            messages.error(request,'invalid credentials...please try again')
            # return redirect('home')
    return render(request,'signup.html',{'form':form}) 

def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        # authenticating user to login
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # if the user is from student group we will show him his datails 
            if(request.user.groups.first().name=='students'):
                return redirect(f'student/{user.id}')
            # otherwise redirect to logged in page
            return redirect('page')
        else:
            messages.error(request,'invalid credentials...')
    return render(request,'home.html') 

@login_required(login_url="/")
def log_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/")
def page(request):
    # if user is superadmin he will redirected to page where he can see and edit student/teacher data
    if(request.user.groups.first().name=='superadmin'):
        teacher_id=Group.objects.get(name='teacher').id
        teacher=User.objects.filter(groups=teacher_id)
        student_id=Group.objects.get(name='students').id
        student=User.objects.filter(groups=student_id)
        context={'teacher':teacher,'student':student}
        print(context)
        return render(request,'page.html',context)
    # if user is teacher he will be shown only student details
    if(request.user.groups.first().name=='teacher'):
        teacher=None
        student_id=Group.objects.get(name='students').id
        student=User.objects.filter(groups=student_id)
        context={'teacher':teacher,'student':student}
        print(context)
        return render(request,'page.html',context)
    return redirect('/')

# to display teacher details
@login_required(login_url="/")
def teachdetail(request,pk):
    teacher=User.objects.get(id=pk)
    return render(request,'details.html',{'teacher':teacher})


@login_required(login_url="/")
def studdetail(request,pk):
    student=User.objects.get(id=pk)
    return render(request,'detailstud.html',{'student':student})


@login_required(login_url="/")
def deleteteach(request,pk):
    teacher=User.objects.get(id=pk)
    teacher.delete()
    return redirect('page')


@login_required(login_url="/")
def deletestud(request,pk):
    student=User.objects.get(id=pk)
    student.delete()
    return redirect('page')

@login_required(login_url="/")
def add(request):
    form=user_log()
    if request.method=='POST':
        try:
            ch=request.POST.get('select')
            form=user_log(request.POST)
            if (form.is_valid):
                user=form.save()
                grp=Group.objects.get(name=ch)
                user.groups.add(grp)
                messages.success(request,'account is added to database successfully...')
        except:
            messages.error(request,'invalid credentials...please try again')
    return render(request,'add.html',{'form':form})

@login_required(login_url="/")
def addstudent(request):
    form=user_log()
    if request.method=='POST':
        ch=request.POST.get('select')
        form=user_log(request.POST)
        if (form.is_valid):
            user=form.save()
            grp=Group.objects.get(name=ch)
            user.groups.add(grp)
            messages.success(request,'account is added to database successfully...')
        else:
            messages.error(request,'invalid credentials...')
    return render(request,'addstudent.html',{'form':form})