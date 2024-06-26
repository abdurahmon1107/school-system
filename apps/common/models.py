from django.db import models
from django.core.validators import RegexValidator
from django.db import models
from apps.users.models import User

PHONE_NUMBER_VALIDATOR = RegexValidator(regex=r"^\+998\d{9}$",message="Invalid phone number")
 
KELDI , KELMADI = "Keldi" , 'Kelmadi'

TOSHKENT = "Toshkent"
ANDIJON = "Andijon"
SAMARQAND = "Samaarqand"
BUXORO = "Buxoro"
NAVOIY = "Navoiy"
QORAQALPOGISTON = "Qorajalpogiston"
QASHQADARYO = "Qashqadaryo"
XORAZM = "Xorazm"
SURHANDARYO = "Surhandaryo"
SIRDARYO = "Sirdaryo"
NAMANGAN = "Namangan"
TOSHKENT_SHAHAR = "Toshkent_shahar"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True





class Position(BaseModel):
    subject_name = models.CharField(max_length=250,
                                   verbose_name='Subject name')

    
    def __str__(self) -> str:
        return self.subject_name
    
class School(BaseModel):
    REGION_CHOICE = (
        ( TOSHKENT , "Toshkent"),
        ( ANDIJON , "Andijon"),
        ( SAMARQAND, 'Samarqand'),
        ( BUXORO, "Buxoro"),
        ( NAVOIY, "Navoiy"),
        ( QORAQALPOGISTON, 'Qoraqalpogiston'),
        ( QASHQADARYO, 'Qashqadaryo'),
        ( XORAZM, "Xorazm"),
        ( SURHANDARYO, "Surhandaryo"),
        ( SIRDARYO, "Sirdaryo"),
        ( NAMANGAN, "Namangan"),
        ( TOSHKENT_SHAHAR, "Toshkent_shahar"),
    )
    school_name = models.CharField(max_length=250)
    director = models.ForeignKey('users.User',
                                    on_delete=models.CASCADE,
                                    verbose_name='Director',
                                    related_name='school_director',
                                )


    adress = models.CharField(max_length=300)
    region = models.CharField(max_length=100, choices=REGION_CHOICE, default=TOSHKENT_SHAHAR, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.school_name} - {self.id}"
    



class Pupil(BaseModel):
    DAVOMAT = (
       ( KELDI , "Keldi"),
        ( KELMADI , "Kelmadi")
    ) 
    full_name = models.CharField(max_length=250,verbose_name='Full name')
    school = models.ForeignKey(School,
                               on_delete=models.CASCADE,
                               related_name='pupils',
                               verbose_name='School')
    group = models.ForeignKey('Group',
                              on_delete=models.PROTECT,
                              related_name='pupils',
                              verbose_name='Group')
    birthday = models.DateField()
    phone_number = models.CharField(max_length=13 ,
                                    validators=[PHONE_NUMBER_VALIDATOR],
                                    verbose_name='Phone number')
    parent_full_name = models.CharField(max_length=500,
                                        verbose_name='Parent full name')
    parent_number = models.CharField(max_length=13,
                                     validators=[PHONE_NUMBER_VALIDATOR],
                                     verbose_name='Parent phone number')
    attendance_status = models.CharField(max_length=7,
                            choices = DAVOMAT,
                            default = KELDI,
                            verbose_name = 'Davomat')

    
    def __str__(self):
        return f"{self.full_name}-{self.id}"
    

class Group(BaseModel):
    group_name = models.CharField(max_length=250,
                                  verbose_name='Group name')
    pupils_count = models.IntegerField(default=0)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_groups')

    
    def __str__(self) -> str:
        return self.group_name
    


class ClassRoom(BaseModel):
    class_name = models.CharField(max_length=250)
    school = models.ForeignKey(School,
                               on_delete=models.CASCADE,
                               related_name='class_rooms',
                               verbose_name='School')
    capacity = models.PositiveIntegerField(default = 0)
    group = models.ForeignKey(Group,
                              on_delete=models.PROTECT,
                              related_name='class_rooms',
                              verbose_name='Group')
    
    def __str__(self) -> str:
        return f"{self.class_name} - {self.id}"
    


class UserSchool(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_schools')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='users_chools')


class UserPosition(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_positions')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='user_positions')
