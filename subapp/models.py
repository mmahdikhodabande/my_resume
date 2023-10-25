from django.db import models


# Create your models here.
class Work_samples(models.Model):
    name_project = models.CharField(max_length=200, verbose_name='نام پروژه')
    avatar_project = models.FileField(upload_to='images/image_project', verbose_name='تصویر پروژه', null=True,
                                      blank=True)
    description = models.TextField(blank=False, max_length=600, null=False, verbose_name='توضیحات راجب نمونه کار')
    link_field = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name_project

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها '


gender = (
    ('مرد', 'مرد'),
    ('زن', 'زن '),
    ('ترجیح می دهم نگویم', 'ترجیح می دهم نگویم '),
)
martial_status = (
    ('مجرد', 'مجرد'),
    ('متاهل', 'متاهل '),
)
Military_service_status = (
    ('پایان خدمت', 'پایان خدمت '),
    ('معافیت دائم', 'معافیت دائم'),
    ('معافیت تحصیلی', 'معافیت تحصیلی'),
    ('در حال انجام ', 'در حال انجام '),
    ('مشمول', 'مشمول'),
)
mastery_level = (
    ('مبتدی', 'مبتدی'),
    ('متوسط', 'متوسط '),
    ('حرفه ای ', 'حرفه ای  '),
    ('تسلط کامل', 'تسلط کامل'),
)
Percent = (
    ('10', '10'),
    ('20', '20 '),
    ('30', '30'),
    ('40', '40'),
    ('50', '50'),
    ('60', '60'),
    ('70', '70'),
    ('80', '80'),
    ('90', '90'),
    ('100', '100'),
)


class work_experience(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='عنوان شغلی')
    date_start_work = models.DateField(verbose_name='تاریخ شروع شغل', null=False, blank=False)
    date_end_work = models.DateField(verbose_name='تاریخ پایان شغل', null=False, blank=False)
    description = models.TextField(max_length=1700, blank=False, null=False, verbose_name='توضیحات شغل')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'عنوان شغل'
        verbose_name_plural = 'عناوین شغلی'


class Educational_records(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='عنوان تحصیلی')
    date_start_work = models.DateField(verbose_name='تاریخ شروع تحصیل', null=False, blank=False)
    date_end_work = models.DateField(verbose_name='تاریخ پایان تحصیل', null=False, blank=False)
    description = models.TextField(max_length=1700, blank=False, null=False, verbose_name='توضیحات تحصیلات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سابقه تحصیل'
        verbose_name_plural = 'سوابق تحصیلات'


class languages(models.Model):
    title = models.CharField(max_length=20, verbose_name='زبان')
    mastery_level = models.CharField(max_length=10, choices=mastery_level, verbose_name='سطح تسلط')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'زبان '
        verbose_name_plural = 'زبان ها'


class interests(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='علافه ها ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'علاقه '
        verbose_name_plural = 'علاقه ها'


class Me(models.Model):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', null=False, blank=False)
    name = models.CharField(max_length=30, verbose_name='نام', null=False, blank=False)
    family_name = models.CharField(max_length=30, verbose_name='نام خانوادگی', null=False, blank=False)
    Scientific_position = models.CharField(max_length=30, verbose_name='جایگاه علمی شما', null=False, blank=False)
    Technical_expertise = models.CharField(max_length=30, verbose_name='تخصص فنی شما', null=False, blank=False)
    gender = models.CharField(max_length=30, choices=gender, verbose_name='جنسیت', null=False, blank=False)
    marital_status = models.CharField(max_length=30, choices=martial_status, verbose_name='وضعیت تاهل ', null=False,
                                      blank=False)
    Military_service_status = models.CharField(max_length=30, choices=Military_service_status,
                                               verbose_name='وضعیت خرمت سربازی ',
                                               null=False,
                                               blank=False)
    Nationality = models.CharField(max_length=30, verbose_name='ملیت شما', null=False, blank=False)
    Your_current_location = models.CharField(max_length=30, verbose_name='موقیعت فعلی شما', null=False, blank=False)
    Requested_stipend = models.IntegerField(max_length=30, verbose_name='حقوق درخواستی شما', null=False, blank=False)
    date_of_birth = models.DateField(verbose_name='تاریخ تولد', null=False, blank=False)
    phone = models.CharField(max_length=11, verbose_name='شماره تماس', null=False, blank=False)
    email = models.EmailField(verbose_name='ایمیل ')
    samples_project = models.ForeignKey(Work_samples, on_delete=models.CASCADE, verbose_name='نمونه کار ', null=False,
                                        blank=False)
    biography = models.TextField(max_length=600, null=False, blank=False, verbose_name='بیوگرافی')
    work_experience = models.ForeignKey(work_experience, on_delete=models.CASCADE, verbose_name='عناوین شغلی')
    Educational_records = models.ForeignKey(Educational_records, on_delete=models.CASCADE, verbose_name='سابقه تحصیلی')

    def __str__(self):
        return f'( {self.name} - {self.family_name} )'

    class Meta:
        verbose_name = ' رزومه شما'
        verbose_name_plural = ' رزومه شما'


class Skills(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان مهارت')
    Percent = models.CharField(max_length=30, choices=Percent,
                               verbose_name='درصد مهارت شما ',
                               null=False,
                               blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'


class Cyberspace(models.Model):
    instagram = models.CharField(max_length=200, verbose_name='لینک اینستگرام')
    X = models.CharField(max_length=200, verbose_name='لینک ایکس(توییتر)')
    Linkedin = models.CharField(max_length=200, verbose_name='لینک لینکدین')
    Github = models.CharField(max_length=200, verbose_name='لینک گیت هاب ')

    def __str__(self):
        return f'( {self.instagram})'

    class Meta:
        verbose_name = 'آدرس فضای مجازی'
        verbose_name_plural = 'آدرس های فضاهای مجازی'
