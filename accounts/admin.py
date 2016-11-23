from django.contrib import admin
from .models import UserProfile,Deposit

# Register your models here.
admin.site.register(UserProfile)


class DepositCounpon(admin.ModelAdmin):
	list_display=('counpon','counponactive')

admin.site.register(Deposit,DepositCounpon)