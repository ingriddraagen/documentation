from django.db import models

# Create your models here.
class Chapter(models.Model):
    title = models.CharField(max_length=30)

class SubChapter(models.Model):
    title = models.CharField(max_length=30)
    part_of_chapter = models.ForeignKey(
        'apidocumentation.Chapter',
        on_delete=models.CASCADE,
    )

class Paragraph(models.Model):
    header = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField()

class CodeSnippet(models.Model):
    code = models.TextField()
    related_to_paragraph = models.ForeignKey(
        'apidocumentation.Paragraph',
        on_delete=models.CASCADE,
    )

class Image(models.Model):
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    related_to_paragraph = models.ForeignKey(
        'apidocumentation.Paragraph',
        on_delete=models.CASCADE,
    )
