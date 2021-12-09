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
    return render(request, 'MainApp/index.html')

@login_required
def pizza1(request):
    pizza1 = Pizza.objects.filter(owner=request.user).order_by('date_added')

    context = {'pizza1':pizza1}

    return render(request, 'pizzas/pizza.html', context)

@login_required
def pizza2(request, pizza2_id):
    pizza2 = Pizza.objects.get(id=pizza2_id)

    if topping.owner != request.user:
        raise Http404

    comments = pizza2.comment_set.all()

    context = {'pizza':pizza1, 'comments':comments}

    return render(request, 'pizzas/pizza2.html', context)

@login_required
def topping(request, pt_id):
    topping = Topping.objects.get(id=pt_id)

    context = {'topping':topping}

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

            return redirect('pizzas:topic', pizza2_id=pizza2_id)
    
    context = {'form':form, 'topping':topping}
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
            return redirect('pizzas:topping', pizza2_id=pizza2.id)
    context = {'entry':comment, 'topping':topping, 'form':form}
    return render(request, 'pizzas/edit_comment.html', context)