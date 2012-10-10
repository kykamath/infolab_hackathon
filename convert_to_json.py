'''
Created on Oct 9, 2012

@author: kykamath
'''
#! /opt/local/bin/python
from library.file_io import FileIO
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
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_file_to_json(input_file, output_file)