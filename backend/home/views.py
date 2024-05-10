from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.http import Http404
from deepface import DeepFace
from django.views.generic import TemplateView
import base64
# from _future_ import unicode_literals
from io import BytesIO
import io
import cv2

import numpy as np
from PIL import Image

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def error(request):
    return render(request, 'home/error.html')


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Create profile
            photo = form.cleaned_data.get('photo')
            profile = Profile.objects.create(user=user, photo=photo)
            print(request.FILES)
            print(photo)
            print("Profile Created")

            # Sending activation email
            current_site = get_current_site(request)
            mail_subject = 'Activate account'
            message = render_to_string('home/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'domain': "{0}".format("http://127.0.0.1:8000"),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.content_subtype = 'html'
            email.mixed_subtype = 'related'
            email.send()
            context = {"user_data": user}
            return render(request, 'home/confirm.html', context)
    else:
        form = SignupForm()
    return render(request, 'home/index.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')


def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return opencv_img


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # data = request.POST.get('image')
        captured_image = request.POST.get('image')
        my_image = captured_image[22:]
        image_data = stringToRGB(my_image)
        # img = Image.fromarray(image_data, 'RGB')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                # print(username, password, captured_image)
                profile = Profile.objects.get(user=user)
                profile_photo = profile.photo.path
                # src is the name of input attribute in your html file, this src value is set in javascript code

                with open(profile_photo, 'rb') as f:
                    reference_image_data = f.read()

                # Convert the reference image bytes into an image
                reference_image = Image.open(io.BytesIO(reference_image_data))

                # Convert the captured image bytes into an image
                # captured_image_data = img.read()
                # captured_image = Image.open(io.BytesIO(img))

                # Convert images to numpy arrays
                reference_image_np = np.array(reference_image)
                # captured_image_np = np.array(captured_image)

                result = DeepFace.verify(
                    img1_path=reference_image_np, img2_path=image_data)
                print(result)
                if result['verified']:
                    print("Verification completed")
                    return redirect(f"profile/{profile.user.id}/")
                else:
                    print("User not authorized")
                    return redirect("error")
            except Profile.DoesNotExist:
                # Handle the case where the user doesn't have a profile
                raise Http404("Profile matching query does not exist.")
            except ValueError as e:
                # Handle the case where face detection fails
                return render(request, 'home/detection_error.html')
        else:
            # Handle invalid credentials
            context = {'error': True}
            return render(request, 'home/login.html', context)
    else:
        context = {'error': False}
        return render(request, 'home/login.html', context)


def profile(request, pk):
    if request.user.is_authenticated:
        user_data = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user_data)

        context = {"user_data": user_data,
                   "profile": profile}
        return render(request, 'home/profile.html', context)

    else:
        return redirect("login")


def logout(request):
    auth.logout(request)
    return redirect("/login")