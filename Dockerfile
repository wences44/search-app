### Dockerfile 

# Created by Wences

# Pulling from base Python image 

FROM python:3.6.7-alpine3.6

# author of file
LABEL maintainer=”Wences”

# Set the working directory of the docker image 
WORKDIR /app
COPY . /app

# packages that we need
#RUN pip install package_name && \
#    pip install paackage_name2 

EXPOSE 8888

ENTRYPOINT ["python"]

CMD ["search.py"]
