from django.contrib import admin
from .models import Authentication, Admin, Manager, Employee


# Register your models here.
admin.site.register(Authentication)
admin.site.register(Admin)
admin.site.register(Manager)
admin.site.register(Employee)