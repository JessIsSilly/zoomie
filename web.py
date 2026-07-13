# IMPORTANT!
# This has only been tested on XCode, and Brave.
# I have NO idea how this works on anything else

import os
import sys
import about
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse, HTMLResponse
from fastapi.concurrency import run_in_threadpool
import uuid
import afmChat
import time
import json
import uvicorn
import platform
import tomllib

if getattr(sys, 'frozen', False):
    with open(os.path.join(sys._MEIPASS, "config.toml"), "r", encoding="utf-8-sig") as f:
        config = tomllib.load(f.read())
else:
    with open(os.path.join(os.path.dirname(__file__), "config.toml"), "r", encoding="utf-8-sig") as f:
        config = tomllib.load(f.read())

def isUserOnGoodEnoughVersion() -> bool:
    versionString = platform.mac_ver()[0]
    if not versionString:
        return False
    majorVar = int(versionString.split(".")[0])
    return majorVar >= 26

app = FastAPI()
afModels = afmChat.appleFoundationModels()

if not afModels.getIfFoundationModelsAvailable():
    print(f"Apple Foundation Models unavailable. Reason: {afModels.getFoundationModelUnavailableErrorMessage()}")
    quit()


@app.post("/v1/chat/completions")
async def chatCompletions(request: dict):
    global afModels

    stream = request.get("stream", False)

    print("posted /v1/chat/completions")

    messages = request.get("messages", [])
    if not messages:
        return JSONResponse(status_code=400, content={"Error": "No messages given"})

    print(messages)

    userPrompt = str(messages)

    if stream:
        async def streamEvent():
            responseInFull = await run_in_threadpool(afModels.askModelAndReturnResponse, userPrompt)

            chunk = {
            "id": f"chatcmpl-{uuid.uuid4()}",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": "apple-foundation-model_zoomie-server",
            "choices": [
                {
                    "index": 0,
                    "delta": {"role": "assistant", "content": responseInFull},
                    "finish_reason": "stop"
                }
                ]
            }

            yield f"data: {json.dumps(chunk)}\n\n"
            yield "data: [DONE]\n\n"

        return StreamingResponse(streamEvent(), media_type="text/event-stream")

    try:
        response = await run_in_threadpool(afModels.askModelAndReturnResponse, userPrompt)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"Error": "400 - Internal server error."})

    return {
        "id": f"chatcmpl-{uuid.uuid4()}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "apple-foundation-model_zoomie-server",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response
                },
                "finish_reason": "stop"
            }
        ]
    }

@app.post("/v1/simple/getAiResponse")
async def simpleGetAiResponse(request: Request):
    requestJson = await request.json()
    if not requestJson["message"]:
        print("no question")
        return {"response": "SYSTEM: No message provided"}

    question = requestJson["message"]
    response = await run_in_threadpool(afModels.askModelAndReturnResponse, question)

    return {"response": response}

@app.get("/v1/zoomie/about")
async def zoomieAbout():
    return {
        "version": about.version,
        "appleFoundationModelChatVersion": about.afmChatVersion
    }

@app.get("/v1/models")
async def getModels():
    # this is only here because xcode was whining
    return {
        "object": "list",
        "data": [
            {
                "id": "apple-foundation-model_zoomie-server",
                "object": "model",
                "created": 1700000000,
                "owned_by": "apple"
            }
        ]
    }

# WWW
@app.get("/{item:path}")
async def wwwGetPage(item: str):
    global config
    if not config["enableWebUi"]:
        return JSONResponse(status_code=403, content={"error": "disabled"})

    if getattr(sys, 'frozen', False):
        wwwRoot = os.path.join(sys._MEIPASS, "www")
    else:
        wwwRoot = os.path.join(os.path.dirname(__file__), 'www')
    requestedPath = os.path.realpath(os.path.join(wwwRoot, item))

    if (item == "/") or (item == ""):
        with open(os.path.join(wwwRoot, "index.html")) as page:
            return HTMLResponse(content=page.read(), status_code=200)

    if not requestedPath.startswith(os.path.realpath(wwwRoot) + os.sep):
        return JSONResponse(content={"error": "No :3"}, status_code=403)

    if not os.path.exists(requestedPath):
        return JSONResponse(content={"issue": "File not found"},
                            status_code=404)

    if not os.path.isfile(requestedPath):
        if not os.path.exists(os.path.join(requestedPath, "index.html")):
            return JSONResponse(content={"issue": "File not found"}, status_code=404)

        else:
            with open(os.path.join(requestedPath, "index.html")) as page:
                return HTMLResponse(content=page.read(), status_code=200)

    with open(requestedPath) as page:
        print(requestedPath)
        return HTMLResponse(content=page.read(), status_code=200)

if __name__ == "__main__":
    print("Starting Zoomie...")
    if not isUserOnGoodEnoughVersion():
        print("Your not on a new enough MacOS version, or your not using MacOS at all!"
              "\nYou must be using MacOS 26 or newer")
        time.sleep(30)
        exit(1)
    print(f"Zoomie version: {about.version}\nafmChat version: {about.afmChatVersion}")
    uvicorn.run(app, host="127.0.0.1", port=8000)