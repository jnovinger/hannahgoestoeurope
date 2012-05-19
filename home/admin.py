from django.contrib import admin
from models import Post, Donation, Section

class DonationAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'first_name', 'last_name', 'received', 'cleared', 'payment_type', 'get_sections')

admin.site.register(Post)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Section)
