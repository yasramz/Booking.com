from django.contrib import admin
from user.models import User, Profile, BankInfo

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(BankInfo)

