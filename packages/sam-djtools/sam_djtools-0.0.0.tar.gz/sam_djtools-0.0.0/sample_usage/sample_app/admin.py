from django.contrib import admin
from .models import Model1
from sam_tools.utils import DjangoUtils


class Model1Admin(admin.ModelAdmin):
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['site_url'] = DjangoUtils.site_url(request)
        res = super().render_change_form(request, context, add, change, form_url)
        return res


# Register your models here.
admin.site.register(Model1, Model1Admin)
