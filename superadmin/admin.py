from django.contrib import admin
from .models import Category,CourseDetails,DaysAccess,Payment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status")

admin.site.register(Category,CategoryAdmin)

class CoursedetailsAdmin(admin.ModelAdmin):
    list_display = ("name","type","price","status")
    
admin.site.register(CourseDetails,CoursedetailsAdmin)


class DaysAccessAdmin(admin.ModelAdmin):
    list_display = ("days", "status")

admin.site.register(DaysAccess,DaysAccessAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "course_id","price","payment_date","payment_status")

admin.site.register(Payment,PaymentAdmin)



