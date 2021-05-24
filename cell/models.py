from django.db import models


class CellImage(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(blank=True, upload_to="images", null=True)
    # predicted_images = models.ImageField(blank=True, upload_to="predict", null=True)

    # pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def predict(self):
        # self.predicted_images=predict_model(self.images)
        pass


    # def summary(self):
    #     return self.body[:100]



#
# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)


    # image = models.ImageField(blank=True) #None(null) vs. 0, ''
#     image = ProcessedImageField(
#                             blank=True,
#                             processors=[ # 어떤 가공을 할지
#                                 Thumbnail(300, 300),
#                             ],
#                             format='JPEG', # 이미지 포멧 (jpg, png)
#                             options={  # 이미지 포멧 관련 옵션
#                                 'quality':90,
#                             }
#                         )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
