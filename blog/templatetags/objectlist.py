from django import template
from django.db.models import get_model

register = template.Library()

class ObjectNode(template.Node):

	def __init__(self, var_name, app_label, model):
		self.entries = []
		self.var_name = var_name
		try:
			self.entries = get_model(app_label, model).objects.all()
		except:
			pass

	def render(self, context):
		context[self.var_name] = self.entries
		return ''

@register.tag(name="get_object_list")
def do_object_list(parser, token):
	try:
		tag_name, app_label, model, trash, var_name = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "%r tag requires 4 argument style" % token.contents[0]
	return ObjectNode(var_name, app_label, model)
