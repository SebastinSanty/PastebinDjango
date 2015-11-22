from django.contrib import admin

# Register your models here.
from .forms import PastebinForm
from .models import Pastebin

class PastebinAdmin(admin.ModelAdmin):
	list_display = ["pasteurl"]
	form = PastebinForm
	#class Meta:
	#	model = Pastebin


admin.site.register(Pastebin, PastebinAdmin)