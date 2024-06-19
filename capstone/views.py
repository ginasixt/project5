from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse 
from .forms import SignupForm, LoginForm
from .models import Group
from .forms import GroupForm, ActivityForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta, timezone
from django.utils import timezone
from django.utils.timezone import localtime, utc
import pytz


# Create your views here.

# Group detail page
def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)

    if (group.time_and_date >= timezone.now()):
        next_event_date = group.time_and_date
    elif group.recurring:
        current_date = group.time_and_date
        max_iterations = 10

        for _ in range(max_iterations):
            if current_date >= timezone.now():
                next_event_date = current_date
                break
            current_date += timedelta(days=7)
    else:
        next_event_date = None
    
    return render(request, 'capstone/group_detail.html', {'group': group, 'next_event_date': next_event_date,})

# Home page
def index(request):
    groups = Group.objects.all()

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


    return render(request, 'capstone/index.html', {'groups': groups})

# Create group page
def create_group_page(request):
    group_form = GroupForm(instance=Group()) 
    return render(request, 'capstone/create_group.html', {'group_form': group_form})

# Create activity page
def create_activity_page(request):
    activity_form = ActivityForm()
    return render(request, 'capstone/create_activity.html', {'activity_form': activity_form})







# Calendar page
def calendar_view(request):
    user_groups = Group.objects.filter(users=request.user)
    group_dates = {}
    for group in user_groups:
        # Convert to local time first, then to UTC
        local_time = localtime(group.time_and_date)
        utc_time = local_time.astimezone(pytz.utc)
        formatted_date = utc_time.strftime('%Y-%m-%d')
        formatted_time = utc_time.strftime('%H:%M')
        group_name = group.name
        group_url = reverse('group_detail', args=[group.id])
        group_dates[formatted_date] = {'time': formatted_time, 'name': group_name, 'url': group_url}
        
        if group.recurring:
            for i in range(1, 10):
                new_date = utc_time + timedelta(weeks=i)
                formatted_new_date = new_date.strftime('%Y-%m-%d')
                formatted_new_time = new_date.strftime('%H:%M')
                group_dates[formatted_new_date] = {'time': formatted_new_time, 'name': group_name, 'url': group_url}
    return render(request, 'capstone/calendar.html', {
        'user_groups': user_groups,
        'group_dates': group_dates})

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

# Leave a group
def leave_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.users.remove(request.user)
    group.save()
    return redirect('group_detail', group_id=group_id)

# Delete a group    
def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    if group.creator != request.user:
        messages.error(request, 'You cant delete the group, you are not the creator.')
        return redirect('group_detail', group_id=group_id)
    group.delete()
    messages.success(request, "Successfull.")
    return redirect('index')

# Create a new group
def create_group(request, group_id=None):
    # Check if the group exists and the current user is the creator
    if group_id:
        group = Group.objects.get(id=group_id)
        if group.creator != request.user:
            messages.error(request, 'You do not have permission to edit this group.')
            return redirect('group_detail', group_id=group_id)
    else:
        group = Group()

    # Handle form submission
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user
            group.save()
            group.users.add(request.user)
            form.save_m2m()
            messages.success(request, "Group updated successfully." if group_id else "Group created successfully.")
            return redirect('group_detail', group_id=group.id)
        else:
            messages.error(request, 'Error creating/updating group. Please try again and fill out all fields.')
    else:
        form = GroupForm(instance=group)

    return render(request, 'capstone/create_group.html', {'group_form': form, 'group': group})

# Create a new activity
def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            messages.success(request, "Activity: Activity created successfully.")
            return redirect('create_activity_page')  
        else:
            messages.error(request, 'Activity: Error creating activity. Please try again.')
    else:
        form = ActivityForm()
    return redirect('create_activity_page') 