from django.shortcuts import render
import random
import time

# Create your views here.

specialslist = ["Chicken Parmigiana", "Chicken Piccata", "Salmone Arrosto", "Lamb Scottadito"]
specialsprice = ["$31.99", "$31.99", "$34.99", "$31.99"]

def main(request):
    '''directs application to main page html'''
    template_name = "restaurant/main.html"
    return render(request, template_name)

def order(request):
    template_name = "restaurant/order.html"
    r = random.randint(0,3)
    context = {
    "special": specialslist[r],
    "sprice":  specialsprice[r],
    }
    print(context)

    return render(request, template_name, context)

def confirmation(request):
    template_name = "restaurant/confirmation.html"

    # # read the form data into python variables:
    if request.POST:
 
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        sinstructions = request.POST['Special Instructions']
        items = request.POST.getlist('items')
        flavors = request.POST.getlist('flavors')

        total = 0
        if 'Chicken Wings' in items:
            total += 20.99
        if 'Boston Bibb' in items:
            total += 14.99
        if 'Spaghetti alle Vongole Macchiato' in items:
            total += 29.99
        if 'Chicken Parmigiana' in items:
            total += 31.99
        if 'Chicken Piccata' in items:
            total += 31.99
        if 'Salmone Arrosto' in items:
            total += 34.99
        if 'Lamb Scottadito' in items:
            total += 31.99

        r = random.randint(30,60)
        curtime = time.time() + r*60
        time_string = time.strftime('%I:%M:%S %p', time.localtime(curtime))

        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'items': items,
            'total': total,
            'time_string': time_string,
            'flavors' : flavors,
            'sinstructions': sinstructions
        }


        print(items)
    return render(request, template_name, context)
