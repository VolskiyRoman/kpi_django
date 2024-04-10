from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from .forms import EditUserForm, OrderForm, ReviewForm
from .models import User, Order, Review

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateUserForm()
            return render(request, 'create_user.html', {'form': form})
    else:
        form = CreateUserForm()
    return render(request, 'create_user.html', {'form': form})


def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_page', user_id=user_id)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})


def user_page(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return HttpResponse(status=200)
    context = {'user': user}
    return render(request, 'user_page.html', context)


def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user.delete()
        return redirect('create_user')
    except User.DoesNotExist:
        return HttpResponseNotFound("User not found")


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'order_detail.html', context)


def mark_order_as_completed(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.completed = True
    order.save()
    return redirect('order_detail', order_id=order_id)


def create_review(request, user_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            rating = form.cleaned_data['rating']
            reviewer_id = form.cleaned_data['reviewer'].id
            user_id = user_id

            reviewer = User.objects.get(pk=reviewer_id)
            user = User.objects.get(pk=user_id)

            review = Review.objects.create(text=text, rating=rating, reviewer=reviewer, user=user)
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', {'review': review})