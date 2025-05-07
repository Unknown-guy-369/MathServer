# Ex.05 Design a Website for Server Side Processing

## Date:7/5/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
~~~py
math.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculator</title>
</head>
<style>
    body{
        background-image: linear-gradient(-20deg, #b721ff 0%, #21d4fd 100%);                    font-family: Arial, sans-serif;
            color: white;    }

    .BoxBody{
        display: flex;
        justify-content: center;
        margin-top: 100px;
    }
    .box{
        padding: 50px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.04);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        margin-bottom: 30px;
        box-shadow:0 15px 35px rgba(0,0,0,0.5);
    }
    input {
            margin-bottom: 10px;
            padding: 8px;
            border-radius: 8px;
            border: none;
            width: 100%;
        }

        button {
            margin: 10px 0;
            padding: 10px;
            border-radius: 8px;
            border: none;
            background-color: #fff;
            color: #333;
            cursor: pointer;
            margin-left:38% ;
        }

</style>
<body >
    <div class="BoxBody">
        <div class="box">
        <form  method="post">
            {% csrf_token %}
        <h1>Power Calculator</h1>
        <label >Intensity (A)</label>
        <input  value="{{I}}" name="intensity"><br>
        <label >Resistance (Ohm)</label>
        <input value="{{R}}" name="resistance"><br>
        <button type="submit">Calculate</button><br>
        <label >Power(watts)</label>
        <input name="power" value="{{power}}">
        </div>
        </form>
    </div>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lamp-power/', views.lamp_power, name="lamp_power"),
    path('', views.lamp_power, name="lamp_power_root")
]
~~~

## SERVER SIDE PROCESSING:
![alt text](image-1.png)

## HOMEPAGE:
![alt text](image.png)

## RESULT:
The program for performing server side processing is completed successfully.
