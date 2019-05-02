FROM python:3.7
ADD AllFunctions.py /sud1/
ADD UserDataCollections_working.py /sud1/
RUN apt-get update && apt-get install vim -y
# RUN pip install pystrich
RUN pip install pymongo
EXPOSE 8081
CMD ["python", "/sud1/UserDataCollections_working.py"]
