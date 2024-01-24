# CoinLuxe

### Deployed Website: https://coinluxe.herokuapp.com/

Embrace the future of finance with CoinLuxe. Start your crypto journey today and unlock the potential of decentralized technologies.
The coinluxe website was designed to be a e-commerce where people can easily buy cryptos using credit or debit card. The motivation behind the creation of coinluxe was to facilitate the acquisition of cryptocurrencies at a small fee, making it an ideal place to buy cryptocurrencies. 

# Strategy

By combining competitive fees, a user-friendly experience, secure transactions, a diverse cryptocurrency selection, our crypto e-commerce platform is the ideal gateway for clients looking to enter the exciting world of cryptocurrencies and start their investment journey. With the crypto industry valued at 
US$180 billion and increasing yearly, the coinluxe enters the market with a attractive alternative to crypto investment.

# Marketing

Our crypto e-commerce strategy is designed to provide an accessible and user-friendly platform for clients to purchase cryptocurrencies. We aim to empower our users to kickstart their investment journey in the crypto market by offering a diverse payment methods.

Key features of our strategy include:

* Competitive Fee Structure: We offer competitive fees that can be customized for each cryptocurrency. This flexibility ensures that clients can enjoy cost-effective transactions while trading a wide range of digital assets.

* User-Friendly Experience: Our platform is designed with simplicity in mind. We prioritize an intuitive and user-friendly interface, making it easy for both beginners and experienced traders to buy cryptocurrencies hassle-free.

* Secure Transactions: We prioritize the security of transactions. Clients can confidently use their credit or debit cards to make purchases, knowing that their financial data and investments are protected.

* Diverse Cryptocurrency Selection: We provide access to a diverse selection of cryptocurrencies, allowing clients to choose from a variety of digital assets to match their investment goals.

* Facebook campains to keep the user up to date and attract new users.

* Newsletter to inform and engage. We keep our users informed and always in contact with our regular newsletter.



## Table of Contents

# UX Design


Here's a table that lists the site goals and their corresponding user goals:

| Site Goal                                       | User Goal                                      |
|-------------------------------------------------|------------------------------------------------|
| Provide an engaging platform overview           | Visit Homepage for Platform Overview           |
| Present a list of cryptocurrencies              | Explore List of Cryptocurrencies              |
| Enable users to edit cryptocurrency information | Edit Crypto                                   |
| Allow admins to remove cryptocurrencies          | Remove Crypto                                 |
| Provide tools for managing cryptocurrency       | Manage Cryptos                                |
| Send confirmation emails                         | Receive Confirmation Email                   |
| Facilitate cryptocurrency withdrawals            | Withdrawal Crypto                             |
| Enable cryptocurrency purchases                  | Buy Cryptos                                   |
| Allow removal of items from a shopping bag       | Remove Crypto from Bag                        |
| Allow adding items to a shopping bag             | Add Crypto to the Shopping Bag                |
| Display historical price data                   | See Historical Prices                         |
| Provide detailed cryptocurrency information     | See Crypto Details                            |
| Present a comprehensive cryptocurrency list     | See Cryptocurrencies                          |
| Enable user login                               | Sign In                                      |
| Allow user logout                               | Log Out                                      |
| Provide a secure login process                   | Login                                        |
| Offer a wallet view                              | View Wallet                                 |
| Streamline the registration process              | Sign Up for a New Account                    |
| Allow registered users to log in                | Log In to Account                            |
| Offer product browsing and detailed views        | Browse Products and View Individual Product Pages |

## Design

A simple design to keep the focus on the list of cryptocurrencies and the information about it. 

With options of **Light Mode and Dark Mode**

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/home_light.png" width="800" alt="homepage light">
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/home_black.png" width="800" alt="homepage dark">

### Images

The CoinLuxe website incorporates crypto images and crypto data obtained from Coingecko.com through the Coingecko API. To ensure real-time and  accurate information, the crypto data is updated every 10 minutes using a scheduler configured on the Heroku platform.


### Fonts

The fonts used in this project are system fonts to keep the user style and increase loading speed.

### Wireframes

**Original Wireframes** The original wireframes were scatched on paper during the design process. 

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/home.jpg" width="300" alt="homepage">
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/details.jpg" width="300" alt="crypto_detail">
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/cryptos.jpg" width="300" alt="cryptos">

# Agile Methodology

Github projects was used to manage the project's tasks and issues. 

The link to the project's Github project board can be found [here](https://github.com/users/cafalchio/projects/7)

# Database Schema

PostgreSQL was used to create the database for this project. The database schema can be found below:

![SCHEMA](https://github.com/cafalchio/coinluxe/blob/main/media/readme/all_models.png)

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
- Add to Bag
- Remove from Bag

## Custom error pages:

Custom error pages were created for the following errors:

- 404 - (page not found): Page not found error occurs when the user tries to access a page that does not exist.

  This functionality ensures that the user is redirected to a custom error page when an error occurs.

# Features

The current features of the website are:

## Navbar

- The website has a navigation bar that allows users to navigate to different sections of the website.
- The navbar includes links to the home page, cryptocurrencies list, login, signup. If the user is logged, than also includes to: Shopping Bag and Wallet
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/navbar.png" width="600" alt="navbar">
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/navbar_logged.png" width="600" alt="navbar logged">

## Footer

- The website has a footer section that appears on every page.
- The footer may contain links to facebook page and github.

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/footer.png" width="600" alt="navbar logged">

## Home Page

- The home page serves as the main landing page of the website.
- It may provide an overview of the website's purpose, features, and highlights.

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/home_light.png" width="600" alt="homepage light">


## User Account Pages

- The website includes user account functionality.
- Users can create an account, log in, and access their personalized account pages.

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/signup.png" width="400" alt="signup">
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/signin.png" width="400" alt="signin">
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/signout.png" width="400" alt="signout">

## Cryptocurrencies List

- The website provides a list of cryptocurrencies.
- Users can browse through the available cryptocurrencies and access detailed information about each one.
- The list may include features such as sorting, filtering, and pagination for easy navigation.

## Pagination

- The pagination feature allows the user to navigate through the crypto list. The most important page, as the users can select the cryptos to explore and buy.

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/crypto_list.png" width="800" alt="Cryptos list">



## Crypto detail

Another important page, here the user can see details of the crypto and the price x time graph.


<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/kas_details.png" width="800" alt="Graph details">



## Error Page

The custom error page

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/404.png" width="800" alt="Error page">



# Marketing Strategy

Our marketing strategy revolves around two core pillars: our newsletter and our Facebook page. We believe that by optimizing these channels, we can effectively reach and engage our target audience. Here's how we plan to make it better:

* Engagement: To keep our subscribers engaged, we will introduce interactive elements such as polls, surveys, and quizzes, inviting them to participate actively.

* Personalization: Our newsletters will be tailored to individual preferences and user behavior, ensuring that the content resonates with each recipient.

* Frequency: We will maintain a consistent and well-balanced sending frequency to ensure our newsletters are informative without overwhelming our subscribers.

## SEO

* Our metatags provide a good foundation for SEO:
    <meta name="description" content="CoinLuxe a unique place to buy and sell crypto." />
    <meta name="keywords" content="cryptocurrency, exchange, crypto" />
    <meta name="author" content="Matheus Cafalchio" />
    <title>CoinLuxe</title>

* Robots.txt: Ensure that your robots.txt file is correctly configured to control which parts of your site are accessible to search engine crawlers.

* Sitemap.xml: Create and submit a sitemap.xml file to search engines like Google. This file lists all the pages on your site, making it easier for search engines to crawl and index your content.

* Mobile friendly design

* Page load speed


## Social Media Marketing

Our social media marketing is posted frequently on our facebook account.

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/facebook1.png" width="600" alt="Facebook account">

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/face2.png" width="600" alt="Facebook account 2">


## Email Marketing



# Testing

* Testing has taken place continuously throughout the development of the project. Each view was tested regularly. When the outcome was not as expected, debugging took place at that point.

## Python validation

Pycodestyle was tested in all folders. Currently just the management part of the api_backend does not comply with the style in line characters. But the work around to comply would make the code much longer and complicated.  "– sometimes style guide recommendations just aren’t applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. " (pep8)

## LightHouse

Desktop
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/desktop.png" width="600" alt="Lighthouse Desktop">

Mobile
<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/mobile.png" width="600" alt="Lighthouse Mobile">


## HTML validation

<img src="https://github.com/cafalchio/coinluxe/raw/main/media/readme/html_check.png" width="600" alt="Html check">

## CSS validation

The CSS validation was not made as Tailwind CSS was using in this project.

## Manual testing

* Visit Homepage for Platform Overview:
    The homepage provides an engaging and informative overview of the platform, highlighting its key features and benefits without any issues.


* Browse Cryptos and View Individual Crypto Pages:
    Users can browse and access detailed pages for individual cryptos without disruptions.

* Explore List of Cryptocurrencies:
    The list of cryptos appears and the page navigation works for all pages.


* Edit Crypto:
    Editing cryptocurrency information in the user's portfolio works correctly. Changes are saved, and the user receives a confirmation message.

* Remove Crypto from bag:
    Removing a cryptocurrency from the user's bag functions as expected. The selected cryptocurrency is successfully deleted.

* Manage Cryptos:
    The management system for cryptocurrencies operates without issues. Admins manage their listings.

* Receive Confirmation Email:
    Confirmation emails are sent to users when the users register and pay for cryptos.

* Withdrawal (deliver) Crypto:
    The mock withdrawal process for cryptocurrencies works as expected. The once clicked the cryptos are removed from the site.

* Buy Cryptos:
    Purchasing cryptocurrencies through the platform is straightforward. Transactions are processed correctly, and users receive their purchased assets in their wallets.

* Add Crypto to the Shopping Bag:
    Adding cryptocurrencies to the shopping bag or cart functions correctly. The selected items are added, and users can proceed with their purchases.

* See Historical Prices:
    Viewing historical price charts and data for cryptocurrencies is error-free. Users can track price trends over time without issues.

* See Crypto Details:
    Accessing detailed information about specific cryptocurrencies works as intended. Users can explore market data, news, and performance metrics.

* See Cryptocurrencies:
    Browsing the list of available cryptocurrencies with brief descriptions is seamless. Users can gather information and make informed decisions.

* Receive Login Email:
    User receive email when sign in.

* Sign In:
    The user sign-in process is working as expected.

* Log Out:
    The log-out functionality works correctly. Users can sign out of their accounts, enhancing security and privacy.

* Login:
    The login system is user-friendly and secure, providing access to personalized features and data.

* View wallet:
    The wallet view displays user cryptocurrency holdings and amount.

* Log In to Account:
    Registered users can log in to their accounts without issues, gaining access to personalized features and data.


# Bugs

* During the development there were many bugs, currently there are few known bugs.

- Add Crypto. The Add Crypto form was impossible to fill manually, as it needs all the crypto details that cannot be created. Market related data is based on real data. To work around, a model was created to keep all the cryptos id of cryptos that will be automatically updated by the scheduler.
So once the id is in the list, the data will be added later.

- The site uses the free Coingecko api. However, sometimes due to the free tier, the api call fails and timeout.


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

 - TailWind: used to make the style and compile the css.

# Credits

https://picsvg.com/ 
https://www.youtube.com/watch?v=K1e8kpoag0E  
https://www.youtube.com/watch?v=miiPsBlqMns
https://tailwindcss.com/
https://www.khanna.law/blog/deploying-django-tailwind-to-heroku
https://looka.com
https://github.com/ecabanasv/ci-pp5-ecommerce

# Acknowledgments

 - Thanks to Daisy (mentor) for the help
 - To the hackathon and comunity neurodiversity for the motivation

# Disclaimer

This project is for educational purposes only. All the content of the website is fictional and it is not intended to be used for commercial purposes.

# License

This project is licensed under the Apache2 License  - see the LICENSE.md file for details.
