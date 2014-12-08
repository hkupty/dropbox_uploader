pydropbox
=========

[![Code Health](https://landscape.io/github/hkupty/pydropbox/master/landscape.svg)](https://landscape.io/github/hkupty/pydropbox/master)

This project is born out of the need to automatically upload documents to dropbox.

This is orignially forked from https://github.com/c0ding/dropbox_uploader, but this diverged a lot from the original project in the internals.

This is in constant evolution yet, so it's not safe for production uses.

The desired architecture is to use mechanize + dropbox API, but I might experiment something like oauth + requests.
Anyhow, I can't escape the use of two libs for:
  1. There is no way to bypass (F*#!ng) Oauth, so we'll have mechanize or oauth handling it.
  2. The API itself is rest (or kinda), so if dropbox API is not decent enough, I'll end up with requests doing all the work.
  
If, for any reason, you like me and would like to help this project, you can send me some tips here:
194WfkjPahe3v46RM6NK9ncCZRNEU5KRg9
