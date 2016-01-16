from django.shortcuts import render

def render_template(request, template):
    return render(request, template)
