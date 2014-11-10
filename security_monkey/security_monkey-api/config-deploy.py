# Insert any config items here.
# This will be fed into Flask/SQLAlchemy inside security_monkey/__init__.py

LOG_LEVEL = "DEBUG"
LOG_FILE = "/var/log/security_monkey/security_monkey-deploy.log"

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:securitymonkeypassword@postgres:5432/secmonkey'

SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 15
ENVIRONMENT = 'ec2'
USE_ROUTE53 = False
FQDN = '<PUBLIC_IP_ADDRESS>'
API_PORT = '5000'
WEB_PORT = '443'
FRONTED_BY_NGINX = True
NGINX_PORT = '443'
WEB_PATH = '/static/ui.html'
BASE_URL = 'https://{}/'.format(FQDN)

SECRET_KEY = '<INSERT_RANDOM_STRING_HERE>'

MAIL_DEFAULT_SENDER = 'securitymonkey@<YOURDOMAIN>.com'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = False
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '<INSERT_RANDOM_STRING_HERE>'

SECURITY_POST_LOGIN_VIEW = WEB_PATH
SECURITY_POST_REGISTER_VIEW = WEB_PATH
SECURITY_POST_CONFIRM_VIEW = WEB_PATH
SECURITY_POST_RESET_VIEW = WEB_PATH
SECURITY_POST_CHANGE_VIEW = WEB_PATH

# This address gets all change notifications
SECURITY_TEAM_EMAIL = []

SECURITY_SEND_REGISTER_EMAIL = False
# These are only required if using SMTP instead of SES
EMAILS_USE_SMTP = False     # Otherwise, Use SES
MAIL_SERVER = 'smtp.<YOUREMAILPROVIDER>.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'securitymonkey'
MAIL_PASSWORD = '<YOURPASSWORD>'

