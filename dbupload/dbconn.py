import requests
import re
import mechanize
import dropbox

app_key = 'jmy9doyome57vcm'
app_secret = 'cxp1n63f06rww9y'

class DropboxConnection:
    """ Creates a connection to Dropbox """

    def __init__(self, uname, pwd):
        self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(
            app_key, app_secret)

        self.username = uname
        self.password = pwd
        self.session = requests.Session()

        self.login()

    def login(self):
        """ Login to Dropbox and return mechanize browser instance """

        # Fire up a browser using mechanize
        authorize_url = self.flow.start()

        # Browse to the login page
        page = self.session.get(authorize_url)._content

        token = re.findall(r"TOKEN: '(.+)'", page)[0]

        payload = {
            't': token,
            'cont': '',
            'login_email': self.username,
            'login_password': self.password,
            'is_xhr': 'true'
        }

        auth = requests.post('https://www.dropbox.com/ajax_login', params=payload)



        try:
            self.root_ns = re.findall(r'"root_ns": (\d+)', home_src)[0]
            self.token = re.findall(
                r'"TOKEN": "([a-zA-Z0-9_\-]+)"', home_src)[0]
        except:
            raise(Exception("Unable to find constants for AJAX requests"))

        code = ''

        access_token, user_id = self.flow.finish(code)

        self.client = dropbox.client.DropboxClient(access_token)

    def upload_file(self, local_file, remote_file_full_path):
        """ Upload a local file to Dropbox """

        with open(local_file, 'rb') as f:
            # TODO: Check (or assert) response
            self.client.put_file(remote_file_full_path, f)

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
