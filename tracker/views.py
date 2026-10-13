from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from tracker.models import *
from tracker.forms import *


# Dashboard ---------------------------------------------------------------------------------------


@login_required
def dashboard(request):

    try:
        bmr = request.user.user_profile.bmr

    except:
        bmr = 0

        messages.warning(request, "Please update your profile first")

        return redirect("profile_update")

    data = ConsumedCalorieModel.objects.filter(user=request.user).aggregate(
        total_calorie=Sum("consumed_calorie")
    )

    total_consumed_calorie = data["total_calorie"] or 0
    remaining_calorie = bmr - total_consumed_calorie
    if total_consumed_calorie > bmr:

        suggestion = "Fatty"

    else:

        suggestion = "Cutey"

    context = {
        "title": "Dashboard",
        "bmr": round(bmr, 2),
        "total_consumed_calorie": round(total_consumed_calorie, 2),
        "remaining_calorie": round(remaining_calorie, 2),
        "suggestion": suggestion,
    }

    return render(request, "tracker/dashboard.html", context)


# Profile ---------------------------------------------------------------------------------------


@login_required
def profile(request):

    return render(request, "tracker/profile.html")


@login_required
def profile_update(request):

    current_user = request.user

    try:
        profile_data = request.user_profile

    except:

        profile_data = None

    form = UpdateProfileForm(instance=profile_data)

    if request.method == "POST":

        form = UpdateProfileForm(request.POST, request.FILES, instance=profile_data)

        if form.is_valid():

            form = form.save(commit=False)

            form.user = current_user

            form.save()

            return redirect("profile")

    context = {
        "title": "Profile",
        "form_title": "Profile Update Page",
        "form_btn": "Update",
        "form": form,
    }

    return render(request, "form_base.html", context)


def profile_add(request):

    return render(request, "tracker/profile_add.html")


def profile_list(request):

    return render(request, "tracker/profile_list.html")


def profile_delete(request):

    return render(request, "tracker/profile_delete.html")


# Calorie Consumed ---------------------------------------------------------------------------------


@login_required
def calorie_consume_list(request):

    try:
        bmr = request.user.user_profile.bmr
    
    except:
        bmr = 0
    
        messages.warning(request, "Please update your profile first")
    
        return redirect("profile_update")

    consumed_calorie = ConsumedCalorieModel.objects.filter(user=request.user)

    search_data = request.GET.get('search', '')

    if search_data:

        consumed_calorie = ConsumedCalorieModel.objects.filter(
            Q(user = request.user) &
            Q(item_name__icontains = search_data))

    context = {
        "consumed_calorie": consumed_calorie,
        'search_data':search_data
        }

    return render(request, "tracker/calorie_consume_list.html", context)


@login_required
def calorie_consume_add(request):

    form = ConsumedCalorieForm()

    if request.method == "POST":

        form = ConsumedCalorieForm(request.POST)

        if form.is_valid():

            form = form.save(commit=False)

            form.user = request.user

            form.save()

            return redirect("calorie_consume_list")

    context = {
        "title": "Add Consumed Calorie",
        "form_title": "Add Consumed Calorie Data",
        "form_btn": "Add Calorie",
        "form": form,
    }

    return render(request, "form_base.html", context)


@login_required
def calorie_consume_update(request, c_id):

    data = get_object_or_404(ConsumedCalorieModel, id=c_id)

    form = ConsumedCalorieForm(instance=data)

    if request.method == "POST":

        form = ConsumedCalorieForm(request.POST, instance=data)

        if form.is_valid():

            form = form.save(commit=False)

            form.user = request.user

            form.save()

            return redirect("calorie_consume_list")

    context = {
        "title": "Update Consumed Calorie",
        "form_title": "Update Consumed Calorie Data",
        "form_btn": "Update Calorie",
        "form": form,
    }

    return render(request, "form_base.html", context)


@login_required
def calorie_consume_delete(request, c_id):

    get_object_or_404(ConsumedCalorieModel, id=c_id).delete()

    return redirect("calorie_consume_list")
