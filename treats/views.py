from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Treat
from .forms import TreatForm
from .aws import upload_to_s3


def treat_list(request):
    treats = Treat.objects.all()
    return render(request, 'treats/list.html', context={'treats': treats})


def treat_detail(request, pk):
    treat = get_object_or_404(Treat, pk=pk)
    return render(request, 'treats/detail.html', context={'treat': treat})


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
    treat = get_object_or_404(Treat, pk=pk)
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
    treat = get_object_or_404(Treat, pk=pk)
    if request.method == "POST":
        treat.delete()
        messages.success(request, 'Deleted treat')
        return redirect('treats:treat_list')
    return render(request, 'treats/delete.html', context={"treat": treat})
