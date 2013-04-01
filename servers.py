from novaclient import OpenStack

username = 'username'
password = 'password'
auth_url = 'https://identity.api.rackspacecloud.com/v2.0/tokens'

nova = OpenStack(username, password, auth_url)