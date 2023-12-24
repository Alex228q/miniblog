from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок поста', max_length = 100)
    description = models.TextField('Текст поста')
    author = models.CharField('Имя автора',max_length = 100)
    date = models.DateField('Дата публикации')
    image = models.ImageField('Изображение', upload_to= 'images/%Y')


    def __str__(self):
        return f'{self.title} , {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



class Comment(models.Model):
    '''коментарий'''
    # email = models.EmailField()
    name = models.CharField('Имя', max_length = 50)
    text_comment = models.TextField('Текст комментария', max_length = 2000)
    post = models.ForeignKey(Post, verbose_name= 'Публикация', on_delete = models.CASCADE)
    created_at = models.DateTimeField('Дата комментария', auto_now_add = True)

    def __str__(self):
        return f'{self.name} , {self.text_comment}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'