from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Cell(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True) #None(null) vs. 0, ''
    image = ProcessedImageField(
                            blank=True,
                            processors=[ # 어떤 가공을 할지
                                Thumbnail(300, 300),
                            ],
                            format='JPEG', # 이미지 포멧 (jpg, png)
                            options={  # 이미지 포멧 관련 옵션
                                'quality':90,
                            }
                        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


