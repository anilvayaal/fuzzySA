# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 11:31:24 2014

@author: Anil
"""

import time
import datetime
import urllib2
from urllib2 import urlopen

website = 'http://csgv.org/blog/2014/human-side-sandy-hook-tragedy/'
topSplit = '<h3 class=\"headline\">The Human Side of the Sandy Hook Tragedy </h3>'
bottomSplit = '#comments ul { margin-left:0; padding: 0; }'

def main():
    try:
        src = urllib2.urlopen(website).read()
        # print src
        srcSplit = src.split(topSplit)[1].split(bottomSplit)[0]
        content = srcSplit.split('\n')
        for line in content:
            if '<p>' in line:
                print line
        
    except Exception, e:
        print "Error in main loop"
        print str(e)
        
main()
    