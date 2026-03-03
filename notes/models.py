from django.db import models
import markdown

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_markdown_content(self):
        md_content = markdown.markdown(self.content)
        print(f"RAW: {self.content[:100]}")  # дебаг
        print(f"HTML: {md_content[:100]}")  # дебаг
        return md_content



