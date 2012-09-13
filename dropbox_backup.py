#!/usr/bin/env python

#********************************* README **************************************

# 0) DESCRIPTION:


# On invocation, the script creates a snapshot of ORIG_DIR's contents and writes

# it to BACKUP_DIR into 1) a new subdirectory or 2) a .tar.bz2 archive. 

#The time of snapshot creation is written into the

# subdirectorie's name / archive file name. An optional second location can

# be defined to which the snapshot will be written additionally.


# This script is useful to manually and quickly create snapshots of a multi-file

# project you're working on, enabling _rollbacks_ to an older version of your

# project's files. Furthermore, using the additional backup location on another

# physical storage, the script prevents _data loss_.


# 1) USAGE:


# Download and install Python 2.7.x: http://python.org/download/


# Put the script file into the directory containing the directory you want to

# back up, adjust settings (below) and then run the script (doubleclick on Win).


# The snapshot/backup of

#  ./ORIG_DIR/*

# will go to

#  ./BACKUP_DIR/BACKUP_PREFIX_timestring/*       (SIMPLE method, built-in)

# OR to the archive

#  ./BACKUP_DIR/BACKUP_PREFIX_timestring.tar.bz2 (BZ2 method, built-in)

# Of course, ORIG_DIR and BACKUP_DIR can be absolute paths, too. Then, the

# location of this script does not matter.


# 2) SETTINGS:


# always use SLASHES ("/") in paths, even on Windows -> don't use "\"

ORIG_DIR = "/home"          # e.g. "." or "/home/user/"

BACKUP_DIR = "/root/dropbox_uploader"        # e.g. "/home/user/backup"

BACKUP_PREFIX = ""          # e.g. "user_bck"


# choose backup method: 'SIMPLE' OR 'BZ2':

#METHOD = 'SIMPLE'  # copy directory tree; e.g. if you don't have many files..

METHOD = 'BZ2'      # builtin method; if you like compression,


# set ADDITIONAL_BACKUP_DIR to double-save backup (e.g. on another hard disk)

#(outcomment the next line if this is desired behavior)

#ADDITIONAL_BACKUP_DIR = ""   # e.g. "/tmp"

#*******************************************************************************

import os
import time 
import shutil
import sys 
import tarfile 
import subprocess
import traceback
from dbupload import DropboxConnection
from getpass import getpass



def backup_directory_simple(srcdir,dstdir):

    if os.path.exists(dstdir):

        exit_stop("backup path %s already exists!" % dstdir)

    try:

        shutil.copytree(srcdir,dstdir)

    except:

        print "Error while copying tree in %s to %s" % (srcdir,dstdir)

        print "Traceback:\n%s"%traceback.format_exc()

        return False

    return dstdir



def backup_directory_bz2(srcdir,tarpath):

    if os.path.exists(tarpath):

        exit_stop("backup path %s already exists!" % tarpath)

    try:

        tar = tarfile.open(tarpath, "w:bz2")

        for filedir in os.listdir(srcdir):

           tar.add(os.path.join(srcdir,filedir),arcname=filedir)

        tar.close()

    except:

        print "Error while creating tar archive: %s" % tarpath

        print "Traceback:\n%s"%traceback.format_exc()

        return False

    return tarpath



def so_flushwr(string):

    sys.stdout.write(string)

    sys.stdout.flush()



# build timestring, check settings and invoke corresponding backup function

print ""

print "*********************************************************************"

print "* DropBox Backup script v.0.1a (very early alpha)                   *"

print "*                                                   created by c0da *"

print "*                                                    SEPTEMBER 2012 *"

print "*********************************************************************\n"


timestr = time.strftime("%d.%m.%Y-%H:%M:%S",time.localtime())

if METHOD not in ["SIMPLE", "BZ2"]:

    exit_stop("METHOD not 'SIMPLE' OR 'BZ2'")

if not os.path.exists(ORIG_DIR):

    exit_stop("ORIG_DIR does not exist: %s" % os.path.abspath(ORIG_DIR))

if not os.path.exists(BACKUP_DIR):

    exit_stop("BACKUP_DIR does not exist: %s" % os.path.abspath(BACKUP_DIR))

else:

    print ("Writing snapshot of\n    %s\n to\n    %s\nusing the %s method...\n" %

            (os.path.abspath(ORIG_DIR),os.path.abspath(BACKUP_DIR),METHOD))

    if METHOD == "SIMPLE":

        rv = backup_directory_simple(srcdir=ORIG_DIR,

            dstdir=os.path.join(BACKUP_DIR, BACKUP_PREFIX + timestr))

    elif METHOD == "BZ2":

        rv = backup_directory_bz2(srcdir=ORIG_DIR,

            tarpath=os.path.join(BACKUP_DIR,

                BACKUP_PREFIX + timestr + ".tar.bz2"))


if rv:

    print "Snapshot successfully written to\n  %s\n" % os.path.abspath(rv)

else:

    print "Failure during backup :-("


head, tail = os.path.split(os.path.abspath(rv))


try:
    conn = DropboxConnection("dropbox.email", "dropbox.password")
    
    conn.upload_file(tail,"/backup",tail)

except:

        print ("*********************************************************************")

        print ("* Upload failed. Try again!                                         *")

        print ("*********************************************************************")

else:
	
	os.remove(tail)
	
        print ("*********************************************************************")  

        print ("* Succes! File uploaded to your Dropbox                             *")

        print ("*********************************************************************")

sys.exit
