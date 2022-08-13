# LANGUAGE TRANSLATOR API

![alt text](http://nyxcore.com/wp-content/uploads/2017/01/Mulang_Banner.jpg)

## Description

Language translator api helps translate a language.
The API uses the [T5-base-model](https://huggingface.co/t5-base) from huggingface.co to
translate languages and [HappyTransformer](https://happytransformer.com/text-to-text/) for both
Model initialization and tokenization

During training or initialization of the model through HappyTransformer's HappyTextToText Model

```python
    from happytransformer import HappyTextToText
    # --------------------------------------#
    model = HappyTextToText("T5", "t5-base", load_path=Model_path)
    ## Model_path is the location of the directory that contains the necessary files to form a model
```

Steps to setup Model_path

```bash
    mkdir model
    cd model
    wget https://huggingface.co/t5-base/blob/main/config.json .
    wget https://huggingface.co/t5-base/blob/main/spiece.model .

    wget https://huggingface.co/t5-base/blob/main/tokenizer.json .

    wget https://huggingface.co/t5-base/blob/main/pytorch_model.bin .

```

**Note** To Run the application set an Environment variable.

```bash
    export MODEL_PATH="location of the model u created"
    uvicorn main:app --reload --port 8080 --host 0.0.0.0
```

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
