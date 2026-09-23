from django.shortcuts import render
import random
import time

# Create your views here.

#David Chung
#dwjchung@bu.edu
#this is our views file, containing functions for each major component of our restuarant app
specialslist = ["Chicken Parmigiana", "Chicken Piccata", "Salmone Arrosto", "Lamb Scottadito"]
specialsprice = ["$31.99", "$31.99", "$34.99", "$31.99"]

def main(request):
    #our main views function can just return the template for our main page
    '''directs application to main page html'''
    template_name = "restaurant/main.html"
    return render(request, template_name)

def order(request):
    #the order views function will take a randomized special and its corresponding price from the list above
    #in addition itll render our order.html file
    template_name = "restaurant/order.html"
    r = random.randint(0,3)
    context = {
    "special": specialslist[r],
    "sprice":  specialsprice[r],
    }
    print(context)

    return render(request, template_name, context)

def confirmation(request):
    #our confirmation page will render the html, as well as collect the POST information from 
    #the order form. Itll collect name,phone,email, any special instructions, items,
    #and flavors for chicken wings if they choose. This function will also hardcode and check
    #which food items are selected and compute the total for the order
    #in addition, itll also take a random time between 30 and 60 minutes and add it to our current
    #time for a projected order pickup time estimate. For some reason, the code is fine, and even
    #print statements show that the time is correctly being updated(I have screenshot proof!)
    #for some reason, the hour is not properly displayed.
    template_name = "restaurant/confirmation.html"

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
