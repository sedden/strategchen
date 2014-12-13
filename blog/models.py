from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tagging.fields import TagField

from blog.fields import MarkdownTextField

class Entry(models.Model):
	
	title = models.CharField(_('title'), max_length=200)
	slug = models.SlugField(_('slug'), unique=True,
		help_text='Wird automatisch aus Titel erzeugt')
	date = models.DateTimeField(_('date/time submitted'))
	body = MarkdownTextField(_('content'))
	excerpt = MarkdownTextField(_('excerpt'), blank=True,
		help_text='Eine Kurzfassung vom Inhalt (SMS-Version)')

	enable_comments = models.BooleanField(_('enable comments'), default=True)
	is_public = models.BooleanField(_('is public'), default=False)

	tags = TagField()

	author = models.ForeignKey(User, editable=False, verbose_name=_('author'))

	class Meta:
		ordering = ['-date']
		verbose_name = 'Eintrag'
		verbose_name_plural = 'Eintraege'

	def get_absolute_url(self):
		return '/blog/%s/%s/' % ( self.date.strftime("%Y/%m/%d"), self.slug)

	def get_next_public_by_date(self):
		return self.get_next_by_date(is_public=True)

	def get_previous_public_by_date(self):
		return self.get_previous_by_date(is_public=True)

	def __unicode__(self):
		return u'%s' % self.title

