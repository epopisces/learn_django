from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home.html', {'user_groups': user_groups})

def about(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'about.html', {'user_groups': user_groups})

@login_required
def contact(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home.html', {'user_groups': user_groups})

@login_required
def admin_dashboard(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'admin_dashboard.html', {'user_groups': user_groups})

@login_required
def user_dashboard(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'user_dashboard.html', {'user_groups': user_groups})

@login_required
def search(request):
    query = request.GET.get('q')
    # Implement your search logic here
    return render(request, 'search_results.html', {'query': query})