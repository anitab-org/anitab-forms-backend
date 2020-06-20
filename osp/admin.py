from django.contrib import admin

from osp.models import *

admin.site.register(UserInformation)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Checkbox)
admin.site.register(Dropdown)
admin.site.register(Paragraph)
admin.site.register(ShortAnswer)
admin.site.register(Date)
admin.site.register(Time)
admin.site.register(FileUpload)
