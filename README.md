# mac_addr_tool

Tool to query Macaddress.io api for Company Name of a Mac Address

## Run locally

```
$ git clone https://github.com/akrzos/mac_addr_tool
$ cd mac_addr_tool
$ virtualenv .venv; source .venv/bin/activate; pip3 install -r requirements.txt
$ vi .api_key
$ ./mac_addr_tool.py $(cat .api_key) 4F:3B:61:34:FD:E0
```

Alternatively provide your macaddress.io api key in the CLI rather than a file. Keep in mind that
doing so could end up keeping your API key in your shell history.

## Build/Run from Docker

```
$ git clone https://github.com/akrzos/mac_addr_tool
$ docker build -t mac_addr_tool mac_addr_tool/
$ vi .api_key
$ docker run mac_addr_tool $(cat mac_addr_tool/.api_key) 4F:3B:61:34:FD:E0
```
