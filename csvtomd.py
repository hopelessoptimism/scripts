'''
Run from the command line with arguments of the CSV files you wish to convert.  
There is no error handling so things will break if you do not give it a well 
formatted CSV most likely.

USAGE: python csvtomd.py [first_file.csv] [second_file.csv] ...

OUTPUT: creates a directory for each CSV file, and for each row
        of the CSV it creates a corresponding Markdown file.

NOTE: Produces N directories and M files
      where N = # of CSV files
      and M = total number of rows across files

WARNING: M could be a potential large number, keep this in mind
'''

import sys
import csv
import os
import re
import shutil

for arg in sys.argv[1:]:
    dir_name = arg.split(".")[0] + "_markdown"
    
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    
    # create a directory to store the results
    os.mkdir(dir_name)
    
    # read in CSV file
    with open(arg, 'rb') as f:
            reader = csv.reader(f)
            
            # strip off CSV header for names of markdown headers
            header = reader.next()
            
            # parse through each record/row and convert to markdown
            for row in reader:
              
                if len(row) > 0:
                        # change this depending on your file layout.  
                        # This is what field the markdown files will be named with.
                        name = re.sub('\s', r'_', row[1]).lower()
                        
                        # create a new markdown file
                        with open(dir_name + "/" + name + ".md", 'wb') as md:
                        
                            # associate each new field with the associated column header
                            entry = zip(header, row)
                            
                            for datum in entry:
                                md.write("## " + datum[0] + "\n")  
                                md.write(datum[1] + "\n\n")
