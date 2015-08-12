from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.auth.decorators import login_required

from blog.models import Entry
from blog.feeds import LatestEntries, LatestEntriesAtom
from flatpages.sitemaps import FlatPageSitemap

archive_common = {
    'queryset': Entry.objects.filter(is_public=True),
    'date_field': 'date',
}

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^strategchen/', include('strategchen.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

# Debug? Serve static files!
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#           {
#            'document_root': settings.PRJ_DIR+'/static',
#            'show_indexes': True
#       }
#        ),
#        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    )

# MarkItUp
if 'markitup' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^markitup/', include('markitup.urls')),
    )

# Robots
if 'robots' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^robots.txt$', include('robots.urls')),
    )

# Flatblocks
if 'flatblocks' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^flatblocks/', include('flatblocks.urls')),
    )

# Registration
if 'django.contrib.auth' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^login/$', 'django.contrib.auth.views.login'),
        (r'^logout/$', 'django.contrib.auth.views.logout'),
    )

# Sitemaps
if 'django.contrib.sitemaps' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
            'sitemaps': {
                'flatpages': FlatPageSitemap,
                'blog': GenericSitemap(archive_common, priority=0.4),
            } }
        ),
    )

# Feeds
if 'django.contrib.syndication' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^feeds/atom/$', LatestEntriesAtom()),
        (r'^feeds/rss/$', LatestEntries()),
    )

# Blog
if 'blog' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^blog/', include('blog.urls')),
    )

# / -> Blog, Favicon, ...
urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'redirect_to', {'url': '/blog/', 'permanent': False, }),
    (r'^favicon.ico$', 'redirect_to', {'url': None, 'permanent': True, }),
)

