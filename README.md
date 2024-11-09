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
  serializer.is_valid()  # Check with validation flags.
  serializer.validated_data  # Similar to `cleaned_data` of Django `Form`. (Must call `is_valid()` first)
  serializer.save()

  # To inspect all the fields in a serializer instance.
  serializer = SnippetSerializer()
  print(repr(serializer))
  ```

- In summary, serializer is the **key component** in Django REST framework.
