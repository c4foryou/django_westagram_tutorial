from django.db import models

class Comment(models.Model):
    name       = models.CharField(max_length = 50)
    comments   = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
    	db_table = 'user_comment'
