# Zoomie

Zoomie is a python script/app that allows you to host a server so you can access Apple Foundation Models on other devices, or as an API for stuff like Apple XCode

## Important Note!
1. I cannot at all build the app. I'm still looking into it. If you came from Stardance, please look at the newest dev log ("Regarding feedback")
2. Zoomie will ONLY work on Macs with support for Apple intelligence. This is because of Apples requirements for Apple Foundation Models.

# Features:
Features of Zoomie include
* A Web Server/ui
* An API 

# Documentation
Documentation is available at [the docs folder](https://github.com/JessIsSilly/zoomie/blob/main/docs), or for specific things, see here:
* Web Server/ui: https://github.com/JessIsSilly/zoomie/blob/main/docs/web%20server.md
* API: https://github.com/JessIsSilly/zoomie/blob/main/docs/api.md

## Installation

To begin using Zoomie server, you have two options:
1. download the contents of this github repo, and open a terminal in the unzipped folder. Next, run the following command:
    ```bash
    pip install -r requirements.txt
    ```
    Please note that if it throws an error about apple_fm_sdk, you may not have XCode installed (install it from the Mac app store). Or, you have an old version of Python which is not compatible. After you complete that, run in a terminal/ide web.py. 


2. Use the executable found in releases inside the Zoomie.Mac.zip file. This should start successfully. If you have any issue starting Zoomie this way, please make me aware inside [Issues](https://github.com/JessIsSilly/zoomie/issues)
## Usage
To use the Zoomie web ui (if enabled) go to https://localhost:8000/, and you should see a (very basic as of right now) page where you can interact with the AI. You can even access it from other devices if you know your Macs IP. How ever if it is not enabled, please refer to the API documentation for more information about integrating Zoomie with anything.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## This project uses:
This project uses Apples Python Foundation Model sdk for communicating with the models. You can find information about it on Apples official GitHub repo here: https://github.com/apple/python-apple-fm-sdk

## License

See license tab for license information.
