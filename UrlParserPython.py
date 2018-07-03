# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:59:14 2018

@author: Kjell
"""
import parsers as parsers

url = 'http://username:password@hostname/path?arg=value&arg2=value2&arg3=value3#anchor'

parsedURL = dict({"[scheme]":parsers.schemeParser(url),
                  "[hostname]":parsers.hostnameParser(url),
                  "[username]":parsers.usernameParser(url),
                  "[password]":parsers.passwordParser(url),
                  "[path]":parsers.pathParser(url),
                  "[query]":parsers.queryParser(url),
                  "[fragment]":parsers.fragmentParser(url)})

print("Prints the parsed URL: \n", parsedURL)

print("\nPrints the query part: \n", parsers.queryParserArray(parsedURL.get("[query]")))
