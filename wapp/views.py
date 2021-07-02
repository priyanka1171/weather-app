from django.shortcuts import render
import requests
def home(request):
	if request.method == "POST":
		try:
			city=request.POST.get("city")
			a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2="&q="+city
			a3="&appid="+"166fb3da7431055da7f56c07eac79d04"
			wa=a1+a2+a3
			res=requests.get(wa)
			data=res.json()
			print(data)
			temp=data['main']['temp']
			desc=data['weather'][0]['description']
			msg=" City name :  " + str(city) + " temp :   " + str(temp) + "  description :  " + str(desc)
			icon="http://openweathermap.org/img/w/"+data['weather'][0]['icon']+".png"
			return render(request,"home.html",{"msg":msg,"icon":icon})
		except Exception as e:
			print(e)
			return render(request,"home.html",{"msg":"City name not found"})
	else:
		return render(request,"home.html")
