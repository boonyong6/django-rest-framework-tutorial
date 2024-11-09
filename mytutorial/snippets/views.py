from http import HTTPMethod, HTTPStatus
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request: HttpRequest):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == HTTPMethod.GET:
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == HTTPMethod.POST:
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@csrf_exempt
def snippet_detail(request: HttpRequest, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=HTTPStatus.NOT_FOUND)

    if request.method == HTTPMethod.GET:
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == HTTPMethod.PUT:
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    elif request.method == HTTPMethod.DELETE:
        snippet.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
