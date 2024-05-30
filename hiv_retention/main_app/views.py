from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
plt.ioff()



def main(request):
    print('1')
    if request.method == 'POST':
        print('2')
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request , username = username , password = password)
        if User is not None:
            print('3')
            login(request, User)
           
            return redirect('dashboard') 
        else:
            print('6')
            messages.warning(request, 'Invalid Username and  Paasword')
            return redirect('sign_in')
                      
      
    return render(request , 'index.html')