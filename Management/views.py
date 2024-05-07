from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Menu
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from .form import signUp,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User,Group
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    data= Menu.objects.all()
    # groups = Group.objects.all()
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Admins'):
            return render(request,'adminHomepage.html', {'name': request.user, 'data': data})
        else:
            return render(request, 'userHomepage.html', {'name': request.user, 'data': data})
    fm = AuthenticationForm()
    form = signUp()
    return render(request,'Homepage.html',{'data':data,'loginform':fm,'signupform':form})

def addItem(request):
    if request.user.groups.filter(name='Admins'):
        if request.method == "POST":
            item_name = request.POST['item_name']
            item_description = request.POST['item_description']
            item_price = request.POST['item_price']
            item_photo = request.FILES['photo']
            app = Menu(item_name=item_name, item_description=item_description, item_price=item_price, item_photo=item_photo)
            app.save()
            messages.success(request, 'Item Added Successfully')
            return redirect('/')
        else:
            messages.warning(request,'Unable to add item')
            return redirect('/AddMenuItem')
    else:
        messages.warning(request,'User is not authorized for this action')
        return redirect('/')
    return redirect('/')

def addMenuItem(request):
    if request.user.groups.filter(name='Admins'):
        return render(request,'Add_menu_item.html',{'name':request.user})
    else:
        return redirect('/')

def userSignUp(request):
    if request.method=='POST' :
        form=signUp(request.POST)
        groups=Group.objects.get(name='customers')
        if form.is_valid():
            new_user=form.save()
            groups.user_set.add(new_user)
            messages.success(request,'Successfully Registered New User ')
            return redirect('/')
        else:
            errorsmsg =form.errors.values()
            messages.warning(request,'User Creation Failed')
            for msg in errorsmsg:
                messages.warning(request, msg)
            return redirect('/')
    return redirect('/')


def userLogin(request):
    if request.method=='POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                messages.success(request,'User Logged In Successfully')
                return redirect('/')
            else:
                errorsmsg = fm.errors.values()
                messages.warning(request,'User Login Failed please check the entered details')
                for msg in errorsmsg:
                    messages.warning(request, msg)
                return redirect('/')
        else:
            errorsmsg = fm.errors.values()
            messages.warning(request,'User Login Failed please enter valid details')
            for msg in errorsmsg:
                messages.warning(request, msg)
            return redirect('/')
    return redirect('/')


def userLogout(request):
    logout(request)
    messages.success(request,"User Logged out successfully")
    return redirect('/')

def userManagement(request):
    if request.user.groups.filter(name='Admins'):
        data = User.objects.all()
        return render(request,'manageUser.html',{'name' : request.user, 'users' : data})
    else:
        return redirect('/')

def deleteUser(request):
    if request.user.groups.filter(name='Admins'):
        id = request.GET["id"]
        User.objects.filter(id=id).delete()
        messages.success(request,'User Deleted Successfully')
        return redirect('/manageUsers')
    else:
        return redirect('/')

def updateUser(request):
    if request.user.groups.filter(name='Admins'):
        user_id = request.GET["id"]
        user_to_edit = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=user_to_edit)
            if form.is_valid():
                form.save()
                messages.success(request,'User Updated Successfully')
                return redirect('/manageUsers')
            else:
                errorsmsg = form.errors.values()
                messages.warning(request, 'Unable to Update User please check the entered details')
                for msg in errorsmsg:
                    messages.warning(request, msg)
                return redirect('/manageUsers')
        else:
            form = UserUpdateForm(instance=user_to_edit)
            return render(request, 'Update_user.html', {'form': form})
    else:
        return redirect('/')


def photo_view(request, photo_name):
    photo_path = os.path.join(settings.MEDIA_ROOT, 'media/photo/'+photo_name)
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')  # Adjust content type as per your image format
    else:
        return HttpResponse(photo_path+' unable to fetch the file')


def MenuManage(request):
    if request.user.groups.filter(name='Admins'):
        data = Menu.objects.all()
        return render(request,'ManageMenu.html',{'name' : request.user, 'items' : data})
    else:
        return redirect('/')