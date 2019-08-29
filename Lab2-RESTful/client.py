''' Tai Doan - Huyen Nguyen
    CPE 4750 - Lab2: RESTful Service
    This program designs a client to access our RESTful service on Firebase about Soccer teams' information
'''

import http.client
import json

'''
    Call HTTP method on a secure connection.  Currently, only GET is supported.
    Parameters: an HTTPSConnection, the method to use, list of arguments
    Returns: the response
    '''
def get_response(c, method, url, method_args):
    # REST endpoints requires appending .json
    url = url + ".json"
    if method == 'GET':
        c.request(method, url)
    else:
        print("Invalid HTTP method!")
        exit()
    
    return c.getresponse()

'''
    Process the HTTP response.
    Parameters: an HTTPResponse
    Returns: the JSON object, converted to a Python dictionary
    '''
def process_response(res):
    
    #Response should be `200 OK`, or we quit
    if res.status != 200:
        print(res.status, ' ', res.reason)
        exit()

    #ops holds json (in a string)
    ops = response.read().decode()
    
#convert json to dictionary and return
    return json.loads(ops)


'''
    Access to the top level of the database
'''
#accessing Firebase Real-Time Database via
toplevel = '/Soccer_teams'
#open connection to Firebase Real-time Database
conn = http.client.HTTPSConnection('tdoan-assignment2.firebaseio.com')
#GET request for top-level JSON object -- a set of links
response = get_response(conn, 'GET', toplevel, None)

ops_dict = process_response(response)

'''
    The loop allows the client to access deeper level of the database
'''
while True:
    #open connection to Firebase Real-time Database
    conn = http.client.HTTPSConnection('tdoan-assignment2.firebaseio.com')
    #GET request for top-level JSON object -- a set of links
    response = get_response(conn, 'GET', toplevel, None)
    
    '''
    If the client reaches the endpoint -- the object's type is not dict,
    print out the JSON and exit.
    Otherwise, keep looping
    '''
    if not isinstance(ops_dict,(dict,)):
        print(ops_dict," is an important player of the team!")
        print("Good bye!")
        exit()
    
    print('Valid operations are: ')
    i = 0

    #print list of options from dictionary; value is a link
    for op_key, op_value in ops_dict.items():
        print(i, '.', op_key)
        i = i + 1

    choice = -1
    while choice < 0 or choice > len(ops_dict) - 1:
        choice = int(input('Choose wisely... '))

    #Update the top-level JSON object
    toplevel = toplevel + "/" + list(ops_dict.keys())[choice]
    print("URL: ",toplevel)

    '''
    Open a new connection to the database and
    perform GET request based on user's choice
    '''
    conn = http.client.HTTPSConnection('tdoan-assignment2.firebaseio.com')
    response = get_response(conn, 'GET', toplevel, None)
    ops_dict = process_response(response)

