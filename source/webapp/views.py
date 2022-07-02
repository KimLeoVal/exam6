from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import RecordForm
from webapp.models import STATUS_CHOICES, Record


def index_view(request):
    records = Record.objects.filter(status='active')


    context = {"records": records}
    return render(request, "index.html", context)


def create_record(request):
    if request.method == "GET":
        form = RecordForm()
        return render(request, "create.html", {"statuses": STATUS_CHOICES, "form": form})
    else:
        form = RecordForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            author = form.cleaned_data.get("author")
            mail = form.cleaned_data.get("mail")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            new_record = Record.objects.create(author=author, mail=mail, status=status, description=description)
            return redirect("index_view")
        return render(request, "create.html", {"form": form})



# def update_task(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == "GET":
#         form = TaskForm(initial={
#             "title": task.title,
#             "description": task.description,
#             "status": task.status,
#             "done_at": task.done_at
#         })
#         return render(request, "update.html", {"form": form})
#     else:
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task.title = form.cleaned_data.get("title")
#             task.description = form.cleaned_data.get("description")
#             task.status = form.cleaned_data.get("status")
#             task.done_at = form.cleaned_data.get("done_at")
#             task.save()
#             return redirect("task_view", pk=task.pk)
#         return render(request, "update.html", {"form": form})
#
#

def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {'record': record})
    else:
        record.delete()
        return redirect("index_view")

