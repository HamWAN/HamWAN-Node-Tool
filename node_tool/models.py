'''
Created on Mar 2, 2014

@author: ryan_turner
'''

from jinja2 import Environment, FileSystemLoader

class Configuration:
    def __init__(self, callsign, site, location, shared_administration, dhcp_client, route_cache):
        self.callsign = callsign
        self.site = site
        self.location = location
        self.shared_administration = shared_administration
        self.dhcp_client = dhcp_client
        self.route_cache = route_cache
        return
    def __repr__(self):
        env = Environment(loader=FileSystemLoader('templates/'))
        template = env.get_template('client.conf')
        template_vars = {'operators_callsign': self.callsign,
                'site_connecting_to': self.site,
                'operators_location': self.location,
                'shared_administration': self.shared_administration,
                'dhcp_client_on_lan': self.dhcp_client,
                'route_cache_bug_fix': self.route_cache
                }
        return template.render(template_vars)
    def __str__(self):
        return self.__repr__()