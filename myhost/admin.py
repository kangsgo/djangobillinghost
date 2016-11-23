from django.contrib import admin
from .models import PersonHost,Personblling
# Register your models here.

class PersonHostAdmin(admin.ModelAdmin):
	"""docstring for PersonHost"""
	list_display=('id','user','come_time','create_date','was_come_time')
	list_filter = ['create_date']
	search_fields=['user']

admin.site.register(PersonHost,PersonHostAdmin)

class PersonBillAdmin(admin.ModelAdmin):
	"""docstring for PersonHost"""
	list_display=('id','user','billingstatus','billingmoney')
	search_fields=['user']

admin.site.register(Personblling,PersonBillAdmin)