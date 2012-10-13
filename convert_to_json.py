'''
Created on Oct 9, 2012

@author: kykamath
'''
from library.classes import GeneralMethods
from library.file_io import FileIO
from xml.etree import ElementTree
import os
import sys

def convert_file_to_json_using_xml(input_file, output_file):
    output_file=output_file[:-3]+'json'
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
        if is_xml(input_file): convert_file_to_json_using_xml(input_file, output_file)
        else: copy_file(input_file, output_file)
