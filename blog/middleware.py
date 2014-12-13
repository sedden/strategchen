from django.http import HttpResponseRedirect
import settings


class FeedburnerMiddleware(object):
    '''
    Redirect the user to a feedburner feed for basic feeds
    '''
    def process_request(self, request):
        r = request.path
        if not r in settings.FEEDBURNER_URLS:
            return None
        
        if request.META['HTTP_USER_AGENT'].startswith('FeedBurner'):
            return None
        else:
            return HttpResponseRedirect(settings.FEEDBURNER_URLS[r])
