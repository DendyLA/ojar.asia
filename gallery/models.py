from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Gallery( models.Model ):
	title = models.CharField( max_length=250, verbose_name='имя фото', blank=True, null=True)
	image = models.ImageField(upload_to='gallery/', verbose_name="Фото")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Галерея'
		verbose_name_plural = 'Галерея'
		ordering = ['-created_at']
		


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

		super().save(*args, **kwargs)

	def __str__(self):
		return self.title or 'No data'
	
        
	