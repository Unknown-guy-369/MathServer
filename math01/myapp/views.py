from django.shortcuts import render
def lamp_power(request):
    context = {}
    context['power'] = ""
    context['I'] = ""
    context['R'] = ""  

    if request.method == 'POST':

        I = float(request.POST.get('intensity', '0')) 

        R = float(request.POST.get('resistance', '0')) 
        
        power = (I*I)*R
       
        context['power'] = f"{ power:.2f}"
        
        context['I'] = I
        
        context['R'] = R
        
        print(f"POST method is used")
        print(f"request= {request}")
        print(f"Intensity = {I}")
        print(f"Resistance = {R}")
        print(f"Power = {power}")
    
    return render(request, 'math.html',context)