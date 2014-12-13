from django import template

from urllib2 import urlopen
import feedparser
import datetime

register = template.Library()


class FeedParserNode(template.Node):

	def __init__(self, url, var_name):
		self.url = url
		self.entries = []
		self.var_name = var_name
		try: 
			data = urlopen(url).read()
			feed = feedparser.parse(data)
			for entry in feed.entries:
				date = entry['updated_parsed']
				entry['date'] = datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5])
				self.entries.append(entry)
		except Exception:
			pass

	def render(self, context):
		context[self.var_name] = self.entries
		return ''

@register.tag(name="get_feed")
def do_list_topartists(parser, token):
	try:
		tag_name, url, trash, var_name = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "%r tag requires 3 argument style" % token.contents[0]
	return FeedParserNode(url, var_name)
