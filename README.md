# CoinLuxe

Embrace the future of finance with CoinLuxe. Start your crypto journey today and unlock the potential of decentralized technologies.
The coinluxe website was designed to be a e-commerce where people can easily buy cryptos using credit or debit card. The motivation behind the creation of coinluxe was to facilitate the acquisition of cryptocurrencies at a small fee, making it an ideal place to buy cryptocurrencies.

# Strategy

By combining competitive fees, a user-friendly experience, secure transactions, a diverse cryptocurrency selection, and educational support, our crypto e-commerce platform is poised to become the ideal gateway for clients looking to enter the exciting world of cryptocurrencies and start their investment journey."

# Marketing

Our crypto e-commerce strategy is designed to provide an accessible and user-friendly platform for clients to purchase cryptocurrencies. We aim to empower our users to kickstart their investment journey in the crypto market by offering a diverse payment methods.

Key features of our strategy include:

    ### Competitive Fee Structure: We offer competitive fees that can be customized for each cryptocurrency. This flexibility ensures that clients can enjoy cost-effective transactions while trading a wide range of digital assets.

    ### User-Friendly Experience: Our platform is designed with simplicity in mind. We prioritize an intuitive and user-friendly interface, making it easy for both beginners and experienced traders to buy cryptocurrencies hassle-free.

    ### Secure Transactions: We prioritize the security of transactions. Clients can confidently use their credit or debit cards to make purchases, knowing that their financial data and investments are protected.

    ### Diverse Cryptocurrency Selection: We provide access to a diverse selection of cryptocurrencies, allowing clients to choose from a variety of digital assets to match their investment goals.



## Table of Contents

# UX Design


SITE GOALS:

1. Site Goal: Provide a user-friendly and visually appealing platform that engages and captivates users.
2. Site Goal: Offer comprehensive and accurate information about cryptocurrencies and related products to empower users in their decision-making process.
3. Site Goal: Ensure a secure and seamless user authentication process for account access and personalized features.
4. Site Goal: Streamline the account registration process, making it quick and hassle-free for new users.
5. Site Goal: Implement intuitive pagination functionality for the cryptocurrency and product lists, enabling easy navigation and improved user experience.
6. Site Goal: Safeguard user accounts by providing a secure and reliable password reset mechanism.
7. Site Goal: Personalize the shopping experience by granting logged-in users access to specific product pages.
8. Site Goal: Continuously enhance and optimize the platform to meet user needs and expectations in the dynamic cryptocurrency market.

USER GOALS:

1. User Goal: Visit Homepage for Platform Overview
   - Site Goal: Provide an engaging and informative overview of the platform, highlighting its key features and benefits.
2. User Goal: Explore List of Cryptocurrencies
   - Site Goal: Present a comprehensive and up-to-date list of cryptocurrencies, allowing users to gather information and make informed decisions about their investments.
3. User Goal: Browse Products and View Individual Product Pages
   - Site Goal: Showcase a wide range of products related to cryptocurrencies, enabling users to explore different offerings and access detailed information about each product.
4. User Goal: Log In to Account
   - Site Goal: Facilitate user authentication and secure access to personalized features and account-related functionalities.
5. User Goal: Sign Up for a New Account
   - Site Goal: Streamline the account creation process, enabling users to register and become members of the platform easily.
6. User Goal: Navigate Cryptocurrency List with Pagination
   - Site Goal: Enhance user experience by implementing pagination functionality, allowing users to navigate through the cryptocurrency list conveniently.
7. User Goal: Navigate Product List with Pagination
   - Site Goal: Improve user experience by implementing pagination functionality, enabling users to browse through the product list efficiently.
8. User Goal: Reset Account Password
   - Site Goal: Provide a straightforward and secure mechanism for users to reset their account passwords if they forget them.
9. User Goal: Access Specific Product Pages After Logging In
   - Site Goal: Grant logged-in users access to specific product pages, ensuring a seamless and personalized shopping experience.
10. User Goal: Navigate Cryptocurrency List with Pagination
    - Site Goal: Enable users to browse through the cryptocurrency list effortlessly using pagination, ensuring a smooth and efficient user experience.

## Design


### Images

The CoinLuxe website incorporates crypto images and crypto data obtained from Coingecko.com through the Coingecko API. To ensure real-time and  accurate information, the crypto data is updated every 10 minutes using a scheduler configured on the Heroku platform.

### Fonts

The fonts used in this project are system fonts

### Wireframes

**Original Wireframes** The original wireframes were scatched on paper during the design process. 

![homepage](https://github.com/cafalchio/coinluxe/media/readme/home.jpg)
![crypto_detail](https://github.com/cafalchio/coinluxe/media/readme/details.jpg)
![cryptos](https://github.com/cafalchio/coinluxe/media/readme/cryptos.jpg)


# Agile Methodology

Github projects was used to manage the project's tasks and issues. 

The link to the project's Github project board can be found [here](https://github.com/users/cafalchio/projects/7)

# Database Schema

PostgreSQL was used to create the database for this project. The database schema can be found below:

![SCHEMA](https://github.com/cafalchio/coinluxe/media/readme/all_models.png)

# Security

## User Authentication

Authentication was implemented using Django's built-in authentication system. The authentication system was used to create a custom user model that allows users to sign up and log in to the website. The authentication system was also used to create a custom admin model that allows admin users to log in to the admin site.

Decorators were used to restrict access to certain pages based on the user's role. The decorators used in this project are:

- @login_required: restricts access to the page to logged in users.
- @staff_member_required: restricts access to the page to admin users.

## Form Validation

For security purposes, form validation was implemented in the following forms:

- Login form
- Signup form

## Custom error pages:

Custom error pages were created for the following errors:

- 404 - (page not found): Page not found error occurs when the user tries to access a page that does not exist.

  This functionality ensures that the user is redirected to a custom error page when an error occurs.

# Features

The current features of the website are:

## Navbar

- The website has a navigation bar that allows users to navigate to different sections of the website.
- The navbar may include links to the home page, cryptocurrencies list, user account pages, and other relevant sections.

## Footer

- The website has a footer section that appears on every page.
- The footer may contain links to important pages, social media links, and copyright information.

## Home Page

- The home page serves as the main landing page of the website.
- It may provide an overview of the website's purpose, features, and highlights.

## User Account Pages

- The website includes user account functionality.
- Users can create an account, log in, and access their personalized account pages.
- Account pages may include features such as profile management, order history, and saved preferences.

## Cryptocurrencies List

- The website provides a list of cryptocurrencies.
- Users can browse through the available cryptocurrencies and access detailed information about each one.
- The list may include features such as sorting, filtering, and pagination for easy navigation.

## Pagination

- The pagination feature allows the user to navigate through the crypto list. T



## Search

- Search for a specific cryptocurrency.



## Crypto detail





## Add Product

## Update Product



## Delete Product



## Product Detail



## Buy Product



## Toast messages



## Error Page

# Business Model




# Marketing Strategy



## SEO



## Content marketing



## Social Media Marketing




## Email Marketing



# Testing

# Deployment

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

## Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

## Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']

- Push these changes to Github.

## Update Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                              |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                              |
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
| USE_AWS               | True (when AWS set up - instructions below)                                   |

## Deploy

To deploy the project, follow these simple steps:

- Ensure that DEBUG is set to False in your Django settings.
- Navigate to the deploy tab on Heroku and connect to your GitHub repository.
- Scroll down to the bottom of the deploy page and choose to either enable Automatic Deploys for automatic deployments, or select Deploy Branch to deploy manually. Note that manually deployed branches will need to be re-deployed each time the repository is updated.
- Click View to see your deployed site.
- Your site is now live and fully operational.

# AWS Set Up
## AWS S3 Bucket
To set up AWS S3 Bucket, follow these simple steps:

- Create an AWS account, if you don't already have one.
- Once logged in, navigate to the 'Services' tab on the AWS Management Console and search for 'S3'. Select it.
- Click 'Create a new bucket', give it a name (matching your Heroku app name if possible) and choose the region closest to you.
- Under 'Object Ownership', select 'ACLs enabled' and leave the Object Ownership as 'Bucket owner preferred'.
- Uncheck 'Block all public access' and acknowledge that the bucket will be public.
- Click 'Create bucket'.
- Open the created bucket and go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting', click 'edit' and enable the Static website hosting option. Copy the default values for the index and error documents and click 'save changes'.
- Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- In the 'Bucket Policy' section and select 'Policy Generator'.
- Choose 'S3 Bucket Policy' from the type dropdown.
- In 'Step 2: Add Statements', add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the popup that appears
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.


## IAM
- From the 'Services' menu, search IAM and select it.
- Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'. Choose a name and click 'Create'.
- Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Get the bucket ARN from 'S3 Permissions' as per above.
- Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```

- Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
- Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You need to create a user to put in the group. Select users from the sidebar and click 'Add user'.
- Give your user a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you created.
- Keep clicking 'Next' until you reach the 'Create user' button and click that.
- Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables as per above list and also in your env.py.


## Connecting S3 to Django 
- Go back to your IDE and install 2 more requirements:
    - `pip3 install boto3`
    - `pip3 install django-storages` 
- Update your requirements.txt file by typing `pip3 freeze --local > requirements.txt` and add storages to your installed apps.
- Create an if statement in settings.py 

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

```
- Then add the line 

    - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell django where our static files will be coming from in production.


- Create a file called custom storages and import both our settings from django.con as well as the s3boto3 storage class from django storages. 
- Create the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In settings.py add the following inside the if statement:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

- and then add the following at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

- Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Then under 'Permissions' select the option 'Grant public-read access' and click upload.
- Your static files and media files should be automatically linked from django to your S3 bucket.

# Languages

The main languages used to build this project are:

- HTML5: used to create the structure of the website.
- CSS3: used to style the website.
- JavaScript: used to add interactivity to the website.
- Python: used to build the backend of the website.

# Libraries

# Credits

https://picsvg.com/ 
https://www.youtube.com/watch?v=K1e8kpoag0E  
https://www.youtube.com/watch?v=miiPsBlqMns
https://tailwindcss.com/
https://www.khanna.law/blog/deploying-django-tailwind-to-heroku
https://looka.com
https://github.com/ecabanasv/ci-pp5-ecommerce

# Acknowledgments

# Disclaimer

This project is for educational purposes only. All the content of the website is fictional and it is not intended to be used for commercial purposes.

# License

This project is licensed under the Apache2 License  - see the LICENSE.md file for details.
