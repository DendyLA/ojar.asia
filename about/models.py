from django.db import models

from ckeditor.fields import RichTextField

class AboutMain(models.Model):
	title =  models.CharField(max_length=250, verbose_name="Название", blank=True, null=True)
	text = models.TextField(verbose_name='Текст', blank=True, null=True)
	video = models.FileField(upload_to="videosAbout/",verbose_name='Видео',  blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'О нас видео на главной'
		verbose_name_plural = 'О нас видео на главной'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.title or 'No data'
	

class Info(models.Model):
	category = models.CharField(max_length=250, verbose_name="Название", blank=True, null=True)
	number = models.CharField(max_length=250, verbose_name="число", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'О нас статистика'
		verbose_name_plural = 'Статистики'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.category or 'No data'
	

class Comment(models.Model):
	author = models.CharField(max_length=250, verbose_name="Автор", blank=True, null=True)
	position = models.CharField(max_length=250, verbose_name="Должность", blank=True, null=True)
	image = models.ImageField(upload_to='comment/', verbose_name='Фото')
	text = RichTextField(verbose_name='Текст', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Цитата'
		verbose_name_plural = 'Цитаты'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.author or 'No data'