# A86Monitor
A lightweight ping monitoring system that runs on ARM and x86 via Docker.

##Setup
In order to setup you need to create an image using the docker file. Once the container is running.
`sudo docker build -t a86monitor .`

You will need to get into the container

`sudo docker exec -it /bin/bash container_name`

This will remote you into the container and you will need to run the configurator

Run `python3 configurator.py`

This will run you through multiple prompts, before you add any targets make sure to configure the email servers first
and set the sender email/password. This may lead to issues if you do not have a valid email server set.

Once you configure all of your settings you can `exit` out of the docker container. 

You will need to restart the docker container 
`sudo docker restart container name`

Your done!
