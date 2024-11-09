# Django REST framework tutorial

## Tutorial 1: Serialization

- `pygments` package - for code highlighting.
- First, define how to serialize and deserialize objects into representation (`json`) with serializers.
- `serializers.Serializer`
  - To explicitly define a serializer.
  - `create()` and `update()` define how fully fledged instances are created and modified when calling `serializer.save()`.
  - Includes validation flags similar to Django `Form` on the various fields, such as `required`, `max_length` and `default`.
- `serializers.ModelSerializer`
  - Can define a serializer by inferring it from a `Model`.
  - Shortcut for creating serializers.
- Working with Serializers:

  ```py
  # Serialize
  #   An object
  serializer = SnippetSerializer(snippet)
  serializer.data  # Python native datatypes (dict)
  content = JSONRenderer().render(serializer.data)  # byte string
  #   Querysets
  serializer = SnippetSerializer(Snippet.objects.all(), many=True)
  serializer.data  # Python native datatypes (dict)
  content = JSONRenderer().render(serializer.data)  # byte string

  # Deserialize
  import io
  stream = io.BytesIO(content)  # Initialize a byte stream for `JSONParser`.
  data = JSONParser().parse(stream)  # Python native datatypes (dict)

  # Save to database
  serializer = SnippetSerializer(data=data)
  # Check with validation flags.
  serializer.is_valid()
  # Similar to `cleaned_data` of Django `Form`. (Must call `is_valid()` first)
  serializer.validated_data
  serializer.save()

  # To inspect all the fields in a serializer instance.
  serializer = SnippetSerializer()
  print(repr(serializer))
  ```

- In summary, serializer is the **key component** in Django REST framework.

## Tutorial 2: Requests and Responses

### Request objects

- Introduce a `Request` object that extends the regular `HttpRequest`.

  ```py
  request.POST  # Only handles form data. Only works for 'POST' method.
  request.data  # Handles arbitrary data. Works for 'POST', 'PUT', and 'PATCH' methods.
  ```

### Response objects

- Introduce a `Response` object (type of `TemplateResponse`). It uses content negotiation to determine the content type.

  ```py
  return Response(data)  # Renders to content type as requested by the client.
  ```

### Wrapping API views

- Provides two wrappers for API views
  1. `@api_view` - function-based views.
  2. `APIView` - class-based views.
- To receive `Request` instances in your view.
- Adding context to `Response` objects. (Content negotiation)
- Handle `405 Method Not Allowed`.
- Handle `ParseError` when accessing `request.data` with malformed input.

### Pulling it all together

- No longer explicitly tying our requests or responses to given content type. `Request` and `Response` objects will handle the content type for us.

## Tutorial 3: Class-based Views

### Using mixins

- Advantage of using class-based views.
- For CRUD operations.
- `GenericAPIView` provide the core functionality and mixins to provide actions.
- Provides a set of already mixed-in generic views.
