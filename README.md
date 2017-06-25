codingkatas-mongodb-python
==========================

Solutions for the book "Coding Katas for MongoDB" solved with Python.


# Setup

## MongoDB with Docker

There are official Docker Images on the Dockerhub:
https://hub.docker.com/_/mongo/

You can start the Container with

```
docker run -p 27017:27017 -d mongo:3.4
```

## Python 

used Modules: pymongo, unittest

### Unit Test Framework

https://docs.python.org/3/library/unittest.html

Run all Unit Tests:

```
python -m unittest discover
```

Run only one Unit Test:

```
python3 -m unittest test/kata1/test_robofly_persistence.py
```