from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Item
from .decorators import group_required

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
@group_required('admin')
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

@login_required
def incremental_search(request):
    query = request.GET.get('q', '')
    # Implement your search logic here
    # For example, search in a model called 'Item'
    results = []
    if query:
        results = list(Item.objects.filter(name__icontains=query).values('name', 'description'))
    return JsonResponse({'results': results})

def search_items(request):
    query = request.GET.get('q', '')
    items = Item.objects.filter(name__icontains=query)
    results = [{'name': item.name, 'link': item.link} for item in items]
    return JsonResponse(results, safe=False)