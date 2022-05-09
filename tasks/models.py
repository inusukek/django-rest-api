from django.db import models


class Task(models.Model):
    description = models.TextField()
    seq = models.CharField(max_length=80) 
    complete = models.BooleanField()
    #การกำหนดคอลัมใน sqllite / หลัง migration รูปแบบฟิลจะถูกจัดเก็บที่ไฟล migration
    class Meta:
        ordering = ['seq']
        db_table = 'task'
    
    def __str__(self):
        return self.seq + ' ' + self.description