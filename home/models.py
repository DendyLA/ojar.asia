from django.db import models

from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields

#sliderMain
class Slider( TranslatableModel ):
	translations = TranslatedFields(
		title = models.CharField(max_length=250, verbose_name='Название',blank=True, null=True)
	)
	image = models.ImageField(upload_to='slides/', verbose_name='Изображение' ,blank=True, null=True)   # Разрешить NULL в БД)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name = 'Слайд'
		verbose_name_plural = 'Слайды'
		ordering = ['-created_at']


	def __str__(self):
		return self.safe_translation_getter('title', any_language=True) or "Без названия"



	
	

class Videos(TranslatableModel):
	translations = TranslatedFields(
		title =  models.CharField(max_length=250, verbose_name="Название", blank=True, null=True),
		text = RichTextField(verbose_name='Текст', blank=True, null=True)
	)
	
	video = models.FileField(upload_to="videos/", blank=True, null=True)
	image = models.ImageField(upload_to="videosPhoto/", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Видео'
		verbose_name_plural = 'Видео'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.safe_translation_getter('title', any_language=True) or "Без названия"
	

	
class Awards(TranslatableModel):
	translations = TranslatedFields(
		title =  models.CharField(max_length=250, verbose_name="Название", blank=True, null=True),
		text = RichTextField(verbose_name='Текст', blank=True, null=True)
	)
	image = models.ImageField(upload_to="Awards/", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Награда'
		verbose_name_plural = 'Награды'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.safe_translation_getter('title', any_language=True) or "Без названия"
	

class ContactForm(models.Model):
	name = models.CharField( verbose_name='Имя', max_length=100)
	phone = models.CharField( verbose_name='Номер', max_length=50)
	email = models.CharField( verbose_name='Email', max_length=50)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Форма связи'
		verbose_name_plural = 'Форма связи'
		ordering = ['-created_at']

	def __str__(self):
		return f"Message from {self.name}"		