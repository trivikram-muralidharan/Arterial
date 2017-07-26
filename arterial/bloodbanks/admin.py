from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Donor, Hospital, Bloodbank, BloodReq
# Register your models here.


admin.site.register(Donor)
admin.site.register(Hospital)
admin.site.register(Bloodbank)
admin.site.register(BloodReq)
