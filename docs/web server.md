# Zoomie | Web Server

# What is the Web UI?
Zoomie exposes a web ui on localhost:8000/ for a user to talk to through a browser using Zoomie APIs

# How can I disable the Web UI?
The web server is on by default, however if you don't want it to be, you can change it in the config.toml file, and change the following line and make it false.
```toml
enableWebUi = true
```

# Can I change the Web UI as I like?
Yeah, if you change the files in the www folder, this will also change it on the Web UI/localhost:8000