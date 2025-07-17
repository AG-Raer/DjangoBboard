from django.contrib import admin
from django import forms
from .models import Bb

class BbAdminForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = '__all__'

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if slug:
            return slugify(slug, allow_unicode=True) or slug
        return slug

@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    form = BbAdminForm
    list_display = ['title', 'slug', 'price', 'published', 'user']
    list_filter = ['published', 'user']
    search_fields = ['title', 'content']
    fields = ['title', 'content', 'price', 'image', 'slug', 'user']