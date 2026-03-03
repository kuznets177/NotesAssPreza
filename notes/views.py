from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Note


def note_list(request):
    """Список всех заметок + создание новой"""
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '')
        if title:
            note = Note.objects.create(title=title, content=content)
            return redirect('note_detail', pk=note.pk)

    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    print(f"DEBUG: note={note.title}, content={note.content[:50]}")  # дебаг
    return render(request, 'notes/note_detail.html', {'note': note})


def note_edit(request, pk):
    """Редактирование заметки"""
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '')
        if title:
            note.title = title
            note.content = content
            note.save()
            return redirect('note_detail', pk=note.pk)

    return render(request, 'notes/note_edit.html', {'note': note})


@csrf_protect
def note_delete(request, pk):
    """Удаление заметки (поддержка AJAX и обычной формы)"""
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        return redirect('note_list')
    return JsonResponse({'error': 'POST required'}, status=400)
