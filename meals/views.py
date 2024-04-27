'''
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def generate_meal_plan(request):

    print(f"request: {request.POST}")

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date') 
        # hash = request.POST.get('hash')
        hash = 'f5b035dd6746035f6492df0a48c5b9aff8e31e94'
        api_key = 'fdef638ec29c4967a45f297845d7d440'
        # url = f'https://api.spoonacular.com/mealplanner/{username}/day/{date}?apiKey={api_key}&hash={hash}'
        # url = f'https://api.spoonacular.com/mealplanner/{username}/day/{date}?hash={hash}&apiKey={api_key}'
        url = f'https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey={api_key}&hash={hash}&username={username}&targetCalories=2000'
        headers = {'Content-Type': 'application/json','x-api-key': 'fdef638ec29c4967a45f297845d7d440'}
        response = requests.get(url, headers=headers)
        print(response.content)
        print(response)

        # if response.status_code == 200:
        #     meal_plan = response.json()
        #     # console log the meal plan
        #     print(meal_plan)
        #     return render(request, 'meals/meal_plan.html', {'meal_plan': meal_plan})
        # else:
        #     return HttpResponse('Error fetching meal plan')

        # try:
        #     meal_plan = response.json()
        #     # console log the meal plan
        #     print(meal_plan)
        #     return render(request, 'meals/meal_plan.html', {'meal_plan': meal_plan})
        # except Exception as e:
        #     return HttpResponse('Error fetching meal plan')
        try:
            api = json.loads(response.content)
            print(response.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'meals/meal_plan.html', {'api': api})
    else:
        return render(request, 'meals/meal_plan.html')


'''  
import requests
from django.shortcuts import render

def generate_meal_plan(request):
    if request.method == 'POST':
        username = 'aditipillai'
        hash = 'f5b035dd6746035f6492df0a48c5b9aff8e31e94'
        time_frame = request.POST.get('time_frame')
        api_key = 'fdef638ec29c4967a45f297845d7d440'
        target_calories = request.POST.get('target_calories')
        diet = request.POST.get('diet')
        exclude = request.POST.get('exclude')
        # url = f'https://api.spoonacular.com/mealplanner/generate?timeFrame={time_frame}&targetCalories={target_calories}'
        url = f'https://api.spoonacular.com/mealplanner/generate?timeFrame={time_frame}&apiKey={api_key}&hash={hash}&username={username}&targetCalories={target_calories}&diet={diet}&exclude={exclude}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            if time_frame == 'day':
                return render(request, 'meals/meal_plan_day.html', {'data': data})
            else: 
                return render(request, 'meals/meal_plan_week.html', {'data': data})
            
        else:
            error_message = f"Failed to generate meal plan: {response.text}"
            return render(request, 'meals/meal_plan_day.html', {'error_message': error_message})
    
    return render(request, 'meals/meal_plan_day.html')

    
