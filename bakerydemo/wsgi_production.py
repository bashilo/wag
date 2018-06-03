from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import os

import dotenv


dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
