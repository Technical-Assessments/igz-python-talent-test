from django.contrib import admin
from .models import Matrix, String

# Register your models here.

class MatrixAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'created', 'matrix', 'output_data', 'output_type']
    list_filter = ['output_type']

    class Meta:
        model = Matrix



class StringAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'created', 'string', 'output_data']
    list_filter = ['created']

    class Meta:
        model = String



admin.site.register(Matrix, MatrixAdmin)
admin.site.register(String, StringAdmin)
