# Zoomie

Zoomie is a python script/app that allows you to host a server so you can access Apple Foundation Models on other devices, or as an API for stuff like Apple XCode

## Important Note!
1. I cannot at all build the app. I'm still looking into it. If you came from Stardance, please look at the newest dev log ("Regarding feedback")
2. Zoomie will ONLY work on Macs with support for Apple intelligence. This is because of Apples requirements for Apple Foundation Models.

## Installation

To begin using Zoomie server, download the contents of this github repo, and open a terminal in the unzipped folder. Next, run the following command:
```bash
pip install -r requirements.txt
```
Please note that if it throws an error about apple_fm_sdk, you may not have XCode installed, which is required. Or, you have an old version of Python which is not compatible. After you complete that, run in a terminal/ide web.py. 

## Usage
To use Zoomie go to https://localhost:8000/, and you should see a (very basic as of right now) page where you can interact with the AI. You can even access it from other devices if you know your Macs IP.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

See license tab
