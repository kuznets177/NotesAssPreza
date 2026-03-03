from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from notes import views as notes_views

def home(request):
    return HttpResponse("""
    <h1>Obsidian Clone</h1>
    <p><a href="/notes/">📝 Заметки</a> | <a href="/admin/">⚙️ Админка</a></p>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('notes/', notes_views.note_list, name='note_list'),
    path('notes/<int:pk>/', notes_views.note_detail, name='note_detail'),
    path('notes/<int:pk>/edit/', notes_views.note_edit, name='note_edit'),
    path('notes/<int:pk>/delete/', notes_views.note_delete, name='note_delete'),
]
