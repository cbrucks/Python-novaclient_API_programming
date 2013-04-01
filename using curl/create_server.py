import json
import pprint
import sys
import re
from curl_request import *


##..............................Function Definitions.................................##

# get_image_id_by_keyword(url, auth_token, keyword)
# Requests a list of images and finds the id of the first match to the keyword given
#
# param:
#   url -[string]- a url to designate the server and file to send the request
#   auth_token -[string]- the authentication token recieved from the server
#   keyword -[string]- the keyword(s) to search for
# return:
#   [string] - returns the id of the image found
#
def get_image_id_by_keyword(url, auth_token, keyword):
    # get the image list
    extra_headers = [['X-Auth-Token', auth_token]]
    try:
        image_list = send_json_request(url + '/images', '', extra_headers)
    except Exception, e:
        sys.exit(e)

    # show the image list
    #pprint.pprint(image_list)    # uncomment to see output

    # get image id from list
    try:
        image_id = [image['id'] for image in image_list['images'] if keyword in image['name']][0]
    except IndexError,e:
        sys.exit('Image name "' + image_name + '" does not exist')

    return image_id


# get_flavor_id_by_keyword(url, auth_token, keyword)
# Requests a list of flavors and finds the id of the first match to the keyword given
#
# param:
#   url -[string]- a url to designate the server and file to send the request
#   auth_token -[string]- the authentication token recieved from the server
#   keyword -[string]- the keyword(s) to search for
# return:
#   [string] - returns the id of the flavor found
#
def get_flavor_id_by_keyword(url, auth_token, keyword):
    # get the flavor list
    extra_headers = [['X-Auth-Token', auth_token]]
    try:
        flavor_list = send_json_request(url + '/flavors', '', extra_headers)
    except Exception, e:
        sys.exit(e)

    # show results
    #pprint.pprint(flavor_list)    # uncomment to see output

    # get flavor id from list
    try:
        flavor_id = [flavor['id'] for flavor in flavor_list['flavors'] if keyword in flavor['name']][0]
    except IndexError,e:
        sys.exit('Flavor size ' + flavor_size + ' does not exist')

    return flavor_id


# create_server(url, auth_token, name, image_id, flavor_id)
# Create a server
#
# param:
#   url -[string]- a url to designate the server and file to send the request
#   auth_token -[string]- the authentication token recieved from the server
#   name -[string]- the server name
#   image_id -[string]- the id of the desired image
#   flavor_id -[string]- the id of the desired flavor
# return:
#   [string, string] - returns the admin password and the server id
#
def create_server(url, auth_token, name, image_id, flavor_id):
    # get the flavor list
    extra_headers = [['X-Auth-Token', auth_token], ['X-Auth-Project-Id', 'test-project']]
    server_info = {'server':{'name':re.sub('\s', '_', name),'imageRef':image_id,'flavorRef':flavor_id,'metadata':{'My Server Name': name}}}
    json_string = json.dumps(server_info)
    try:
        server_response = send_json_request(url + '/servers', json_string, extra_headers)
    except Exception, e:
        sys.exit(e)

    # show results
    pprint.pprint(server_response)    # uncomment to see output

    # get the admin password and server id
    admin_pass = server_response['server']['adminPass']
    server_id = server_response['server']['id']

    return [admin_pass, server_id]
