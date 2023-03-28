from django.db import models
from django.contrib.auth.models import User
from backend.custom_storages import MediaStorage
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_delete, post_migrate

class UserProfile(models.Model):
    WHITE = '1'
    BLACK = '2'
    USER_TEMPLATE_CHOICE = [
    (WHITE, 'White Header'),
    (BLACK, 'Black Header')
    ]

    MALE = '1'
    FEMALE = '2'
    USER_GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user_profile')
    user_company = models.CharField('Company',max_length=255, null = True, blank=True)
    user_position = models.CharField('Position', max_length = 255, null = True, blank=True)
    # user_template = models.CharField(verbose_name='Timesheet Template Color',max_length=1, choices=USER_TEMPLATE_CHOICE, default=BLACK)
    user_gender = models.CharField(verbose_name = 'Your gender', max_length = 1, choices = USER_GENDER_CHOICE, default = MALE, null=True)
    user_email_destiny = models.EmailField(verbose_name='Email Addressee/ Who will receive your timesheet', null = True, blank=True) 
    # user_salary = models.FloatField('Salary', default=0,null=True, blank=True)
    user_phone_number = models.CharField('Phone Number', max_length=255, null = True, blank=True)

    user_car_registration = models.CharField('Car Registration', max_length=255, null = True, blank=True)
    user_car_make = models.CharField('Car Make', max_length=255, null = True, blank=True)
    user_car_model = models.CharField('Car Model', max_length=255, null = True, blank=True)
    user_car_is_diesel = models.BooleanField('Is the car diesel?', default=False, null=True, blank=True)
    user_car_wof = models.DateField('Car WOF', null = True, blank=True)
    user_car_rego = models.DateField('Car REGO', null = True, blank=True)
    user_date_next_service = models.DateField('Next Service', null = True, blank=True)
    user_next_service_mileage = models.IntegerField('Next Service Mileage', null = True, blank=True, )
    user_kms_paid_up_to = models.IntegerField('Kms Paid Up To', null = True, blank=True)


    #user_photo = models.ImageField(upload_to=f'media/{str(user)}_img/', null=True)
    def __str__(self):
        return str(self.user)

class UserKey(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activation_key = models.CharField(max_length=40, null=True)
	key_expires = models.DateTimeField(null=True)
	active = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.user)

class SignatureProfile(models.Model):
    user_signature= models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_signature', null=True, blank=True)
    # signature = models.ImageField(upload_to='signatures/', null=True, blank=True)
    signature = models.ImageField(storage=MediaStorage(), null=True, blank=True, upload_to='signatures_forms/')
    signature_url = lambda self: self.signature.url if self.signature else None
    def __str__(self):
        return f'{self.user_signature}'


@receiver(post_delete, sender=[SignatureProfile])
def auto_delete_file(sender, instance, **kwargs):
    instance.file.delete(False)

@receiver(post_migrate, sender=[SignatureProfile])
def auto_update_file(sender, instance, **kwargs):
    instance.file.delete(False)