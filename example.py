from dbupload import DropboxConnection
from getpass import getpass

try:
    # Create the connection
    conn = DropboxConnection("martin.simon@email.com", "natalia2602")
    
    # Upload the file
    conn.upload_file("/tmp/13.09.2012-23:28:35.tar.bz2","/backup","13.09.2012-23:28:35.tar.bz2")
except:
    print("Upload failed")
else:
    print("Uploaded file to your Dropbox")

