
# Dockerfile, Image, container
FROM python:3.8
ADD hello_world.py .
#ADD any libraries necessary 
CMD ["python","./hello_world.py"]
