# import the helpers from dbhelper to this file
from dbhelpers import conn_exe_close
# import json to send data as a string
import json 
# import flask to crete api
from flask import Flask

app = Flask(__name__)


# get request with the end point of /animals
@app.get('/animals')
def all_animals():
    # call the conn_exe_function
    results = conn_exe_close('call all_animals()',[])
    # after getting the correct result check for the data type
    # if the data is returned it will be in the form of list of tuples
    # if something is wrong then the data returned will not be a list
    if(type(results) == list):
        # if data is a list then stringify it and return it
        results_json = json.dumps(results, default=str)
        return results_json
    elif(type(results) == str):
        # if data returned is string i.e. if there is any error
        # then following message will get printed
        print('To proceed, please fix the error first')
    
    
all_animals()

@app.get('/dogs')
def all_dogs_species():
    # call the conn_exe_function
    results = conn_exe_close('call all_dog_species()',[])
    # after getting the correct result check for the data type
    # if the data is returned it will be in the form of list of tuples
    # if something is wrong then the data returned will not be a list
    if(type(results) == list):
        # if results are in the form of a list then it will stringify with json and return
        results_json = json.dumps(results, default=str)
        return results_json
    elif(type(results) == str):
        # else if not then following msg will get printed
        print('To proceed, please fix the error')


@app.get('/cats')
def all_cats_species():
    results = conn_exe_close('call all_cat_species()',[])
    # after getting the correct result check for the data type
    # if the data is returned it will be in the form of list of tuples
    # if something is wrong then the data returned will not be a list
    if(type(results) == list):      
        # it will stringify the data with a json and return it  
        results_json = json.dumps(results, default=str)
        return results_json
    elif(type(results) == str):
        # if results are not in a list then following msg will get printed
        print('To proceed , please fix the error')
app.run(debug=True)