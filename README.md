# What is this?
To get a better understanding of Docker and FastAPI, I created a basic API using these two technologies. At the end of this page you can see the API in action.

You have a few endpoints to do CRUD operations on a fake database that is actually just a Python dictionary object.

You can return all courses, return a course by index within the dictionary, delete a course and reload/reset the dictionary to a set of 5 courses. The 5 courses are stored in a CSV file and loaded into a Pandas dataframe at the start of the application.

Since this is a very basic Docker learning project, here are also instructions on how to run the application on your machine.

# Build image
In the root directory of this project, run the following command:
`docker build -t fastapi-demo-app:1.0  .`

This will create an image based on the Dockerfile found in the current working directory (specified by the dot at the end of the command) and give it the tag name fastapi-demo-app, used for easier access.

To double-check that it worked use the following command to list your Docker images, you should find one named fastapi-demo-app with version number 1.0:
`docker image ls`

# Run container based on image
Now that you got the image, you can run a container based on it. To do so run the following command:
`docker run -d --name courses-api -p 5000:8000 fastapi-demo-app:1.0`

This will create and run a container named coursesapi and map port 8000 from within the Docker container to port 5000 on your machine, i.e. the mapping is Local:Container. Now if you access port 5000 on localhost, your request will be forwarded to within the Docker container listening on it.

Alternatively you can run `docker-compose up`. It will also start the container (under a different name) with the same port mapping specified in `docker-compose.yml`.

# In real life...

...you would typically PUSH your image onto a Docker image registry from where someone else can PULL it.

# Learning resources used / Credits
- Why did we choose FAST API over Flask and Django for our RESTFUL#
Micro-services: https://ahmed-nafies.medium.com/why-did-we-choose-fast-api-over-flask-and-django-for-our-restful-micro-services-77589534c036

- FastAPI [ Python Web Framework ] Crash Course 2021 For Beginners: https://www.youtube.com/watch?v=62pP9pfzNRs

- Fast API crash course | easy way: https://www.youtube.com/watch?v=TQfIUS52QHA&t=1413s

- Learn Docker in 7 Easy Steps - Full Beginner's Tutorial: https://www.youtube.com/watch?v=gAkwW2tuIqE

- Deploy with Docker - FastAPI: https://fastapi.tiangolo.com/deployment/docker/


# Demo app in action

![Alt Text](https://i.imgur.com/1tO3tf5.gif)
