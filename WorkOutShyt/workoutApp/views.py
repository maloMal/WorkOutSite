from django.shortcuts import render
from models import Exercise, UserProfile

# Create your views here.


def index(request):
	exercise_list = Exercise.objects.order_by('name')
	context_dict = {}
	context_dict['exercises'] = exercise_list
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def exercise(request, exercise):
	context_dict = {}
	context_dict['result_list'] = None
	context_dict['query'] = None

	if request.method == 'POST':
		query = request.POST['query'].strip()
		if query: 
			result_list = run_query(query)
			context_dict['result_list'] = result_list
			context_dict['query'] = query
	try:
		exercise = ExerciseDone.objects.get(name=exercise)
		pages = Page.objects.filter(category=category)

		context_dict['category'] = category
		context_dict['pages'] = pages

	except Category.DoesNotExist:
		pass

	return render(request, 'category.html', context_dict)
	#return render(request, 'exercise.html', {})