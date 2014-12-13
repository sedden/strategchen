from django.db.models import TextField
from markdown import markdown

class MarkdownTextField(TextField):

	def __init__(self, *args, **kwargs):
		super(MarkdownTextField, self).__init__(*args, **kwargs)
    
	def contribute_to_class(self, cls, name):
		self._html_field = "%s_html" % name
		TextField(editable=False, blank=True, null=True).contribute_to_class(cls, self._html_field)
		super(MarkdownTextField, self).contribute_to_class(cls, name)

	def pre_save(self, model_instance, add):
		value = getattr(model_instance, self.attname)
		setattr(model_instance, self._html_field, markdown(value))
		return value
    
	def __unicode__(self):
		return self.attname
