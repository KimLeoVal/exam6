from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import RecordForm
from webapp.models import STATUS_CHOICES, Record


def index_view(request):
    if request.method == "GET":
        form = RecordForm()
        records = Record.objects.filter(status='active').order_by('-created_at')
        context = {"records": records, "form": form}
        return render(request, "index.html", context)



def create_record(request):
    if request.method == "GET":
        form = RecordForm()
        return render(request, "create.html", {"statuses": STATUS_CHOICES, "form": form})
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get("author")
            mail = form.cleaned_data.get("mail")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            new_record = Record.objects.create(author=author, mail=mail, description=description)
            return redirect("index_view")
        return render(request, "create.html", {"form": form})


def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "GET":
        form = RecordForm(initial={
            "author": record.author,
            "mail": record.mail,
            "description": record.description,
            "status": record.status,
        })
        return render(request, "update.html", {"form": form})
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.author = form.cleaned_data.get("author")
            record.mail = form.cleaned_data.get("mail")
            record.description = form.cleaned_data.get("description")
            record.save()
            return redirect("index_view")
        return render(request, "update.html", {"form": form})


#
#

def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {'record': record})
    else:
        record.delete()
        return redirect("index_view")
