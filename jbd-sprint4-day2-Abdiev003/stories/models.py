from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    title = models.CharField('Title', max_length=50)

    # moderation's
    order = models.PositiveIntegerField('Order', default=1)
    is_published = models.BooleanField('Is Published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('created_at',)

    def __str__(self):
        return self.title


class Category(models.Model):
    # information's
    title = models.CharField('Title', max_length=127)
    image = models.ImageField('Image', upload_to='category_images', )

    # moderation's
    order = models.PositiveIntegerField('Order', default=1)
    is_published = models.BooleanField('Is Published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('order', '-created_at')

    def __str__(self):
        return self.title


# class TagRecipeRel()
#     tag
#     recipe =


class Recipe(models.Model):
    """
    in this table you can store recipes like: 'Alma Piroqu, Gilas Piroqu,'
    """
    # CATEGORY_OPTIONS = (
    #     (1, 'Dessert'),
    #     (2, 'Salat'),
    #     (3, 'Xalodni'),
    # )
    # relation's
    category = models.ForeignKey(Category, verbose_name='Category',
                                 on_delete=models.CASCADE, db_index=True, related_name='recipes')
    tags = models.ManyToManyField(Tag, verbose_name='Tags', db_index=True, blank=True, )
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE, db_index=True,
                               related_name='recipes', )

    # information's
    title = models.CharField('Basliq', max_length=127)
    slug = models.SlugField('Slug', max_length=155)
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    image = models.ImageField('Sekil', upload_to='recipe_images', )

    # category = models.IntegerField('Kategoriya', choices=CATEGORY_OPTIONS)
    description = models.TextField('Mezmun', )

    # moderation's
    order = models.PositiveIntegerField('Order', default=1)
    is_published = models.BooleanField('Is Published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Resept'
        verbose_name_plural = 'Reseptler'
        ordering = ('order', '-created_at')

    def __str__(self):
        return f"{self.title} Kategoriyasi: {self.category.title}"


# resept = Recipe()
# resept.category
#
# kategori = Category()
# kategori.recipes.all()


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


class Comment(models.Model):
    # relation's
    recipe = models.ForeignKey(Recipe, verbose_name='Recipe', on_delete=models.CASCADE, db_index=True,
                               related_name='comment')
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='comment')
    parent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_comments', blank=True, null=True)

    # information's
    content = models.TextField('Content')

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"
