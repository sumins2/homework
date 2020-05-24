from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class comment(models.Model):
    post_that_i_wrote_a_comment = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()