import os
from dotenv import load_dotenv, find_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())

verify_token = os.environ['VERIFY_TOKEN']
page_access_token = os.environ['PAGE_ACCESS_TOKEN']
fb_url = os.environ['FB_URL']
main_url = 'http://videochat.herokuapp.com'


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'confidential top secret!'
    TRAP_HTTP_EXCEPTIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/accountant.db' % BASEDIR
    DEBUG = True
