from django.db import models

class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True)

    created = models.DateField('Criado em', auto_now_add=True)
    modified = models.DateField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    stars = models.IntegerField('Avaliação')
    category = models.ForeignKey('catalog.category', verbose_name='Categoria', on_delete=models.CASCADE)
    image = models.ImageField('Imagem', null=True, blank=True, upload_to='img')

    created = models.DateField('Criado em', auto_now_add=True)
    modified = models.DateField('Modificado em', auto_now=True)

    
    def __str__(self):
        return self.name
        
    class Meta():
        verbose_name ='Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']