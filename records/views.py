from django.shortcuts import render, get_object_or_404, redirect
from records.models import Category, Log
from django.contrib.auth.decorators import login_required
from records.forms import LogForm

def list_categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "records/list.html", context)


@login_required
def category_details(request, category_name):
    category_name = category_name.capitalize()
    category = get_object_or_404(Category, name=category_name)
    context = {"category": category}
    return render(request, "records/detail.html", context)


@login_required
def log_event(request, category_name=None):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_details", form.cleaned_data["category"].name)
    else:
        try:
            form = LogForm(initial={
                "category": get_object_or_404(Category, name=category_name),
                })
        except:
            form = LogForm()


    context = {"form": form}

    return render(request, "records/log_event.html", context)


@login_required
def edit_event(request, id):
    event = get_object_or_404(Log, id=id)
    if request.method == "POST" and "save" in request.POST:
        form = LogForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("category_details", event.category.name)
    elif request.method == "POST" and "delete" in request.POST:
        event.delete()
        return redirect("category_details", event.category.name)
    else:
        form = LogForm(instance=event)


    context = {
        "event": event,
        "form": form
    }

    return render(request, "records/edit.html", context)
