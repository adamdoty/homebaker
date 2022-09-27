from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Treat, Note
from .forms import TreatForm, NoteForm
from .aws import upload_to_s3


def treat_list(request):
    treats = Treat.objects.all()
    return render(request, 'treats/list.html', context={'treats': treats})


def treat_detail(request, pk):
    treat = get_object_or_404(Treat, pk=pk)
    notes = treat.notes.filter(treat_id=treat.id)
    return render(request, 'treats/detail.html', context={'treat': treat, 'notes': notes})


@login_required
def treat_new(request):
    if request.method == 'POST':
        form = TreatForm(data=request.POST)

        if form.is_valid():
            file = request.FILES["img_upload"]
            cover_img_url = upload_to_s3(file)

            treat = form.save(commit=False)
            treat.user = request.user
            treat.cover_img = cover_img_url
            treat.save()
            messages.success(request, 'Added treat')
            return redirect('treats:treat_list')
    else:
        form = TreatForm()
    return render(request, 'treats/form.html', context={"form": form})


@login_required
def treat_edit(request, pk):
    treat = get_object_or_404(Treat, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TreatForm(instance=treat, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated treat')
            return redirect('treats:treat_list')
    else:
        form = TreatForm(instance=treat)

    return render(request, 'treats/form.html', context={"treat": treat,
                                                        "form": form})


@login_required
def treat_delete(request, pk):
    treat = get_object_or_404(Treat, pk=pk, user=request.user)
    if request.method == "POST":
        treat.delete()
        messages.success(request, 'Deleted treat')
        return redirect('treats:treat_list')
    return render(request, 'treats/delete.html', context={"treat": treat})


@login_required
def treat_note(request, pk):
    treat = get_object_or_404(Treat, id=pk)
    note = None
    if request.method == 'POST':
        form = NoteForm(data=request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.treat = treat
            note.save()
            messages.success(request, 'Added note')
            # issue with redirecting here
            return redirect('treats:treat_detail', treat_id=treat.id)
    else:
        form = NoteForm()
    return render(request, 'treats/note.html', context={'treat': treat, 'form': form, 'note': note})


@login_required
def treat_note_delete(request, treat_pk, note_pk):
    treat = get_object_or_404(Treat, id=treat_pk)
    note = get_object_or_404(Note, id=note_pk)
    if request.method == "POST":
        note.delete()
        messages.success(request, 'Deleted note')
        return redirect('treats:treat_detail')
    return render(request, 'treats/delete.html', context={"treat": treat, "note": note})
