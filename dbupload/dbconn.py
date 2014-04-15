import mechanize
import dropbox
import urllib2
import re
import json

app_key = ''
app_secret = ''

# I might use this --> https://github.com/PrincessPolymath/python-oauth2

class DropboxConnection:
    """ Creates a connection to Dropbox """

    def __init__(self):
        self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(
            app_key, app_secret)


        self.login()

    def login(self):
        """ Login to Dropbox and return mechanize browser instance """

        # Fire up a browser using mechanize
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        authorize_url = self.flow.start()

	print url

        # Browse to the login page
        self.browser.open(authorize_url)

        self.browser.forms = [i for i in self.browser.forms()][0]

        # Should I check return?
        self.browser.submit()

        # should find the text containing the token
        
        #

        code = ''

        access_token, user_id = self.flow.finish(code)

        self.client = dropbox.client.DropboxClient(access_token)

    def upload_file(self, local_file, remote_file_full_path):
        """ Upload a local file to Dropbox """

        with open(local_file, 'rb') as f:
            # TODO: Check (or assert) response
            client.put_file(remote_file_full_path, f)

    def get_dir_list(self, remote_dir):
        """ Get file info for a directory """

       raise NotImplemented("On version 0.2.1")

    def get_download_url(self, remote_dir, remote_file):
        """ Get the URL to download a file """

       raise NotImplemented("On version 0.2.1")

    def download_file(self, remote_dir, remote_file, local_file):
        """ Download a file and save it locally """

        raise NotImplemented("On version 0.2.1")


    def out(self):
        """
        This is highly experimental yet..
        """
        raise NotImplemented("On version 0.2.1")
