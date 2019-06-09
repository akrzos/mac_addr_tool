# Dockerfile for mac_addr_tool
FROM python:3

ADD mac_addr_tool.py /
ADD requirements.txt /

RUN pip3 install -r /requirements.txt

ENTRYPOINT [ "python", "./mac_addr_tool.py"]
