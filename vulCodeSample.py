from django.http import HttpResponse
from flask import request, redirect, Response

@app.route('flask_redirect')
def flask_redirect():
    url = request.args["next"]
    return redirect(url)  # Noncompliant

@app.route('set_location_header')
def set_location_header():
    url = request.args["next"]
    response = Response("redirecting...", 302)
    response.headers['Location'] = url  # Noncompliant
    return response

def index(request):
    value = request.GET.get("value")
    response = HttpResponse("")
    response["Set-Cookie"] = value  # Noncompliant
    response.set_cookie("sessionid", value)  # Noncompliant
    return response
