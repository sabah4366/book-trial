from django.db import models
from django.contrib.auth.models import User
BOOK_CATEGORIES=(
    ('action','action'),
    ('classics','classics'),
    ('comic','comic'),
    ('mystery','mystery'),
    ('fantacy','fantacy'),
    ('fiction','fiction'),
    ('horror','horror'),
    ('literary','literary'),
    ('nonfiction','nonfiction')

)
class Book(models.Model):
    author=models.ForeignKey(User,related_name='books',on_delete=models.CASCADE)
    title=models.CharField(blank=False,max_length=100)
    book_price=models.IntegerField(blank=False)
    category=models.CharField(choices=BOOK_CATEGORIES,default='classics',max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    modified_at=models.DateTimeField(auto_now=True,blank=True)

    class Meta:
        ordering=['-created_at']
