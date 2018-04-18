# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .tasks import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from celery.result import AsyncResult
import json

# Create your views here.



x = 10
ncou = 2
ncon = 2
budget = 1000
duration = 40
origin = 'SFO'
list_airports = None
matrix = None
def poll_state(request):
    """ A view to report the progress to the user """
    data = 'Fail'
    global matrix
    if request.is_ajax():
        if 'task_id' in request.POST.keys() and request.POST['task_id']:
            task_id = request.POST['task_id']
            task = AsyncResult(task_id)
            data = task.result or task.state
            print(len(data))
            if len(data) == len(list_airports):
                matrix = np.array(data)


        else:
            data = 'No task_id in the request'
    else:
        data = 'This is not an ajax request'

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def index(request):
    global origin,ncou,ncon,list_airports

    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        data = job.result or job.state

        context = {
            'data':data,
            'task_id':job_id,
        }
        return render(request,"show_t.html",context)
    elif 'n' in request.GET:
        ncou = int(request.GET['n'])
        list_airports = choose_countries(origin, ncou, ncon)
        job = find_best_travel.delay(list_airports,duration,ncou)
        print(job.id)
        return HttpResponseRedirect(reverse('index') + '?job=' + job.id)
    else:

        return HttpResponse("ok1")

def test(request):
    global  matrix,list_airports,duration,origin
    test,cost = compute_optimal_tour(matrix,list_airports)
    return HttpResponse("itinerary : " + str(test + [origin]) + " cost : "+str(cost)+"$")