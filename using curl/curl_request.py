import urllib2
import json


# send_json_request(url, json_string, extra_headers)
# Sends a JSON formatted request to a server
#
# param:
#   url -[string]- a url to designate the server and file to send the request
#   json_string -[string]- contains any JSON formatted data to include
#   extra_headers -[array]- contains an array of extra headers to include
#       format:
#           [['header_1_name', 'value'], ['header_2_name', 'value'],...]
# return:
#   [object] - returns a decoded JSON response from the server
#
# No exceptions are caught here to give the user the option to handle each
# one differently.
#
def send_json_request(url, json_string, extra_headers):
    # create the request object and set some standard headers
    req = urllib2.Request(url)
    req.add_header('Accept', 'application/json')
    req.add_header("Content-type", "application/json")
    
    # set any extra headers
    for header in extra_headers:
        req.add_header(header[0], header[1])
        
    # set any extra data
    if json_string:
        req.add_data(json_string);
        
    # send the request
    res = urllib2.urlopen(req)
    
    # parse and return the results
    return json.loads(res.read())