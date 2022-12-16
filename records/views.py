from django.shortcuts import render, get_object_or_404, redirect
from records.models import Category, Log
from django.contrib.auth.decorators import login_required
from records.forms import LogForm

def list_categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "records/list.html", context)


# @login_required
# def list_details(request, id):
#     log_details = get_object_or_404(Category, id=id)
#     context = {"log_details": log_details}
#     return render(request, "records/detail.html", context)


@login_required
def category_details(request, category_name):
    category_name = category_name.capitalize()
    # category_object = Category.objects.get(name=cat)
    category = get_object_or_404(Category, name=category_name)
    context = {"category": category}
    return render(request, "records/detail.html", context)


@login_required
def log_event(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_categories")
    else:
        form = LogForm()

    context = {"form": form}

    return render(request, "records/log_event.html", context)
