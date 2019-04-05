from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm, \
                   ParticipationForm
from .models import Profile,Participation,Event,Event_Type

from django.views.generic.base import TemplateView
from django.views import generic



class HomePageView(TemplateView):
    template_name='account/home.html'

#display the list of all events
class EventListView(generic.ListView):
    model=Event
    #context_object_name='event_list' #your own name for the list as a template variable
    queryset=Event.objects.all()
    template_name='account/event_list.html'

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    profile_dictionary={}
    profile_dictionary['section']='dashboard'

    return render(request,
                  'account/dashboard.html',
                  profile_dictionary)

@login_required
def profile_display(request):
        profile_dictionary={}
        profile_dictionary['username']=str(request.user.username)
        profile_dictionary['email']=str(request.user.email)
        #profile_dictionary['section']='dashboard'
        event_list_technical=[]
        event_list_non_technical=[]
        for o in list(Participation.objects.all()):
            if(str(o.participant)==str(request.user)):
                if(str(o.event).split()[1]=='NON-TECHNICAL'):
                    event_list_non_technical.append(str(o.event).split()[0])
                else:
                    event_list_technical.append(str(o.event).split()[0])


        event_list_non_technical=list(set(event_list_non_technical))
        event_list_technical=list(set(event_list_technical))
        event_list_non_technical.sort()
        event_list_technical.sort()

        print('Tech:',event_list_technical)
        print('Non-Tech:',event_list_non_technical)
        
        profile_dictionary['event_list_non_technical']=event_list_non_technical
        profile_dictionary['event_list_technical']=event_list_technical
        print('Non-Tech:',profile_dictionary['event_list_non_technical'])
        print('Tech:',profile_dictionary['event_list_technical'])
        for o in list(Profile.objects.all()):
            if(str(o.user)==str(request.user)):
                profile_dictionary['college']=str(o.college)
                profile_dictionary['phone']=str(o.phone)
                profile_dictionary['year']=str(o.year)
                profile_dictionary['payment_status']=bool(o.payment_status)
                break
        print(profile_dictionary)
        if(bool(profile_dictionary['payment_status'])):
            profile_dictionary['payment_status']='PAID'
        else:
            profile_dictionary['payment_status']='NOT PAID'

        return render(request, 'account/profile.html', profile_dictionary)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def add_event(request):
    if request.method=='POST':
        event_form=ParticipationForm(request.POST)
        if event_form.is_valid():
            print('SAVING')
            print(event_form.cleaned_data['event'])

            for obj in Profile.objects.all():
                if(str(obj)==str(request.user)):
                    obj1=obj
            print(obj1)
            for obj in Event.objects.all():
                print(str(obj).split()[0]," ",str(event_form.cleaned_data['event'][0]))
                if(str(obj).split()[0]==str(event_form.cleaned_data['event'].split()[0])):
                    obj2=obj

            obj3=Participation(participant=obj1, event=obj2)
            obj3.save()
            print('SAVING')
            #event_form.save()
        else:
            message.error(request, 'Error adding event')

    else:
        event_form= ParticipationForm(request.POST)

    return render(request, 'account/add_event.html', {'event_form':event_form})
