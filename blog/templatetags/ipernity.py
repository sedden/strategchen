from django import template

from BeautifulSoup import BeautifulSoup, Tag
import re

register = template.Library()

@register.filter(name="iperlink")
def do_iperimage(value):

	'''detects iPernity static urls and creates clickable thumbnail for it'''

	soup = BeautifulSoup(value)
	iprl = re.compile('^(http://\w+\.ipernity\.com/\d+/\d+/\d+/\d+\.\w+\.)(75|100|240|500|560)(\.jpg)$')
	iprl_thumb = '500'
	iprl_zoom = '560'

        for img in soup.findAll('img', src=iprl ):

		match = iprl.match(img['src'])
		try:
			thumb = Tag(soup, 'img')
			thumb['alt'] = img['title']
			thumb['src'] = match.group(1)+iprl_thumb+match.group(3)

			link = Tag(soup, 'a')
			link['href'] = match.group(1)+iprl_zoom+match.group(3)
			link['rel'] = 'lightbox'
			link['title'] = img['title']
			link.insert(0, thumb)

			img.replaceWith(link)
		except:
			pass	
	
	return unicode(soup)

do_iperimage.is_safe = True
