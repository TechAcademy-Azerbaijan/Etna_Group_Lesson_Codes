from django.db import models


class Recipe(models.Model):
    """
    in this table you can store recipes like: 'Alma Piroqu, Gilas Piroqu,'
    """
    CATEGORY_OPTIONS = (
        (1, 'Dessert'),
        (2, 'Salat'),
        (3, 'Xalodni'),
    )

    # information's
    title = models.CharField('Basliq', max_length=127)
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    image = models.ImageField('Sekil', upload_to='recipe_images',)
    category = models.IntegerField('Kategoriya', choices=CATEGORY_OPTIONS)
    description = models.TextField('Mezmun', )

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table = 're'
        verbose_name = 'Resept'
        verbose_name_plural = 'Reseptler'
        ordering = ('title', '-created_at')

    def __str__(self):
        return f"{self.title} Kategoriyasi: {self.get_category_display()}"


class Contact(models.Model):
    """
    in this table you can store user contact info
    """

    # information's
    full_name = models.CharField('Tam adi', max_length=127)
    email = models.EmailField('E-poct', max_length=63)
    subject = models.CharField('Movzu', max_length=255)
    message = models.TextField('Mesaj', help_text='Bu qutuya mesajinizi ehateli sekilde daxil edin')

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"

