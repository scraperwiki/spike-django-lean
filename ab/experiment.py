from django_lean.experiments.models import Experiment, GoalRecord
from django_lean.experiments.utils import WebUser
from json import dumps

def gr(request, goalname):
    "Record a GoalRecord"
    try:
        GoalRecord.record(goalname, WebUser(request))
    except Exception as e:
        return dumps({'status': str(type(e)), 'error': str(e)})
    else:
        return '{"status": "okay"}'

def pirates_v_zombies(request, *args, **kwargs):
    if Experiment.test("pirates_v_zombies", WebUser(request)):
        view = pirates
    else:
        view = zombies
    return view(request, *args, **kwargs)

def pirates(request):
    return 

def zombies(request):
    return 
