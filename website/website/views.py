from django.shortcuts import render
from django.http import HttpResponse
import json

def getArticles(request):
    myRes = {
        "date": "today 23:40"
    }

    jsonifiedRes = json.dumps(myRes)
    return HttpResponse(jsonifiedRes, content_type="application/json")

def getArticleDetails(request, article_id):
    return HttpResponse("This is an articles list")