from django.contrib import admin
from devGuardN.models import Poll
from devGuardN.models import Choice

# Register your models here.
#default way to register a model
#admin.site.register(Poll)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
 
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question','pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
	  
admin.site.register(Poll, PollAdmin)