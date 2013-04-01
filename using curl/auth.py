import urllib2
import json
import sys
from curl_request import *

##..............................Function Definitions.................................##


# authenticate(url, username, password)
# Sends a request to authenticate the credentials to the server
#
# param:
#   url -[string]- a url to designate the server and file to send the request
#   username -[string]- contains the username
#   password -[string]- contains the password
# return:
#   [string, string] - returns the authentication token recieved from the server and the service catalog
#
def authenticate(url, username, password):
    # create the json string containing the authorization information
    auth_str = {'auth': {'passwordCredentials': {'username': username, 'password': password}}};
    json_string = json.dumps(auth_str);

    # make the request and handle any exceptions
    try:
        results = send_json_request(url, json_string, [])
    except urllib2.HTTPError, e:
        sys.exit('\n\tURL:\t\t' + url + '\n\tUsername:\t' + username + '\n\tPassword:\t' + password + '\n\tError:\t\t' + str(e.code) + ' : ' + e.msg)
    except Exception:
        sys.exit('Could not authenticate.')

    # store the authentication token and service catalog
    auth_token = results['access']['token']['id']
    service_catalog = results['access']['serviceCatalog']

    return [auth_token, service_catalog]



