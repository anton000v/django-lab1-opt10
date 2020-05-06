from django.shortcuts import render
from django.views import View
from .models import File
from django.http import JsonResponse

class IndexView(View):
    def get(self, request):
        files = File.objects.all()
        search_key_word = request.GET.get('key-word')
        if search_key_word:
            files = files.filter(description__icontains=search_key_word)
        context = {
            'files': files,
            'search_key_word': search_key_word
        }
        return render(request, 'Lab1Files/index.html', context=context)

class AjaxAddDownload(View):
    def get(self, request):
        if request.is_ajax():
            id = request.GET.get('id')
            file_field = File.objects.get(id=id)
            file_field.incr_counter()
            file_field.save()
            return JsonResponse({'message':'Success'})
        else:
            raise 404

class AdminStatistics(View):
    def get(self, request):
        if request.user.is_superuser:
            files = File.objects.all()
            context = {
                'files':files,
            }
            return render(request,'Lab1Files/admin-statistics.html', context=context)
        else:
            raise 404