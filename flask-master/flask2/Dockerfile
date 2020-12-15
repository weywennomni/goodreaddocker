# Contain the instructions on how to build the container 
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container /app where . is the relative directory AKA flask
ADD . /app

# Install the dependencies 
RUN pip install -r requirements.txt

# Install uswgi separately
RUN pip install uWSGI

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
