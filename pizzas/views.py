from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from pizzas.forms import CommentForm, ImageForm
from .models import Pizza, Topping, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # get post may on interview
    return render(request, 'pizzas/index.html')


def pizza1(request):
    pizza1 = Pizza.objects.order_by('date_added')

    context = {'pizza1':pizza1}

    return render(request, 'pizzas/pizza1.html', context)


def pizza2(request, pizza2_id):
    pizza2 = Pizza.objects.get(id=pizza2_id)

    toppings = pizza2.topping_set.all()
    comments = pizza2.comment_set.all()
    images  = pizza2.image_set.all()

    if request.method != 'POST':
        form = ImageForm()
    else:
        form = ImageForm(data=request.POST)

    context = {'pizza2':pizza2, 'toppings':toppings, 'comments':comments, 'images':images, 'form':form}
    #context = {'pizza':pizza2, 'comments':comments}

    return render(request, 'pizzas/pizza2.html', context)


#@login_required
def new_comment(request, pizza2_id):
    pizza2 = Pizza.objects.get(id=pizza2_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza2
            new_comment.save()

            return redirect('pizzas:pizza2', pizza2_id=pizza2_id)
    
    context = {'form':form, 'pizza2':pizza2}
    return render(request, 'pizzas/new_comment.html', context)

