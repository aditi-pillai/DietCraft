from django.shortcuts import render
#yy+fGlsQMnVpqS9gdGdatg==GTWbYZnLQoF3t1IH
# Create your views here.


def calorie_counter(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'yy+fGlsQMnVpqS9gdGdatg==GTWbYZnLQoF3t1IH'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'calories/calorie_counter.html', {'api': api})
    else:
        return render(request, 'calories/calorie_counter.html', {'query': 'Enter a valid query'})
        
# def calorie_counter(request):
#     return render(request, 'calories/calorie_counter_new.html')

def something(request):
    return render(request, 'calories/something.html')