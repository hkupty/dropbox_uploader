from distutils.core import setup

setup(
    name='drobpx_upload',
    version='0.2.0',
    author='Henry "Ingvij" Kupty',
    author_email='hkupty@gmail.com',
    packages=['dbupload'],
    url='https://github.com/hkupty/dropbox_uploader',
    license='LICENSE.txt',
    description='Fairly simple dropbox backup script written in python',
    install_requires=[
        "mechanize >= 0.2.5",
        "dropbox >= 2.0.0"
    ],
)
