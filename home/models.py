from django.db import models

from ckeditor.fields import RichTextField


#sliderMain
class Slider( models.Model):
	title = models.CharField(max_length=250, verbose_name='Название',blank=True, null=True)
	image = models.ImageField(upload_to='slides/', verbose_name='Изображение' ,blank=True, null=True)   # Разрешить NULL в БД)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name = 'Слайд'
		verbose_name_plural = 'Слайды'
		ordering = ['-created_at']


	def __str__(self):
		return self.title or "No data"



	
	

class Videos(models.Model):
	title =  models.CharField(max_length=250, verbose_name="Название", blank=True, null=True)
	text = RichTextField(verbose_name='Текст', blank=True, null=True)
	video = models.FileField(upload_to="videos/", blank=True, null=True)
	image = models.ImageField(upload_to="videosPhoto/", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Видео'
		verbose_name_plural = 'Видео'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.title or 'No data'
	

	
class Awards(models.Model):
	title =  models.CharField(max_length=250, verbose_name="Название", blank=True, null=True)
	text = RichTextField(verbose_name='Текст', blank=True, null=True)
	image = models.ImageField(upload_to="Awards/", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Награда'
		verbose_name_plural = 'Награды'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.title or 'No data'