from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Treat
from .forms import TreatForm


def treat_list(request):
    treats = Treat.objects.all()
    return render(request, 'treats/list.html', context={'treats': treats})


def treat_detail(request, pk):
    treat = get_object_or_404(Treat, pk=pk)
    return render(request, 'treats/detail.html', context={'treat': treat})


def treat_new(request):
    form = TreatForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Added treat')
        return redirect('treats:treat_list')
    return render(request, 'treats/form.html', context={"form": form})


def treat_edit(request, pk):
    treat = get_object_or_404(Treat, pk)
    form = TreatForm(request.POST or None, instance=treat)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated treat')
        return redirect('treats:treat_list')
    return render(request, 'treats/form.html', context={"treat": treat,
                                                              "form": form})


def treat_delete(request, pk):
    treat = get_object_or_404(Treat, pk)
    if request.method == "POST":
        treat.delete()
        messages.success(request, 'Deleted treat')
        return redirect('treats:treat_list')
    return render(request, 'treats/delete.html', context={"treat": treat})
