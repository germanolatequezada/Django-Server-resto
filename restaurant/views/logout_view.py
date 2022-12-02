from django.contrib.auth import logout
from django.shortcuts import redirect
import traceback

def index(request): 
    print('logout')
    try:    
        logout(request)
    except Exception as e:
        traceback.print_exc()
    return redirect('/carta')