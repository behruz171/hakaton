from django.db import models
from apps.users.models import User

    
from django.core.validators import RegexValidator , MaxValueValidator




phone_validator = RegexValidator(regex=r"^\+998\d{9}$", message='phone number is wrong',
                                 code="invalid_phone")


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Banner(BaseModel):
    image = models.ImageField(upload_to='banner_image/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def str(self):
        return f"{self.title}-{self.description}"



     
class Appeal(BaseModel):
    expert = models.ForeignKey(User,
                                related_name='expert_appeal',
                                on_delete=models.CASCADE,
                                verbose_name='Appeal',
                                )
    user = models.ForeignKey(User,
                             related_name="user_appeal",
                             on_delete=models.CASCADE,
                             verbose_name="User"
                             )
    description = models.TextField()


    def str(self):
        return f"{self.id}-{self.full_name}-{self.telephone_number}"
    
class Comment(BaseModel):
    expert = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='expert_comment',
                                verbose_name='Comment',
                                )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="User"
                             )
    degree = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    description = models.TextField()

    def str(self) -> str:
        return f"{self.id}-{self.degree}-{self.description}"
    
class Meeting(BaseModel):
    title = models.CharField(max_length=255)
    zoom_meeting_id = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self) -> str:
        return f"{self.id}-{self.title}"