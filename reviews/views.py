from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import Application
from .models import Review
from .forms import ReviewForm

@login_required
def create_review(request, application_id):
    application = get_object_or_404(Application, id=application_id, user=request.user)
    
    if application.status != 'completed':
        messages.error(request, 'Отзыв можно оставить только после завершения обучения')
        return redirect('my_applications')
    
    if Review.objects.filter(application=application).exists():
        messages.warning(request, 'Вы уже оставили отзыв для этой заявки')
        return redirect('my_applications')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.application = application
            review.save()
            messages.success(request, 'Спасибо за ваш отзыв!')
            return redirect('my_applications')
    else:
        form = ReviewForm()
    
    return render(request, 'create_review.html', {
        'form': form,
        'application': application
    })