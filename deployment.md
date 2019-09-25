### Local 
1. You need to clone this repository by running the following command:
    ```
    git clone https://github.com/krivanpeter/the-issue-tracker
   ```
2. After cloning the project you need to go into the folder in the terminal
3. After that you need to install all packages from requirements.txt by running the following command:
    ```
    pip install -r requirements.txt
    ```
4. Django does not support serving static files in production, so we need to the following:
    1. Install WhiteNoise
     ```
    pip install whitenoise
     ```   
    2. Be sure to add whitenoise to your requirements.txt file as well.
    3. Add the following code to your settings.py's middleware section:
        ```   
        'whitenoise.middleware.WhiteNoiseMiddleware',
        ```   
    4. Add the following to your setting.py
        ```   
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
        ```   
5. The next thing is to set up the settings:
    1. First you need to create a file with the name: env.py and import os
    2. Set up a secret key with pasting the following into env.py  
       ```
        os.environ.setdefault("SECRET_KEY", "WhatYouWant")
       ```
    3. Put the following at the top of your settings.py file:
        ```
       import env
        ```
    4. In settings.py delete all EMAIL configuration (at the end of file) and replace with this:
       ```
       EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
       ```
    5. In settings.py change the database settings to default:
        ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
       ```
    6. Replace 'Static files (CSS, JavaScript, Images)' section with the following:
        ```
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        STATICFILES_LOCATION = 'static'
        STATIC_URL = '/static/'
       
        MEDIAFILES_LOCATION = 'media'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        MEDIA_URL = '/media/'
        ```
6. Make migrations and migrate with the following codes:
     ```
    python manage.py makemigrations
    python manage.py migrate
     ```
7. To set up online payment you will need Stripe:
    1. Go to [Stripe](https://stripe.com/gb), create an account and log in
    2. Go to your dashboard and get your API keys
    3. Set the keys in your env.py by writing there the followings:
        ```
        os.environ.setdefault("STRIPE_PUBLISHABLE", "YourPublishableKey")
        os.environ.setdefault("STRIPE_SECRET", "YourSecretKey")
        ```
8. Run the application with following code:
    ```
   python manage.py runserver
    ```