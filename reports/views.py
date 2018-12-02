from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


from .forms import ReportForm


class ReportView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': ReportForm()
        }
        return render(request, 'reports/index.html', context)

    def post(self, request, *args, **kwargs):
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user_id = request.user_id
            report.save()
            return render(request, 'reports/index.html', {'form': form})


report = ReportView.as_view()
