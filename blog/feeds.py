from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed

from blog.models import Entry

class LatestEntries(Feed):

	title = "strategchen Blog"
	author_name = "strategchen"
	author_email = "info@strategchen.com"
	description = "Neues im strategchen Blog"
	description_template = 'feeds/description.html'
	link = '/'

	def items(self):
		return Entry.objects.filter(is_public=True).order_by('-date')[:5]

	def item_pubdate(self, obj):
		return obj.date

class LatestEntriesAtom(LatestEntries):
	feed_type = Atom1Feed
	subtitle = LatestEntries.description
