 FROM python:3
 ADD AllFunctions.py /sud/
 ADD UserDataCollections.py/sud/
 RUN pip install pystrich
 RUN pip install pymongo
 CMD [ "python", "/sud/UserDataCollections_working.py" ]
