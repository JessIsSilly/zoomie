# Zoomie | API

# What is the API?
Zoomie exposes an API on localhost:8000/v1/*, and the type and address are in the documentation soon.

# APIS:
## /v1/chat/completions:
Type: **post**

Required arguments in body: **messages (string)**

About: This gets a response formatted in a way programs like Xcode will accept

## /v1/simple/getAiResponse:
Type: **post**

Required arguments in body: **messages (string)**

About: This returns the response in a simple and easy way, eg:
```json
{"response": "model response"}
```

extra: This is the method the web UI uses for its responses. Take a look at www/chat.js for an example

## /v1/models:
Type: **get**

Required arguments in body: **none**

About: This is another for programs like Xcode, this just returns about the model (Apple Foundation Model)

## /v1/zoomie/about:
Type: **get**

Required arguments in body: **none**

About: This will just return the version of Zoomie and afmChat
