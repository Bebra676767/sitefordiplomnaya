from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application
from .forms import ApplicationForm

@login_required
def my_applications(request):
    applications = Application.objects.filter(user=request.user).select_related('course')
    return render(request, 'applications.html', {'applications': applications})

@login_required
def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, 'Заявка успешно создана!')
            return redirect('my_applications')
    else:
        form = ApplicationForm()
    return render(request, 'create_application.html', {'form': form})

@login_required
def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    return render(request, 'application_detail.html', {'application': application})