from django.db import models

class CommonInfo(models.Model):
    upload_date=models.DateField(auto_now_add=True,verbose_name="upload date",name="upload_date")
    title=models.CharField(max_length=300,verbose_name="title",name="title")
    file=models.FileField(upload_to="" )

    class Meta:
        abstract=True

class McaNotice(CommonInfo):
    file=models.FileField(upload_to="admin/mcanotice/" )


class StatisticNotice(CommonInfo):
    file=models.FileField(upload_to="admin/statisticnotice/" )

class McaAdmission(CommonInfo):
    file=models.FileField(upload_to="admin/mcaadmission/" )

class StatisticAdmission(CommonInfo):
    file=models.FileField(upload_to="admin/statisticadmission/" )

class McaResult(CommonInfo):
    file=models.FileField(upload_to="admin/mcaresults/" )

class StatisticResult(CommonInfo):
    file=models.FileField(upload_to="admin/statisticresults/" )

        
class McaCourse(CommonInfo):
    id=None
    upload_date=None
    title=None
    file=models.FileField(upload_to="pdf/mcacourse/" )
class StatisticCourse(CommonInfo):
    id=None
    upload_date=None
    title=None
    file=models.FileField(upload_to="pdf/statisticcourse/" )
    
class LatestDept(CommonInfo):
   upload_date=models.DateTimeField(auto_now_add=True)
   file=models.FileField(upload_to="admin/lastestdeptupdate/" )


class McaEbook(CommonInfo):    
    upload_date=None    
    writer=models.CharField(max_length=200)
    file=models.FileField(upload_to="admin/mcaebook/",max_length=200)

class StatisticEbook(CommonInfo):
    upload_date=None
    writer=models.CharField(max_length=200)
    file=models.FileField(upload_to="admin/statisticebook/", max_length=200)

class McaSemister1(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/mcaquestions/",max_length=200 )

class McaSemister2(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/mcaquestions/", max_length=200 )


class McaSemister3(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/mcaquestions/",max_length=200 )


class McaSemister4(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/mcaquestions/",max_length=200 )


class McaSemister5(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/mcaquestions/",max_length=200 )


class McaSemister6(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/mcaquestions/",max_length=200 )

    
class StatisticSemister1(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/statisticquestions/",max_length=200 )


class StatisticSemister2(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/statisticquestions/",max_length=200 )


class StatisticSemister3(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/statisticquestions/",max_length=200 )
class StatisticSemister4(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/statisticquestions/",max_length=200 )

class StatisticSemister5(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/statisticquestions/",max_length=200)
    
class StatisticSemister6(CommonInfo):    
    upload_date=None
    file=models.FileField(upload_to="admin/statisticquestions/",max_length=200)
    
class Gallery(CommonInfo):    
    upload_date=None
    file=None
    img=models.ImageField(upload_to="admin/StatisticdeptGallery/",max_length=200)

class StudentBlog(CommonInfo):
    upload_date=models.DateTimeField(auto_now_add=True)
    file=None
    author=models.CharField(max_length=200)
    img=models.ImageField(upload_to="admin/studentblogGallery/",max_length=200)
    content=models.TextField()

class Qualification(models.Model):
    qualification=models.CharField(max_length=300)
    def __str__(self):
        return self.qualification
    
    



class Faculty(models.Model):    
    name=models.CharField(max_length=200)    
    experience=models.PositiveIntegerField() 
    qualification=models.ManyToManyField("Qualification")      
    img=models.ImageField(upload_to="admin/mcafaculty/",max_length=200)   
    class Meta:
        abstract=True

class Subject(models.Model):       
    subject=models.CharField(max_length=300,unique=True) 
    
    class Meta:
        abstract=True

class McaFaculty(Faculty):
    subject=models.ManyToManyField("McaSubject")
    def __str__(self):
        return self.name
class McaSubject(Subject):    
    def __str__(self):
        return self.subject

class StatisticsFaculty(Faculty):
    administrative_post= models.CharField(max_length=300)
    subject=models.ManyToManyField("StatisticsSubject")
    def __str__(self):
        return self.name

class StatisticsSubject(Subject):    
    def __str__(self):
        return self.subject
    
    
class Carousel(models.Model):
    img=models.ImageField(upload_to="admin/carousel/",max_length=200)
    
class ContactUs(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    query=models.TextField()
    file=models.FileField(upload_to="user/contactus/")
    

