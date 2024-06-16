from django.db import IntegrityError
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse 
from .forms import SignupForm, LoginForm
from .models import Group
from .forms import GroupForm, ActivityForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# Group detail page
def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, 'capstone/group_detail.html', {'group': group})

# Home page
def index(request):
    groups = Group.objects.all()
    group_form = GroupForm()
    activity_form = ActivityForm()

    paginator = Paginator(groups, 5)
    page_number = request.GET.get('page')

    try:
        groups = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)


    return render(request, 'capstone/index.html', {'groups': groups, 'group_form': group_form, 'activity_form': activity_form})

def create_group_page(request):
    group_form = GroupForm()
    return render(request, 'capstone/create_group.html', {'group_form': group_form})

# Calendar page
def calendar_view(request):
    user_groups = Group.objects.filter(users=request.user)
    group_dates = {group.time_and_date.strftime('%Y-%m-%d'): {'time': group.time_and_date.strftime('%H:%M'), 'name': group.name, 'url': reverse('group_detail', args=[group.id])} for group in user_groups}
    return render(request, 'capstone/calendar.html', {'user_groups': user_groups, 'group_dates': group_dates})

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'capstone/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'capstone/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


# Join a group
def join_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.users.add(request.user)
    group.save()
    return redirect('group_detail', group_id=group_id)


# Create a new group
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user 
            group.save() # Save the group to the database
            group.users.add(request.user)  # Add the creator to the group
            form.save_m2m()  # Needed for many-to-many fields
            messages.success(request, "Group: Group created successfully.")
            return redirect('group_detail', group_id=group.id)  # Redirect to the group_detail page of the newly created group
        else:
            messages.error(request, 'Group: Error creating group. Please try again and fill out all fields.')
            return redirect('create_group_page')
    else:
        form = GroupForm()
         
    return redirect('create_group_page')

# Create a new activity
def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            messages.success(request, "Activity: Activity created successfully.")
            return redirect('index')  # Redirect back to the index page
        else:
            messages.error(request, 'Activity: Error creating activity. Please try again.')
    else:
        form = ActivityForm()
    return render(request, 'capstone/index.html', {'form': form})