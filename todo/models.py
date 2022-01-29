from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    
    PRIORITY = (
     ("1","High"),
     ("2", "Medium"),
     ("3", "Low"),   
    )
    
    priority = models.CharField(max_length=50, choices = PRIORITY)
    isDone = models.BooleanField(default=False)
    
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"TITLE: {self.title}\nDESCRIPTION: {self.description}\nCREATED AT: {self.created_date}"