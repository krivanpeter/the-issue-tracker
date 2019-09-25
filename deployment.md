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
    4.  1. Create a SendGrid account [here](https://sendgrid.com/)
        2. Add these lines to your env.py
       ```
        os.environ.setdefault("EMAIL_HOST_USER", "your.username")
        os.environ.setdefault("EMAIL_HOST_PASSWORD", "your.password")
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
   
### Deploy to Heroku 
#### Prerequisites
1. You will need a Heroku account. If you don't have one, go and create it [here](https://www.heroku.com/)
2. You will need a Stripe account. If you don't have one, go and create it [here](https://stripe.com/)
3. You will need a SendGrid account. If you don't have one, go and create it [here](https://sendgrid.com/)
4. You will need an AWS account. If you don't have one, go and create it [here](https://aws.amazon.com/)
5. You need to install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
6. You need to install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

You need to have the first 3 steps of [Local](#Local) be done.
 
#### Deployment
1. Create a new heroku application. You can do that by going to [here](https://dashboard.heroku.com/apps),
and click on ,,New" then ,,Create new app"
2. In ,,Resources" of heroku add the ,,Heroku Postgress" to your addons
3. Open the addon, go to ,,Settings" and save your database's URI (You'll need it later).
4. Go to [Stripe](https://stripe.com/gb) and log in
    1. Go to your dashboard and get your API keys
    2. Save these keys, you'll need them later
5. Go to [AWS-Amazon](https://aws.amazon.com/) and log in
    1. Go to the [AWS Management Console](https://console.aws.amazon.com/console/home) then click on ,,S3"
    2. Create a new bucket and let it be public
    3. Open the bucket and go to ,,Properties" and choose ,,Static website hosting"
    4. After that choose ,,User this bucket to host a website" and give it the default index and error page
    5. Go to the ,,CORS Configuration" of ,,Permissions" tab, and copy-paste there the code below, then save it:
        ```
        <CORSConfiguration>
            <CORSRule>
                <AllowedOrigin>*</AllowedOrigin>
                <AllowedMethod>GET</AllowedMethod>
                <MaxAgeSeconds>3000</MaxAgeSeconds>
                <AllowedHeader>Authorization</AllowedHeader>
            </CORSRule>
        </CORSConfiguration>
        ```
    6. Go to ,,Bucket Policy" and copy-paste the code below, change the ,,Resource" part of the code to match your bucket, then save it:
        ```
        {
            "Version":"2012-10-17",
            "Statement":[{
              "Sid":"PublicReadGetObject",
                "Effect":"Allow",
              "Principal": "*",
              "Action":["s3:GetObject"],
              "Resource":["arn:aws:s3:::example-bucket/*"
              ]
            }
          ]
        }
        ```
    7. Go to ,,IAM" and create a new group and then go to ,,Policies".
    8. Clink on ,,Create policy", choose ,,Import managed policy" and import ,,AmazonS3FullAccess"
    9. Replace ,,Resource" of JSON to be the following, then click on ,,Review Policy":
        ```
        Resources:["arn:aws:s3:::example-bucket", "arn:aws:s3:::example-bucket/*"]
        ```
    10. Give a name to your policy and save it.
    11. Go to ,,Permissions" of ,,Group" and click on ,,Attach Policy" and select your created policy.
    12. Next, you need to create a new user with programmatic access to the group you created without any keys
    13. Download the .csv file
6. Go to your settings.py file and change the following to match your bucket name:
    ```
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    ```
7. In your settings.py change the ALLOWED_HOSTS to match your heroku app's url
     ```
    your-app-name.herokuapp.com
     ```
8. Go to ,,Settings" of heroku, click on ,,Reveal Config Vars" and then add all your environment variables.
    ```
    AWS_ACCESS_KEY_ID(from the .csv file you downloaded from AWS),
    AWS_SECRET_ACCESS_KEY(from the .csv file you downloaded from AWS),
    DATABASE_URL(what you saved at step 3),
    DISABLE_COLLECTSTATIC = 1,
    EMAIL_HOST_USER (your sendgrid username),
    EMAIL_HOST_PASSWORD (your sendgrid password),
    SECRET_KEY (anything you want),
    STRIPE_PUBLISHABLE (what you saved at step 4),
    STRIPE_SECRET(what you saved at step 4)
    ```
9. Collect all your static files and upload them to AWS
    1. You will need to create the env.py file and put the following there:
    ```
    import os

    os.environ.setdefault("SECRET_KEY", "anything you want")
    os.environ.setdefault("EMAIL_HOST_USER", "your sendgrid username")
    os.environ.setdefault("EMAIL_HOST_PASSWORD", "your sendgrid password")
    os.environ.setdefault("DATABASE_URL", "what you saved at step 3")
    os.environ.setdefault("AWS_ACCESS_KEY_ID", "from the .csv file you downloaded from AWS")
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "from the .csv file you downloaded from AWS")
    os.environ.setdefault("STRIPE_PUBLISHABLE", "what you saved at step 4")
    os.environ.setdefault("STRIPE_SECRET", "what you saved at step 4")
    ```
   2. Put the following at the top of your settings.py
   ```
    import env
    ```
   3. Run the following code then delete the env import from your settings.py
    ```
    python manage.py collectstatic
    ```
10. Next you need to push all your codes to heroku with the followings:
    ```
    $ heroku login
    $ git init
    $ heroku git:remote -a your-app-name
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master
    ```
11. Go to heroku and click on the ,,Open app" button