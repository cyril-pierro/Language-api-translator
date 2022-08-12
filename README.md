# LANGUAGE TRANSLATOR API

## Description

Language translator api helps translate a language.
The API uses the [T5-base-model](https://huggingface.co/t5-base) from huggingface.co to translate languages.

## How it works

The api takes three parameters namely:

1.  source_language
2.  destination_language
3.  input_text

**NOTE**: The source_language and destination_language only
accept values ["GERMAN", "ENGLISH", "ROMANIAN", "FRENCH"]

```python
    response = requests.post('localhost/api/v1/translate', data={
        'source_language': 'English',
        'destination_language': 'German'
        'input_text': 'Thank you for yesterdey'
        })
    print(reponse.json())
    >>> "{'translated_text': 'Vielen Dank für Ihre gestrige Wortmeldung'}"
```

## System Requirements and Tech Stack

| RAM | GPU | ML framework | Web Framework |
| :-: | :-: | :----------: | :------------ |
| 16G | VGA |   Pytorch    | FastAPI       |
