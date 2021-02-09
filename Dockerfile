FROM python:3
ADD monitorSystem.py /
ADD configurator.py /
ADD monitor/ /monitor/
ADD monitor.json /
RUN pip3 install ping3
CMD [ "python3", "./monitorSystem.py" ]

