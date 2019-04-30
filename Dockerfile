FROM python:3.7
ADD AllFunctions.py /var/lib/docker/volumes/pyvol/_data/Programs/
ADD UserDataCollections_working.py /sud/
RUN apt-get update && apt-get install vim -y
RUN pip install pystrich
RUN pip install pymongo
EXPOSE 8081
CMD [ "python", "/var/lib/docker/volumes/pyvol/_data/Programs/UserDataCollections_working.py" ]
