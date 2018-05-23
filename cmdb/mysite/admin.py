from django.contrib import admin

# Register your models here.

from . import models


class CMDBAdmin(admin.ModelAdmin):

    search_fields = ('host', 'team', 'func', 'operation')

    list_display = ('host', 'port', 'team', 'func', 'operation', 'update_date')

    def get_queryset(self, request):
        qs = super(CMDBAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(property=request.user)


admin.site.register(models.CMDB, CMDBAdmin)
