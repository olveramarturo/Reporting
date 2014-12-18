##!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 18:16:21 2014
@author: Arturo Olvera
------------------------------------------------------
Description:
------------------------------------------------------
"""

def buildConnectionString(params):
    """ Build a DB connection string from a list of parameters
        returns a string """
    
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }

    print buildConnectionString(myParams)