from django.db import models

# Create your models here.
class Main(models.Model):
    name = models.CharField(max_length=255)
    screen = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    case = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255, default="http://localhost:8000/product_page1/")
    product_path = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()
    img = models.ImageField(blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.name}, {self.image_path}, {self.product_path}"
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
    
        


# Main.objects.create(name = 'Apple iPhone 14 Pro', screen = '6.1 ", 2556x1179, 460 ppi, 120 Гц', camera = '3 модулі, 48 МП, + 12 МП, fullHD 60 к/с, відео 4K, оптична стабілізація, стабілізація матрицею', memory = '512 ГБ', cpu = 'Apple A16', case = 'скло, 206 г, товщина 8 мм', image_path = 'https://yabloki.ua/media/cache/app_product_page_small_slider_image/79/d5/eaf12ac031d35cc9e9ff37052e3f.png')
# Main.objects.create(name = 'Apple iPhone 15 Plus', screen = '6.7 ", 2796х1290, 460 ppi, 60 Гц', camera = '2 модулі, 48 МП, + 12 МП, fullHD 60 к/с, відео 4K, стабілізація матрицею', memory = '512 ГБ', cpu = 'Apple A16', case = 'скло, 201 г, товщина 8 мм', image_path = 'https://yabloki.ua/media/cache/app_product_page_small_slider_image/c0/84/c04b1910c6b999dcbe9e2c9377c2.png')

# Main.objects.create(name = '', screen = '', camera = '', memory = '', cpu = '', case = '', image_path = '')
# Main.objects.create(name = 'Apple iPhone 15 Pro', screen = '6.1 ", 2556x1179, 461 ppi, 120 Гц', camera = '3 модулі, 48 МП, + 12 МП, fullHD 60 к/с, відео 4K, оптична стабілізація, стабілізація матрицею', memory = '1024 ГБ', cpu = 'Apple A17 Pro', case = 'скло, 187 г, товщина 8 мм', image_path = 'https://yabloki.ua/media/cache/app_product_page_small_slider_image/94/44/a6edf81bc54bb45c1a12ef1078b4.png')
# Main.objects.create(name = 'Apple iPhone 15 Pro Max', screen = '6.7 ", 2796x1290, 460 ppi, 120 Гц', camera = '3 модулі, 48 МП, + 12 МП, fullHD 60 к/с, відео 4K, оптична стабілізація, стабілізація матрицею', memory = '1024 ГБ', cpu = 'Apple A17 Pro', case = 'скло, 221 г, товщина 8 мм', image_path = 'https://yabloki.ua/media/cache/app_product_page_small_slider_image/94/44/a6edf81bc54bb45c1a12ef1078b4.png')
# Main.objects.create(name = 'Apple iPhone 15', screen = '6.1 ", 2556x1179, 460 ppi, 60 Гц', camera = '2 модулі, 48 МП, + 12 МП, fullHD 60 к/с, відео 4K, стабілізація матрицею', memory = '512 ГБ', cpu = 'Apple A16', case = 'скло, 171 г, товщина 8 мм', image_path = 'https://yabloki.ua/media/cache/app_product_page_small_slider_image/90/51/caa89bf03b3b9929c2c49e8cd4f8.png')