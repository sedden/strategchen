from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from reversion.admin import VersionAdmin

from markitup.widgets import MarkItUpWidget

class CustomFlatPageAdmin(VersionAdmin, FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=MarkItUpWidget())
        return super(CustomFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)
