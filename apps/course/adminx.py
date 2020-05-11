import xadmin
from xadmin import views
from .models import Course,Lesson,Video,CourseResource


# xadmin.site.register(views.BaseAdminView,BaseSetting)
# xadmin.site.register(views.CommAdminView,GlobalSettings)

class CourseAdmin(object):
    #课程
    list_display = ['name','degree','desc','detail','learn_times','students']
    search_fields = ['name','degree','desc','detail','students']
    list_filter = ['name','degree','desc','detail','learn_times','students']

xadmin.site.register(Course,CourseAdmin)

class LessonAdmin(object):
    #章节
    list_display = ['name','course','add_time']
    search_fields = ['name','course']
    list_filter = ['name','course','sdd_time']

xadmin.site.register(Lesson,LessonAdmin)

class VideoAdmin(object):
    #视频
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']

xadmin.site.register(Video,VideoAdmin)

class CourseResourceAdmin(object):
    #视频
    list_display = ['name','course','download','add_time']
    search_fields = ['name','course','download']
    list_filter = ['name','course','download','add_time']

xadmin.site.register(CourseResource,CourseResourceAdmin)