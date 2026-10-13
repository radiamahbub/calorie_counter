from django.shortcuts import render

# Create your views here.

def dashboard(request):

    return render(request, 'tracker/dashboard.html')




def profile_add(request):

    return render(request, 'tracker/profile_add.html')

def profile_list(request):

    return render(request, 'tracker/profile_list.html')

def profile_update(request):

    return render(request, 'tracker/profile_update.html')

def profile_delete(request):

    return render(request, 'tracker/profile_delete.html')





def calorie_consume_list(request):

    return render(request, 'tracker/calorie_consume_list.html')

def calorie_consume_add(request):

    return render(request, 'tracker/calorie_consume_add.html')

def calorie_consume_update(request):

    return render(request, 'tracker/calorie_consume_update.html')

def calorie_consume_delete(request):

    return render(request, 'tracker/calorie_consume_delete.html')