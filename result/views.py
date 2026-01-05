from django.shortcuts import render, redirect
from .models import Result
from .forms import ResultForm

def result_list(request):
    results = Result.objects.all()
    return render(request, 'result/result_list.html', {'results': results})

def result_create(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result_list')
    else:
        form = ResultForm()
    return render(request, 'result/result_form.html', {'form': form})
