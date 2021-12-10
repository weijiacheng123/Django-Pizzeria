from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

from django.shortcuts import render, redirect
from pizzas.forms import CommentForm
from .models import Pizza, Topping, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    # get post may on interview
    return render(request, 'pizzas/index.html')


def pizza1(request):
    pizza1 = Pizza.objects.filter(owner=request.user).order_by('date_added')

    context = {'pizza1':pizza1}

    return render(request, 'pizzas/pizza1.html', context)



def pizza2(request, pizza2_id):
    pizza2 = Pizza.objects.get(id=pizza2_id)

    toppings = pizza2.topping_set.all()
    comments = pizza2.comment_set.all()

    context = {'pizza':pizza1, 'toppings':toppings}
    context = {'pizza':pizza1, 'comments':comments}

    return render(request, 'pizzas/pizza2.html', context)


@login_required
def new_comment(request, pizza2_id):
    pizza2 = Pizza.objects.get(id=pizza2_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza2 = pizza2
            new_comment.save()

            return redirect('pizzas:pizza2', pizza2_id=pizza2_id)
    
    context = {'form':form, 'pizza2':pizza2}
    return render(request, 'pizzas/new_comment.html', context)

@login_required
def edit_comment(request, comment_id):
    """Edit an existing entry."""
    comment = Comment.objects.get(id=comment_id)
    topping = comment.pizza2

    if topping.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # this argument teills Django to create the form prefilled
        # with information from the exiting entry object.
        form = CommentForm(instance=comment_id)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza2', pizza2_id=pizza2.id)
    context = {'entry':comment, 'topping':topping, 'form':form}
    return render(request, 'pizzas/edit_comment.html', context)