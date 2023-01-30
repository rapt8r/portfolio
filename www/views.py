import datetime
import os

from django.http import FileResponse
from django.views.generic import TemplateView
from .models import Skill, Project, Visitor, Entry
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class TrackVisitorsMixin:
    def track(self, request, *args, **kwargs):
        # Check if visitor is registered in DB
        new_entry = Entry()
        try:
            # Visitor already exists
            existing_visitor = Visitor.objects.get(ip=request.META['REMOTE_ADDR'])
            new_entry.set_info(request, existing_visitor)
            new_entry.save()
        except Visitor.DoesNotExist:
            # Visitor doesn't exist
            new_visitor = Visitor(ip=request.META['REMOTE_ADDR'], source=request.GET.get('source', ''))
            new_visitor.clean()
            new_visitor.save()
            new_entry.set_info(request, new_visitor)
            new_entry.save()


class IndexPage(TrackVisitorsMixin, TemplateView):
    template_name = 'www/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['skills'] = Skill.objects.all().filter(visible=True)
        context['projects'] = Project.objects.all()
        self.track(request)
        return self.render_to_response(context)


class StatsPage(TrackVisitorsMixin, TemplateView):
    template_name = 'www/stats.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        all_entries = Entry.objects.all()
        all_visitors = Visitor.objects.all()
        context['today'] = datetime.datetime.now()
        # Entries
        context['all_entries_today'] = all_entries.filter(datetime__date=today).count()
        context['all_entries_yesterday'] = all_entries.filter(datetime__date=yesterday).count()
        context['index_entries_today'] = all_entries.filter(datetime__date=today, path='/').count()
        context['cv_entries_today'] = all_entries.filter(datetime__date=today, path='/download-cv/').count()
        try:
            context['all_entries_percent_change'] = int(
                ((context['all_entries_today'] / context['all_entries_yesterday']) - 1) * 100)
        except ZeroDivisionError:
            context['all_entries_percent_change'] = 'N/A'
        # Certificate
        context['all_certificate_checks'] = all_entries.filter(path="CheckingSDACertificate").count()
        context['today_certificate_checks'] = all_entries.filter(datetime__date=today,
                                                                 path="CheckingSDACertificate").count()
        try:
            context['all_entries_percent_change'] = int(
                ((context['all_entries_today'] / context['all_entries_yesterday']) - 1) * 100)
        except ZeroDivisionError:
            context['all_entries_percent_change'] = 'N/A'
        # Sources
        context['linkedin_visitors'] = all_visitors.filter(source='linkedin').count()
        context['linkedinmsg_visitors'] = all_visitors.filter(source='linkedinmsg').count()
        context['cv_visitors'] = all_visitors.filter(source='cv').count()
        context['olx_visitors'] = all_visitors.filter(source='olx').count()
        context['pracujpl_visitors'] = all_visitors.filter(source='pracujpl').count()
        context['na_visitors'] = all_visitors.filter(source='n/a').count()
        return self.render_to_response(context)


class Error404Page(TemplateView):
    template_name = 'www/404.html'
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class DownloadCVPage(TrackVisitorsMixin, TemplateView):
    template_name = 'www/download-cv.html'

    def get(self, request, *args, **kwargs):
        self.track(request)
        return super().get(self, request, *args, **kwargs)


class APIStats(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        today = datetime.date.today()
        all_entries = Entry.objects.all()
        yesterday = today - datetime.timedelta(days=1)
        data = {
            'date': datetime.datetime.now(),
            'all_entries_today': all_entries.filter(datetime__date=today).count(),
            'all_entries_yesterday': all_entries.filter(datetime__date=yesterday).count(),
            'index_entries_today': all_entries.filter(datetime__date=today, path='/').count(),
            'cv_entries_today': all_entries.filter(datetime__date=today, path='/download-cv/').count(),
        }
        return Response(data)

def OpenGraphPage(request):
    return FileResponse(open(os.getenv('OPEN_GRAPH_PATH'), 'rb'))
