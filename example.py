from dbupload import DropboxConnection
from getpass import getpass

try:
    # Create the connection
    conn = DropboxConnection("dropbox.email", "dropbox.password")
    
    # Upload the file
    conn.upload_file("file","/backup","file")
except:
    print("Upload failed")
else:
    print("Uploaded file to your Dropbox")

