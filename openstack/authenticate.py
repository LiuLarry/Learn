#!/usr/bin/env python
# coding=utf-8

from os import environ as env

import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient

keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           tenant_name=env['OS_TENANT_NAME'],
                           region_name=env['OS_REGION_NAME'])

print keystone.auth_token

glance_endpoint = keystone.service_catalog.url_for(service_type='image')

glance = glclient.Client(glance_endpoint, token=keystone.auth_token)

print glance
