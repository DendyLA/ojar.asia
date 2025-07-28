from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


# News
class News( TranslatableModel ):
	translations = TranslatedFields(
		title = models.CharField(max_length=350, verbose_name='Название', blank=True, null=True),
		text = RichTextField(verbose_name="Текст статьи", blank=True, null=True)
	)
	
	image = models.ImageField(upload_to='news/', verbose_name="Фото")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	slug = models.SlugField(max_length=250, unique=True, verbose_name="ЧПУ-ссылка", blank=True, null=True)

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
		ordering = ['-created_at']

	def __str__(self):
		return self.title or 'No data'
	
	
	def save(self, *args, **kwargs):
		if self.image:
			# Открытие изображения
			img = Image.open(self.image)

			# Преобразование в RGB (на случай PNG и др.)
			if img.mode in ("RGBA", "P"):
				img = img.convert("RGB")

			# Сжатие изображения
			output = BytesIO()
			img.save(output, format='JPEG', quality=70)  # quality: от 1 до 95
			output.seek(0)

			# Сохранение в поле image
			self.image = ContentFile(output.read(), self.image.name)

		if not self.slug and self.title:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)
        
	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('news-detail', kwargs={'slug': self.slug})
	