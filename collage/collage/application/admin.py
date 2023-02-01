from django.contrib import admin
from .models import Add_hod
from .models import Add_teacher
from .models import Add_students
from .models import leave
from .models import notification
from .models import mark

from django.contrib.auth.models import User
# Register your models here.
admin.site.register (Add_hod)
admin.site.register (Add_teacher)
admin.site.register (Add_students)
admin.site.register (leave)
admin.site.register (notification)
admin.site.register (mark)
