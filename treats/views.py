from datetime import datetime

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from .models import Treat, Note, Coupon, Event
from .forms import TreatForm, NoteForm, CouponForm, TreatRequestForm
from .aws import upload_to_s3
from .utils import Calendar


# -------- TEST FUNCTION --------
def is_baker(user):
    return user.profile.is_baker_user


def get_date(requested_day):
    if requested_day:
        year, month = (int(x) for x in requested_day.split('-'))
        return datetime(year, month, day=1)
    else:
        return datetime.today()


# ------------------------------- VIEWS -------------------------------
def treat_list(request):
    treats = get_list_or_404(Treat, is_recipient_request=False)
    if request.user.is_anonymous is False:
        redeemable_coupons = request.user.coupon_set.filter(treat=None)
        context = {'treats': treats, 'redeemable_coupons': redeemable_coupons}
    else:
        context = {'treats': treats}
    return render(request, 'treats/list.html', context=context)


def treat_detail(request, pk):
    treat = get_object_or_404(Treat, pk=pk)
    notes = treat.notes.filter(treat_id=treat.id)
    return render(request, 'treats/treat-detail.html', context={'treat': treat, 'notes': notes})


@user_passes_test(is_baker)
@login_required
def treat_new(request):
    if request.method == 'POST':
        form = TreatForm(data=request.POST)

        if form.is_valid():
            treat = form.save(commit=False)
            treat.user = request.user

            file = request.FILES.get("img_upload")
            if file is not None:
                cover_img_url = upload_to_s3(file)
                treat.cover_img = cover_img_url

            treat.save()
            messages.success(request, 'Added treat')
            return redirect('treats:treat_list')
    else:
        form = TreatForm()
    return render(request, 'treats/form.html', context={"form": form})


@user_passes_test(is_baker)
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


@user_passes_test(is_baker)
@login_required
def treat_delete(request, pk):
    treat = get_object_or_404(Treat, pk=pk, user=request.user)
    if request.method == "POST":
        treat.delete()
        messages.success(request, 'Deleted treat')
        return redirect('treats:treat_list')
    return render(request, 'treats/delete.html', context={"treat": treat})


@user_passes_test(is_baker)
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
            return redirect('treats:treat_detail', pk=treat.id)
    else:
        form = NoteForm()
    return render(request, 'treats/note.html', context={'treat': treat, 'form': form, 'note': note})


@user_passes_test(is_baker)
@login_required
def treat_note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    treat = note.treat
    if request.method == 'POST':
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated note')
            return redirect('treats:treat_detail', pk=treat.id)
    else:
        form = NoteForm(instance=note)

    return render(request, 'treats/note.html', context={"treat": treat, "note": note, "form": form})


@user_passes_test(is_baker)
@login_required
def treat_note_delete(request, pk):
    note = get_object_or_404(Note, id=pk)
    treat = note.treat
    if request.method == "POST":
        note.delete()
        messages.success(request, 'Deleted note')
        return redirect('treats:treat_detail', pk=treat.id)

    return render(request, 'treats/delete.html', context={"treat": treat, "note": note})


# maybe add a decorator here that requires the user have a redeemable coupon
@login_required
def treat_request(request):
    """
    After submitting a treat request form, the user gets redirected to the my coupons view,
    they can see the coupon status has changed to IN REVIEW

    When a treat request is submitted it
    """
    if request.method == "POST":

        form = TreatRequestForm(data=request.POST)

        if form.is_valid():
            treat = form.save(commit=False)
            treat.user = request.user
            treat.is_recipient_request = True

            treat.save()
            messages.success(request, 'Requested treat')
            return redirect("treats:redeem_coupon", pk=treat.id)
    else:
        form = TreatRequestForm()
    return render(request, 'treats/treat-request.html', context={"form": form})


@user_passes_test(is_baker)
@login_required
def treat_request_approval(request):
    treat_requests = get_list_or_404(Treat, is_recipient_request=True)
    return render(request, 'treats/treat-request-approval.html', context={'treat_requests': treat_requests})


@user_passes_test(is_baker)
@login_required
def coupon_tracker(request):
    d = get_date(request.GET.get('day', None))
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    coupons = get_list_or_404(Coupon)
    return render(request, 'coupons/tracker.html', context={'coupons': coupons, 'calendar': mark_safe(html_cal)})


@user_passes_test(is_baker)
@login_required
def coupon_detail(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    return render(request, 'coupons/coupon-detail.html', context={'coupon': coupon})


@user_passes_test(is_baker)
@login_required
def coupon_new(request):
    if request.method == 'POST':
        form = CouponForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Added coupon')
            return redirect('treats:coupon_tracker')
    else:
        form = CouponForm()
    return render(request, 'coupons/coupon-form.html', context={'form': form})


@user_passes_test(is_baker)
@login_required
def coupon_edit(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    if request.method == 'POST':
        form = CouponForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Coupon updated')
            return redirect('treats:coupon_detail')
    else:
        form = CouponForm(instance=coupon)
    return render(request, 'coupons/coupon-detail.html', {'coupon': coupon, 'form': form})


@user_passes_test(is_baker)
@login_required
def coupon_delete(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    if request.method == 'POST':
        coupon.delete()
        messages.success(request, 'Coupon deleted')
        return redirect('treats:coupon_tracker')
    return render(request, 'treats/delete.html', context={'coupon': coupon})


@login_required
def my_coupons(request):
    coupons = Coupon.objects.filter(recipient_id=request.user.id)
    # coupons = get_list_or_404(Coupon, recipient_id=request.user.id)
    return render(request, 'coupons/my-coupons.html', context={'coupons': coupons})


@login_required
def redeem_coupon(request, pk):
    treat = get_object_or_404(Treat, pk=pk)
    # get the first redeemable coupon
    coupon = request.user.coupon_set.filter(treat=None)[0]
    coupon.treat = treat
    coupon.save()
    return redirect('treats:my_coupons')


def register(request):
    """Register a new user"""
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('treats:treat_list')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', context={'form': form})
