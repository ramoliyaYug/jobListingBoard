from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Job, Application
from .forms import ApplicationForm


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        # Only show published jobs
        queryset = Job.objects.filter(status='PUBLISHED')

        # Search by title or company
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(company__icontains=search_query)
            )

        # Filter by job type
        job_type = self.request.GET.get('job_type', '')
        if job_type:
            queryset = queryset.filter(job_type=job_type)

        # Filter by location
        location = self.request.GET.get('location', '')
        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['job_type'] = self.request.GET.get('job_type', '')
        context['location'] = self.request.GET.get('location', '')
        context['job_type_choices'] = Job.JOB_TYPE_CHOICES
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_queryset(self):
        # Only show published jobs
        return Job.objects.filter(status='PUBLISHED')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm()
        return context


class ApplicationView(View):
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk, status='PUBLISHED')
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            # Check if applicant already applied
            existing_app = Application.objects.filter(
                job=job,
                email=form.cleaned_data['email']
            ).first()

            if existing_app:
                messages.error(request, 'You have already applied for this position.')
                return redirect('job_detail', pk=pk)

            application = form.save(commit=False)
            application.job = job
            application.save()

            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job_detail', pk=pk)
        else:
            context = {
                'job': job,
                'form': form,
            }
            return render(request, 'jobs/job_detail.html', context)
