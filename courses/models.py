from django.db import models

# Create your models here.


from apps.users.models import RegisterModel

 
class CoursesModel(models.Model):
    
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.course_name
    
    

# class EnrollCourses(models.Moddel):
    
    
#     courses = models.ForeignKey(, verbose_name=_(""), on_delete=models.CASCADE)
    
class SectionModel(models.Model):
    
    section_name = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    course_id = models.ForeignKey(CoursesModel,on_delete=models.CASCADE, related_name='courseid')
    user =  models.ForeignKey(RegisterModel, on_delete=models.CASCADE, related_name='username1') 
    
    def __str__(self):
        return self.section_name


class ExamModel(models.Model):
    
    exam_no = models.IntegerField()
    exam_name = models.CharField(max_length=200)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE, related_name='sectionid')
    user = models.ForeignKey(RegisterModel, on_delete=models.CASCADE, related_name='username2')
    total_number = models.IntegerField()
    exam_marks = models.IntegerField()
    min_marks = models.IntegerField() 
    
    def __str__(self):
        return self.exam_name


    
    
    
    
    
# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     # Other fields for the Course model

#     def _str_(self):
#         return self.title

# class CourseSection(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     sequence_number = models.PositiveIntegerField()  # To define the order of the sections
#     # Other fields for the CourseSection model

#     def _str_(self):
#         return f"{self.course.title} - Section {self.sequence_number}: {self.title}"

# class Exam(models.Model):
#     section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     # Other fields for the Exam model

#     def _str_(self):
#         return f"{self.section.course.title} - Section {self.section.sequence_number} - Exam: {self.title}"

# class UserCourseProgress(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     completed_sections = models.ManyToManyField(CourseSection, blank=True)  # Sections completed by the user
#     # Other fields for UserCourseProgress model

#     def is_course_completed(self):
#         return self.completed_sections.count() == self.course.coursesection_set.count()