from django.shortcuts import render
from main.models import Feedback
# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        BOT_TOKEN = "6598966305:AAFeSGzxWV6ersCQ4bNfcZxXLuoMMeSK9TI"
        TELEGRAM_CHAT_ID = "610795666"
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        feedback = Feedback(name=name, phone=phone)
        feedback.save()
        message = f"Новый клиент\nИмя: {name}\nНомер: {phone}"
        response = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
        from django.shortcuts import redirect

        return redirect('/')

    return render(request, 'vebi.html',{})