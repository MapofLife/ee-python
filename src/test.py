#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import ee
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('.properties')

MY_SERVICE_ACCOUNT = Config.get('Authentication', 'ServiceAccount')
MY_PRIVATE_KEY_FILE = Config.get('Authentication', 'PrivateKeyFile')

print "initializing..."
ee.Initialize(ee.ServiceAccountCredentials(MY_SERVICE_ACCOUNT, MY_PRIVATE_KEY_FILE))
print "initializing complete"
 
fc = (ee.FeatureCollection('ft:1Ec8IWsP8asxN-ywSqgXWMuBaxI6pPaeh6hC64lA')
      .filter(ee.Filter().eq('ECO_NAME', 'Sonoran desert')))
 
print fc.getInfo()
