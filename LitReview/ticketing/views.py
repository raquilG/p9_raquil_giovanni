from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms
from . import models
from django.contrib import messages


@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'ticketing/create_ticket.html', context={'ticket_form': ticket_form})


@login_required
def create_review(request, ticket_id):
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            ticket = models.Ticket.objects.filter(id=ticket_id)[0]
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('home')

    return render(request, 'ticketing/create_review.html', context={'review_form': review_form})


@login_required
def create_ticket_and_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form
    }

    return render(request, 'ticketing/create_ticket_and_review.html', context)


@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    posts = list(tickets) + list(reviews)
    posts.sort(key=lambda x: x.time_created, reverse=True)
    context = {'posts': posts}

    return render(request, 'ticketing/posts.html', context)


@login_required
def post_update(request, post_type, post_id):
    if post_type == "ticket":
        post = models.Ticket.objects.get(id=post_id)
    else:
        post = models.Review.objects.get(id=post_id)

    if request.method == "POST":
        print(request.FILES)
        if post_type == "ticket":
            form = forms.TicketForm(request.POST, request.FILES, instance=post)
        else:
            form = forms.ReviewForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        if post_type == "ticket":
            form = forms.TicketForm(instance=post)
        else:
            form = forms.ReviewForm(instance=post)

    context = {
        "form": form,
        "post": post
    }
    return render(request, 'ticketing/post_update.html', context)


@login_required
def post_delete(request, post_type, post_id):
    if post_type == "ticket":
        post = models.Ticket.objects.get(id=post_id)
    else:
        post = models.Review.objects.get(id=post_id)
    context = {"post": post}

    if request.method == "POST":
        post.delete()
        messages.add_message(request,
                             messages.INFO,
                             "le post a été supprimé avec succès!")
        return redirect('posts')

    return render(request, 'ticketing/post_delete.html', context)
