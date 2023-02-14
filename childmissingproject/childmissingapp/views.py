from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User, Group, auth
from django.contrib import messages
from childmissingapp .models import complainant, Police, user, complainant_history, user_history
from .forms import complainantForm, userForm
from django.contrib.auth import login 
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.conf import settings
from django.http import FileResponse
from io import BytesIO
import face_recognition
import numpy as np
import os


# Create your views here.

def index(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login_view')
        else:
            messages.info(request, "")
            return redirect('register')

    return render(request,'register.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            badge_number = form.cleaned_data['badge_number']
            is_police = form.cleaned_data['is_police']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                try:
                    if is_police == True:
                        user_id = user.id
                        police_instance = Police.objects.get(user_id=user_id)
                        badge_number_police = police_instance.badge_number
                        if badge_number_police == badge_number:
                            auth.login(request, user)
                            return redirect('police')
                        else:
                            return HttpResponse("Error: Police object with username '{}' does not exist".format(username))
                    else:
                        auth.login(request, user)
                        return redirect('new')
                except:
                    return HttpResponse("Error: Police object with username '{}' does not exist".format(username))
            else:
                return HttpResponse("Error: Username or Password is wrong")
    else:
        form = LoginForm()

    return render(request, 'userslogin.html', {'form': form})

def police(request):
    compl = complainant.objects.all()
    use = user.objects.all()
    compl_his = complainant_history.objects.all()
    use_his = user_history.objects.all()
    return render(request, 'police.html',{'compl':compl, 'use':use, 'compl_his':compl_his, 'use_his':use_his})

def update_compl(request, id):
    compl = complainant.objects.get(id=id)
    if request.method=='POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        phone_number = request.POST.get('phone_number')
        child_name = request.POST.get('child_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        identification = request.POST.get('identification')
        Details = request.POST.get('Details')
        staus = request.POST.get('staus')
        report = request.POST.get('report')
        upd_com = complainant_history(name=name, place=place, phone_number=phone_number, child_name=child_name, age=age, gender=gender, identification=identification, Details=Details, staus=staus, report=report)
        upd_com.save()
        compl = complainant.objects.get(id=id)
        compl.delete()
        return redirect('police')
    return render(request, 'update_compl.html', {'compl':compl})

def update_user(request, id):
    usr = user.objects.get(id=id)
    if request.method=='POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        phone_number = request.POST.get('phone_number')
        child_name = request.POST.get('child_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        identification = request.POST.get('identification')
        Details = request.POST.get('Details')
        staus = request.POST.get('staus')
        report = request.POST.get('report')
        usr = user_history(name=name, place=place, phone_number=phone_number, child_name=child_name, age=age, gender=gender, identification=identification, Details=Details, staus=staus, report=report)
        usr.save()
        usr = user.objects.get(id=id)
        usr.delete()
        return redirect('police')
    return render(request, 'update_user.html', {'usr':usr})

def view_compl(request, id):
    com_details = complainant.objects.get(id = id)
    return render(request, 'com_details.html', {'com_details':com_details})

def view_user(request, id):
    user_details = user.objects.get(id = id)
    return render(request, 'user_details.html', {'user_details':user_details})






def new(request):
    com = complainant.objects.filter(complintent = request.user)
    return render(request, 'new.html',{'com':com})

def complainant_view(request):
    comp = complainant.objects.filter(complintent = request.user)
    if request.POST:
        form = complainantForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            comp = form.save()
            comp.complintent = request.user
            comp.save()
            return redirect('complainant')
        else:
            return HttpResponse(request, 'form is not valid Please fill correctly')
    return render(request, 'complainant.html',{'form': complainantForm,'comp':comp})

def user_view(request):
    if request.POST:
        form = userForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            form.save()
            return redirect('last_user_page')
        else:
            return HttpResponse(request, 'form is not valid Please fill correctly')
    return render(request, 'user.html',{'form': userForm})

def complainant_last_page(request):
    return render(request, 'complainant_last_page.html')

def last_user_page(request):
    return render(request, 'last_user_page.html')

def search(request, id):
    com = complainant.objects.get(id = id)
    return render(request, 'search.html',{'com':com})

def search_child(request,id):
    if request.method == 'POST':
        com = complainant.objects.get(id = id)
        image_file = com.img
        image_bytes = BytesIO()
        for chunk in image_file.chunks():
            image_bytes.write(chunk)

        # Load all the known faces into memory
        known_face_encodings = []
        known_face_names = []
        # Load a sample picture and learn how to recognize it.
        folder_path = os.path.join(settings.MEDIA_ROOT, 'pics')
        for filename in os.listdir(folder_path):
            # Load the image
            image = face_recognition.load_image_file(os.path.join(folder_path, filename))
            
            # Get the face encodings for the faces in the image
            face_encodings = face_recognition.face_encodings(image)
            
            # Loop over the encodings
            for face_encoding in face_encodings:
                # Add the encoding and name to the lists
                known_face_encodings.append(face_encoding)
                known_face_names.append(filename.split(".")[0])

        # Load the test image
        test_image = face_recognition.load_image_file(image_bytes)

        # Get the face encodings for the faces in the test image
        face_locations = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image, face_locations)

        # Loop over the face encodings in the test image
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the test face encoding to the known face encodings
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            
            # Find the index of the best match
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            # If there is a match
            # if matches[best_match_index]:
            #     name = known_face_names[best_match_index]
            #     print(f"Found match: {name}")
            #     return render(request,'success.html',{'name':name})

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                best_match_filename = f"{name}.jpg"
                best_match_image_path = os.path.join('media', 'pics', best_match_filename)
                context = {'best_match_image_path': best_match_image_path }
                return render(request, 'success.html', context)
            else:
                return redirect('complainant_last_page')

    return redirect('complainant_last_page')


def success(request):
    return render(request, 'success.html')

# def image_details(request):
#     if request.method == 'POST':
#         image_url = request.POST.get('image_url')
#         row = user.objects.get(image = image_url)
#         return render(request, 'image_details.html', {'row': row})

def image_details(request):
     if request.method == 'GET':
        image_url = request.GET.get('image_url')
        row = get_object_or_404(user, image=image_url)
        return render(request, 'image_details.html', {'row': row})
    

    