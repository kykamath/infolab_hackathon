'''
Created on Oct 9, 2012

@author: kykamath
'''
#! /opt/local/bin/python
from library.file_io import FileIO
import os
import sys

def convert_row_to_dict(row):
    try:
        row = row.replace('\n', '')
        row = row.replace('\r', '')
        data = {}
        for c in row[5:-2].split('" '):
            if c:
                c+='"'
                key, value = c.split('="')
                value=value[:-1]
                data[key] = value
        if data: return data
    except Exception as e:
        print 'Caught expection', e
        pass
    
def convert_file_to_json(input_file, output_file):
    for line in FileIO.iterateLinesFromFile(input_file):
        if line[:4]=='<row': 
            data = convert_row_to_dict(line)
            if data: FileIO.writeToFileAsJson(data, output_file)

if __name__ == '__main__':
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
#    convert_file_to_json(input_file, output_file)
#    input_dir = '/Users/kykamath/Documents/workspace_sept_2012/infolab_hackathon/android_enthusiasts'
#    output_dir = '/Users/kykamath/Documents/workspace_sept_2012/infolab_hackathon/android_enthusiasts_json'
    for file in os.listdir(input_dir):
        input_file = input_dir+'/%s'%file
        output_file = output_dir+'/%s'%file
        convert_file_to_json(input_file, output_file)
        