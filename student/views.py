from django.shortcuts import render,get_object_or_404,redirect
from .forms import MyForm,Academic_form
from .models import StudentInfo,Academics
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def is_superuser(user):
    return user.is_superuser


# Create your views here.



@login_required(login_url="home")
@user_passes_test(is_superuser,login_url="admin_message")
def create(request):
    if request.method == 'POST':
        frm = MyForm(request.POST)  # Create a form instance with POST data

        if frm.is_valid():  # Check if the form is valid
            try:
                frm.save()  # Save the form data to the database
                print("Form saved successfully")
            except Exception as e:
                print("Error saving form:", e)
        else:
            print("Form is not valid:", frm.errors)
    else:
        frm = MyForm()  # Create an empty form instance
        
    return render(request, 'student_create.html', {'frm': frm})


@login_required(login_url="home")
@user_passes_test(is_superuser,login_url="admin_message")
def view(request):
    student_data=StudentInfo.objects.all()
    academics=Academics.objects.all()
    return render(request,'view_students.html',{'studs':student_data})




@login_required(login_url="home")
@user_passes_test(is_superuser,login_url="admin_message")
def edit(request, pk):   
    instance = get_object_or_404(StudentInfo, pk=pk)
    frm = MyForm(instance=instance)
    
    if request.method == 'POST':
        frm = MyForm(request.POST, instance=instance)  
        if frm.is_valid():  # Check if form data is valid
            frm.save()  # Save the form data to the instance
            return redirect('view')  # Redirect to view_students.html after successful form submission
        if not frm.is_valid():
            print(frm.errors)
    
    return render(request, 'student_create.html', {'frm': frm, 'instance': instance})

'''
def academics(request):

    academic_data=Academics.objects.all()
    frm= Academic_form(instance=academic_data)

    if request.method == 'POST':
        frm = MyForm(request.POST, instance=academic_data)  # Bind POST data to form
        if frm.is_valid():  # Check if form data is valid
            frm.save()  # Save the form data to the instance
            return redirect('view')  # Redirect to view_students.html after successful form submission
        if not frm.is_valid():
            print(frm.errors)

    return render(request,'Academics.html',{'frm': frm, 'instance': academic_data})
'''



@login_required(login_url="home")
@user_passes_test(is_superuser,login_url="admin_message")
def academics(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)
    academics_instance = student.academics_set.filter(student_id=pk).first()

    if request.method == 'POST':
        form = Academic_form(request.POST, instance=academics_instance)
        if form.is_valid():
            academics_instance = form.save(commit=False)
            #academics_instance.student = student  # Assign the StudentInfo instance
            academics_instance.student_id_id = student.id
            academics_instance.save()
            print("Form saved successfully")
            return render(request, 'Academics.html', {'form': form, 'instance': student, 'marks': academics_instance})
        else:
            print("Form is not valid:", form.errors)
    else:
        form = Academic_form(instance=academics_instance)

    return render(request, 'Academics.html', {'form': form, 'instance': student, 'marks': academics_instance})




@login_required(login_url="home")
@user_passes_test(is_superuser,login_url="admin_message")
def edit_academics(request):

    academic_data=Academics.objects.all()
    frm= Academic_form(instance=academic_data)

    if request.method == 'POST':
        frm = MyForm(request.POST, instance=academic_data)  # Bind POST data to form
        if frm.is_valid():  # Check if form data is valid
            frm.save()  # Save the form data to the instance
            return redirect('view')  # Redirect to view_students.html after successful form submission
        if not frm.is_valid():
            print(frm.errors)

    return render(request,'Academics.html',{'frm': frm, 'instance': academic_data})


def home(request):
    print(request.POST)
    
    
    if request.POST and 'Register' in request.POST :
    
        try:
            username=request.POST.get('Username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            name=request.POST.get('name')
            Class=request.POST.get('Class')
            Place=request.POST.get('Place')
            phone=request.POST.get('phone')

            
            user=User.objects.create_user(

                username=username,
                password=password,
                email=email
            )

            print(user)
            student=StudentInfo.objects.create(

                    name=name,
                    Class=Class,
                    Place=Place,
                    phone=phone,
                    student_id=name[:3]+str(user.id),
                    user=user
                
            )
            
            success_message="User registered Successfully"
            return redirect('home')
        except Exception as e:
            error_message='invalid username'
            messages.error(request,error_message)
            print(e)
            
    if request.POST and 'user-login' in request.POST :
        
            username=request.POST.get('Username')
            password=request.POST.get('password')
            
            user=authenticate(username=username,password=password)

            if user:
                login(request,user)
                print(user)
                super=user.is_superuser
                print('ajayyyyy:',user.id)
               
                print(super)
                url_student = f'/student_home'
                url_admin=f'/view_students'
                if super:
                    
                    return redirect(url_admin)
                else:
                    return redirect(url_student)
            else:
                return redirect('index.html')


    return render(request,'index.html')
        





def student_home(request):

    return render(request,'student_home.html')

def student_marks(request,pk):

    student = get_object_or_404(StudentInfo, user_id=pk)
    academics_instance = student.academics_set.filter(student_id=student.id).first()

    if request.method == 'POST':
        form = Academic_form(request.POST, instance=academics_instance)
        if form.is_valid():
            academics_instance = form.save(commit=False)
            #academics_instance.student = student  # Assign the StudentInfo instance
            academics_instance.student_id_id = student.id
            academics_instance.save()
            print("Form saved successfully")
            return render(request, 'student_marks.html', {'form': form, 'instance': student, 'marks': academics_instance})
        else:
            print("Form is not valid:", form.errors)
    else:
        form = Academic_form(instance=academics_instance)

    return render(request, 'student_marks.html', {'form': form, 'instance': student, 'marks': academics_instance})


    


def sign_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url="home/")
def delete(request,pk):
    student= get_object_or_404(StudentInfo, pk=pk)
    user = User.objects.get(id=student.user_id)
    print(user)
    user.delete()
    return render(request,'index.html')



def Profile(request,pk):

    student = get_object_or_404(StudentInfo, user_id=pk)
    print(student.name)
    
    return render(request,'profile.html',{'instance':student})


def admin_message(request):
    return render(request,'admin_message.html')