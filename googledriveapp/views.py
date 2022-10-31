from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Model imports
from googledriveapp.models import Folder,File
from mail.models import User
# Create your views here.
# Main page for our drive clone with folders in it where user can click and go to the specific folder 
def drive_index(request):
    if request.user.is_authenticated:
        folder = Folder.objects.filter(folderuser=request.user)
        context = {'folder':folder}
        return render(request,'googledriveapp/drive_index.html',context)
    else:
        return redirect('drive_signup')
# Folder with files in it
def drive_folder(request,folderid):
    if request.user.is_authenticated:
        folder_user = Folder.objects.get(id=folderid)
        files = File.objects.filter(folder=folder_user)
        context = {'folderid':folderid,'files':files}
        if request.method == 'POST':
            file_user = request.FILES.get('file')
            file_title = request.POST.get('filetitle')
            fileadd = File.objects.create(filetitle=file_title,file=file_user,folder=folder_user)
        return render(request,'googledriveapp/drive_folder.html',context)
    else:
        return redirect('drive_signup')
# Add Folder View
def drive_addfolder(request):
   if request.method == 'POST':
       folder_name = request.POST['foldername']
       folder_desc = request.POST['desc']
       folder = Folder.objects.create(foldername=folder_name,folderdesc=folder_desc,folderuser=request.user)
       if folder:
           return redirect("drive_index")
       else:
            messages.error(request,"Folder Not Created")
            return redirect("drive_index")
# View For SignUp the user
def drive_SignUp(request):
    if request.user.is_authenticated:
        return redirect('drive_index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            firstname = request.POST['fname']
            lname = request.POST['lname']
            if username and password and email and cpassword and firstname and lname:
                if password == cpassword:
                    user = User.objects.create_user(username,email,password)
                    user.first_name = firstname
                    user.last_name = lname
                    user.save()
                    if user:
                        messages.success(request,"User Account Created")
                        return redirect("drive_login")
                    else:
                        messages.error(request,"User Account Not Created")
                else:
                    messages.error(request,"Password Not Matched")
                    redirect("drive_signup")
        return render(request,'googledriveapp/drive_signup.html')
    
# View For Log in the user
def drive_Login(request):
    if request.user.is_authenticated:
        return redirect("drive_login")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('drive_index')
        return render(request,'googledriveapp/drive_login.html')
# User logout function
def drive_Logout(request):
    logout(request)
    return redirect("drive_index")