
import os,sys

def installmaps(options,buildout):
    # adding maps files
    os.system("""
cd %s/nad
tar xzvf %s/maps/proj-datumgrid-1.3.tar.gz
cd .. """ %( options['compile-directory'], buildout['buildout']['directory']))


