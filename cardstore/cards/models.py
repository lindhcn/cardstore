from django.db import models

# Create your models here.
# the card model with its fields
class Card(models.Model):
    player = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    year = models.DecimalField(max_digits=10, decimal_places=2)
    index = models.CharField(max_length=100)
    # this is the image for a card, the image will be uploaded to images folder
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    # this is the string representation
    # what to display after querying a card/cards
    def __str__(self):
        return f'{self.player}'
    
    # this will order the cards by date created
    class Meta:
        ordering = ['-created_at']
