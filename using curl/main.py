from auth import *
from create_server import *
import pprint


## ---------------------------------------- Authorization Token ---------------------------------------- ##

# initialize server options
username='cbrucks'
password='Tensor09'
url='https://identity.api.rackspacecloud.com/v2.0/tokens'
region = 'DFW'

# authenticate the credentials
[auth_token, service_catalog] = authenticate(url, username, password)

# get the cloud server endpoint for our region
cs_endpoints = [service['endpoints'] for service in service_catalog if (service['name'] == 'cloudServersOpenStack')]
cs_url = [endpoint['publicURL'] for endpoint in cs_endpoints[0] if endpoint['region'] == region][0]


## ---------------------------------------- Create Server ---------------------------------------- ##

image_name = 'Ubuntu 12.04'
flavor_size = '512MB'
server_name = 'Example Server'

# get the image id
image_id = get_image_id_by_keyword(cs_url, auth_token, image_name)

# get the flavor id
flavor_id = get_flavor_id_by_keyword(cs_url, auth_token, flavor_size)

# create the server
[admin_pass, server_id] = create_server(cs_url, auth_token, server_name, image_id, flavor_id)


## ----------------------------------------  ----------------------------------------