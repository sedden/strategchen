from django.contrib.sitemaps import FlatPageSitemap

class FlatPageSitemap(FlatPageSitemap):

    def priority(self, item):

        if item.url == u'/blog/':
            return 1.0

        return 0.8
	
