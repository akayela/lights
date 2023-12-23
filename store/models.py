from django.db import models
from django.urls import reverse

# Create your models here.
class Stock(models.Model):
    CATEGORIES = (
            ('Fairylts Rub-L', 'Fairylts Rub-L'),
            ('Fairylts Rub-NL', 'Fairylts Rub-NL'),
            ('Fairylts Pvc-L', 'Fairylts Pvc-L'),
            ('Fairylts Pvc-NL', 'Fairylts Pvc-NL'),
            ('Round Rope', 'Round Rope'),
            ('Flat Rope', 'Flat Rope'),
            ('Cable Ties', 'Cable Ties'),
            ('Control Block', 'Control Block'),
            ('Enclosure', 'Enclosure'),
            ('Tee Joint', 'Tee Joint'),
            ('Straight Joint', 'Straight Joint'),
            ('F16 v4', 'F16 v4'),
            ('F16 v3', 'F16 v3'),
            ('F4', ' F4'),
            ('F48', 'F48'),
            ('Power Supply', 'Power Supply'),
            )
    category = models.CharField(max_length=100, choices=CATEGORIES, blank=True, null=True)

    COLORS = (
            ('Red Stdy', 'Red Stdy'),
            ('Red Twkl', 'Red Twkl'),
            ('Red', 'Red'),

            ('Blue Stdy', 'Blue Stdy'),
            ('Blue Twkl', 'Blue Twkl'),
            ('Blue', 'Blue'),

            ('Green Stdy', 'Green Stdy'),
            ('Green Twkl', 'Green Twkl'),
            ('Green', 'Green'),

            ('C.White Stdy', 'C.White Stdy'),
            ('C.White Twkl', 'C.White Twkl'),
            ('C.White', 'C.White'),

            ('W.White Stdy', 'W.White Stdy'),
            ('W.White Twkl', 'W.White Twkl'),
            ('W.White', 'W.White'),

            ('M.Color Stdy', 'M.Color Stdy'),
            ('M.Color Twkl', 'M.Color Twkl'),
            ('M.Color', 'M.Color'),

            ('Pink Stdy', 'Pink Stdy'),
            ('Pink Twkl', 'Pink Twkl'),
            ('Pink', 'Pink'),

            ('Purple Stdy', 'Purple Stdy'),
            ('Purple Twkl', 'Purple Twkl'),
            ('Purple', 'Purple'),

            ('Orange Stdy', 'Orange Stdy'),
            ('Orange Twkl', 'Orange Twkl'),
            ('Orange', 'Orange'),
            
            )
    color = models.CharField(max_length=100, choices=COLORS, null=True, blank=True)

    quantity = models.IntegerField(default=0, blank=True, null=True)
    
    receive_quantity = models.IntegerField(default=0, blank=True, null=True)

    UNITS = (
            ('Meter(s)', 'Meter(s)'),
            ('Unit(s)', 'Unit(s)'),
            ('Packet(s)', 'Packet(s)'),
            ('Roll(s)', 'Roll(s)'),
            )
    unit = models.CharField(max_length=100, choices=UNITS, blank=True, null=True)

    size = models.CharField(max_length=100, default=0, blank=True, null=True)

    stock_code = models.CharField(max_length=100, default=0, blank=True, null=True)

    CONDITIONS = (
            ('New', 'New'),
            ('Used', 'Used'),
            )
    condition = models.CharField(max_length=100, choices=CONDITIONS, null=True, blank=True)

    location = models.CharField(max_length=100, null=True, blank=True)

    shelf_id = models.IntegerField(default=0, blank=True, null=True)

    container_id = models.IntegerField(default=0, blank=True, null=True)

    issue_quantity = models.IntegerField(default=0, blank=True, null=True)

    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.category
