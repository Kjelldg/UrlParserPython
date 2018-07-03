# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 22:25:32 2018

@author: Kjell
"""
import re as re

def schemeParser(url):
    scheme = url.split(":")[0]
    return scheme

def hostnameParser (url):
    hostname = re.match("^.*\\@(.*)\\/.*$", url)
    return hostname.group(1)

def usernameParser (url):
    username = re.match("^.*\\/(.*)\\:.*$", url)
    return username.group(1)

def passwordParser (url):
    password = re.match("^.*\\:(.*)\\@.*$", url)
    return password.group(1)

def pathParser (url):
    path = re.match("^.*\\/(.*)\\?.*$", url)
    return "/" + path.group(1)

def queryParser (url):
    query = re.match("^.*\\?(.*)\\#.*$", url)
    return query.group(1)

def fragmentParser (url):
    fragment = url.split("#")[-1]
    return fragment

def queryParserArray (query):
    queryParsed = re.findall("\\b([^\\&]+)=([^\\&]+)\\b", query)
    return queryParsed
