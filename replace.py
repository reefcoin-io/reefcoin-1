import os
import sys
import time
import subprocess

def renamefile(directory):
    for filename in os.listdir(directory): # parse through file list in the current directory
        #print "checking %s" % filename
        if filename.find(" ") >= 0: # if a space is found
            newfilename = filename.replace(" ","_") # convert spaces to underscores
            args = (['svn','mv',filename, newfilename]) # rename the file via svn mv
            subprocess.call(args, shell=False)
            filename = newfilename
        if os.path.isdir(filename):
            os.chdir(filename)
            space2_(".")
            os.chdir("..")