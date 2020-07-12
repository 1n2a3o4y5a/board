from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'})

        except:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some':100})

        
    else:
        return render(request, 'signup.html', {'some':100})