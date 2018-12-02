from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


from .forms import ShiftForm


class ShiftView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': ShiftForm()
        }
        return render(request, 'shifts/index.html', context)

    def post(self, request, *args, **kwargs):
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.user_id = request.user_id
            shift.save()
            return render(request, 'shifts/index.html', {'form': form})


shift = ShiftView.as_view()
