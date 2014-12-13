from django.conf import settings
from django.conf.urls.defaults import *

from blog.models import Entry

archive_common = {
    'queryset': Entry.objects.filter(is_public=True),
    'date_field': 'date',
}

# Blog
urlpatterns = patterns('django.views.generic',
    (r'^(?P<year>\d{4})/$', 'date_based.archive_year',
        dict(archive_common, make_object_list=True),
    ),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'date_based.archive_month',
        dict(archive_common, month_format='%m'),
    ),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'date_based.archive_day',
        dict(archive_common, month_format='%m', day_format='%d' ),
    ),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>.*)/$', 'date_based.object_detail',
        dict(archive_common, queryset=Entry.objects.all(), month_format='%m', day_format='%d', slug_field='slug', ),
    ),
    (r'^page/(?P<page>\w)/$', 'list_detail.object_list',
        { 'queryset':archive_common['queryset'], 'paginate_by':5,  },
    ),
    (r'^$', 'list_detail.object_list',
        { 'queryset':archive_common['queryset'], 'paginate_by':5, 'page':0 },
    ),
)

# Tagging
if 'tagging' in settings.INSTALLED_APPS:
    urlpatterns += patterns('tagging.views',
        (r'^(?P<tag>.*)/$', 'tagged_object_list', {
            'queryset_or_model': Entry,
            'related_tags': True,
            'template_name': 'blog/entry_list_tags.html',
     } ),
    )
