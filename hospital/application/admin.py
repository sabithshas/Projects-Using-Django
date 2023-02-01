from django.contrib import admin
from .models import Doctorregistration
from .models import Patientregistration
from .models import Booking
from .models import Medicine
from .models import Leave
# Register your models here.
admin.site.register (Doctorregistration)
admin.site.register (Patientregistration)
admin.site.register (Booking)
admin.site.register (Medicine)
admin.site.register (Leave)