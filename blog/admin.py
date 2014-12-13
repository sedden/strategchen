from django.contrib import admin

from blog.models import Entry
from markitup.widgets import MarkItUpWidget
from reversion.admin import VersionAdmin

class EntryAdmin(VersionAdmin):

	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name == 'body':
			return db_field.formfield(widget=MarkItUpWidget())
		return super(EntryAdmin, self).formfield_for_dbfield(db_field, **kwargs)

	prepopulated_fields = {
		'slug': ('title',)
	}

	fieldsets = (
		(None, { 'fields': ('title', 'date', 'slug', 'body', 'tags') }),
		('Erweitert', {
			'classes': ('collapse',),
			'fields': ('excerpt', 'enable_comments', 'is_public' )
		} ),
	)

	list_display = ('title', 'date', 'tags', 'is_public')
	list_filter = ('is_public','date')


	def has_change_permission(self, request, obj=None):
		"""
		Called from the individual object editing page, to ensure the
		user is allowed to edit that object.

		Returns ``True`` if the user has permission for change the
		entry, otherwise returns ``False``.
		"""
		has_class_permission = super(EntryAdmin, self).has_change_permission(request, obj)
		if not has_class_permission:
			return False
		if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
			return False
		return True

	def queryset(self, request):
		"""
		Filter the entries based on ``request.user``. This only
		affects the entries shown in the list view.
		"""
		if request.user.is_superuser:
			return Entry.objects.all()
		return Entry.objects.filter(author=request.user)

	def save_model(self, request, obj, form, change):
		"""
		Automatically fill in the author field on creation.
		"""
		if not change:
			obj.author = request.user
		super(EntryAdmin, self).save_model(request, obj, form, change)

admin.site.register(Entry, EntryAdmin)
