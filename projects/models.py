from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

class Projects(models.Model):
	title =  models.CharField(max_length=250, verbose_name="Название проекта", blank=True, null=True)
	text = RichTextField(verbose_name='Текст проекта', blank=True, null=True)
	location =  models.CharField(max_length=250, verbose_name="Локация проекта", blank=True, null=True)
	image = models.ImageField(upload_to="projects/",verbose_name='Фото проекта',  blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	is_finish = models.BooleanField(default=False, verbose_name="Выполнен проект или нет")
	is_featured = models.BooleanField(default=False, verbose_name="Ключевой проект или нет")
	slug = models.SlugField(max_length=250, unique=True, verbose_name="ЧПУ-ссылка", blank=True, null=True)

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.title or 'No data'
	

	def save(self, *args, **kwargs):
		if not self.slug and self.title:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)
        
	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('projects-detail', kwargs={'slug': self.slug})