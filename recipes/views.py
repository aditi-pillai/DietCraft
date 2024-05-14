from django.shortcuts import render

# Create your views here.
def recipes(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/recipe?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'yy+fGlsQMnVpqS9gdGdatg==GTWbYZnLQoF3t1IH'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'recipes/recipes.html', {'api': api})
    else:
        return render(request, 'recipes/recipes_new.html', {'query': 'Enter a valid query'})