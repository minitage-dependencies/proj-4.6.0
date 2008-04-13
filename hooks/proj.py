
import os,sys

def installmaps(options,buildout):
    # adding maps files
    os.system('cd nad')
    os.system('tar xzvf %s/maps/proj-datumgrid-1.3.tar.gz'% buildout['buildout']['directory'])
    os.system('cd ..')

