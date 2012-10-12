'''
Created on Oct 9, 2012

@author: kykamath
'''
#! /opt/local/bin/python
from library.classes import GeneralMethods
from library.file_io import FileIO
from xml.etree import ElementTree
import os
import re
import sys

def convert_row_to_dict(row):
    #try:
        for tag in ['Location', 'Text', 'Comment', 'UserDisplayName', 'AboutMe', 'DisplayName', 'Title']:
            row = re.sub('%s="( )*'%tag, '%s="'%tag, row)
        data = {}
        for c in row[5:-2].split('" '):
            if c:
                c+='"'
                if c[-2]=='=': c = c[:-2]+'= "'
                print c
                key, value = c.split('="')
                value=value[:-1]
                data[key] = value
        if data: return data
    #except Exception as e:
        #print 'Caught expection', e
        #pass
    
def convert_file_to_json(input_file, output_file):
    output_file=output_file[:-3]+'json'
    for line in FileIO.iterateLinesFromFile(input_file):
        if line[:4]=='<row': 
            data = convert_row_to_dict(line)
            if data: FileIO.writeToFileAsJson(data, output_file)

def convert_file_to_json_using_xml(input_file, output_file):
    rows = ElementTree.iterparse(input_file)
    for event, row in rows:
        if row.tag=='row':
            data = dict(row.items())
            if data: FileIO.writeToFileAsJson(data, output_file)

def copy_file(input_file, output_file):
    command = 'cp %s %s'%(input_file, output_file)
    GeneralMethods.runCommand(command)

def is_xml(file_name): return file_name[-3:]=='xml'

if __name__ == '__main__':
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    for file in os.listdir(input_dir):
        input_file = input_dir+'/%s'%file
        output_file = output_dir+'/%s'%file
#        if is_xml(input_file): convert_file_to_json(input_file, output_file)
        if is_xml(input_file): convert_file_to_json_using_xml(input_file, output_file)
        else: copy_file(input_file, output_file)
        
