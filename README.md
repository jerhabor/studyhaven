<img src="static/images/studyhaven-mockup.PNG" alt="StudyHaven display on devices" width="100%" height="auto"/>

# StudyHaven
Welcome to StudyHaven! This is an app that will reassure your capability for academic success. Aimed at students of ages 7 - 18 years, StudyHaven provides top quality stationery to aid studying, details exam question written by former examiners and professional tutors who carry evidence of high performance in there academia. This is the place to get the very best out of your learning whilst knowing you can rely on attaining the necessary studying equipment and materials to become the best student you can be. 

StudyHaven is deployed to Heroku and can be accessed [here](https://studyhaven.herokuapp.com/).

## 1. User Experience
Ideas for the application were divided into three. Even though users have their own goals when visiting the site, it was worth aligning them with the business goals (i.e. those of the site and store owners).
### 1.1. Strategy Phase

With the pandemic shutting down schools and cancelling exams yet students were still being graded in a totally unexpected manner, their panic was inevitable. The aim of StudyHaven is to offer a safe space to provide assistance to students' learning. I decided to ask students what type of things would they like to see in an e-commerce website focused in education. As the store owner, I was aligned with their viewpoint of having a range of affordable custom-made study resources and stationery to alleviate any stress they may have. Then I met with former examiners and high-performers across a period of 2 months to develop a bespoke StudyHaven syllabus for the most popular subjects that students are struggling with right now. These subjects are:

11 Plus (Ages 7 - 11):
- Mathematics
- English
- Verbal Reasoning
- Non-Verbal Reasoning

KS2 (Ages 7 - 11):
- Mathematics
- English

GCSE (Ages 11 - 16):
- Biology
- Business Studies
- Chemistry
- Computer Science
- Economics
- French
- Mathematics
- Physics
- Spanish

A-Level (Ages 16 - 18):
- Biology
- Business Studies
- Chemistry
- Computer Science
- Economics
- French
- Mathematics
- Physics
- Spanish

Please note that StudyHaven is looking into writing books for more subjects in the future but will always be primarily based on user demand.

### 1.2. Scope Phase

Following on from the stategy phase, it was imperative to develop user stories for which the development of StudyHaven will largely depend on. You can find the full list of user stories in Section 1.6.

__Functional Requirements:__

StudyHaven must...
- Sell products and they should be able to be categorised them. There should be a relationship between the product and the category in order to run a consistent theme across all products within a set category. 
- Handle orders without users being taken to an external site to make purchase otherwise this goes against its purpose of serving as an e-commerce website.
- Offer extra services beyond selling books and stationery to differentiate it from any regular academic e-commerce store.

__Content Requirements:__

StudyHaven must...
- Make students be welcomed or drawn into the website by the choice of colours and fonts.
- Have a responsive website that displays information on any device. This makes it way more accessible, appealing and interactive for the younger generation.
- Display High quality product images to aid in selling the products that they apply to.

### 1.3. Structure Phase
__Interaction Design__
- Following on from the functional requirements above, the user must be able to make the order themselves and at their own speed. This allows them more control in the whole process.
- Any information or message that is displayed after various activities should be displayed in order to help the user keep themselves on track during their site visit.
- Any message should be closed at the request of the user to ensure that they have read the information and take control of their next thoughts and actions based off of it.
- Good interaction design will ensure that products are not easily deleted from the site but there must be a verification process to which the user must press confirm. This could be in the form of a modal.

__Information Architecture__
- Ensure that the product images being displayed are close to their descriptions so that the subconscious can make a logical relationship between the two pieces of product information.
- Utilise Bootstrap grid system particularly on small devices to structure content in a way that encourages padding and limits information overload.
- There should be the ability to scroll back to top in the user is scroll through a long page of products or text.
- The user should be able to make a quick search for products whenever they feel like without have to click links to get there. So it will be helpful if the search bar is accessible in the footer and/or the header (depending on the device).
- When it comes to payment, the most important question is _"How much am I going to pay?"_. So the answer to this question must stand out on the page so that it is clear to the user.

### 1.4. Skeleton Phase
In order to encompass Interface Design, Navigation Design and Information Design, I created wireframes for the website. The [StudyHaven wireframes](https://github.com/jerhabor/studyhaven/blob/ecbfc696bc26739225b683638529b6a301392985/static/wireframes/studyhaven-wireframes.pdf) listed the following pages:

1. Home
2. My Profile
3. Product Admin
4. FAQs
5. Tutoring
6. Register
7. Login
8. Products
9. Product Info
10. Checkout - Shopping Bag
11. Checkout - Contact Information
12. Checkout - Payment
13. Checkout - Order Summary

Please note that the names of the wireframed pages may change for the real application during the course of the development. This could be due to fact that the name should be a solid representation of the information being delivered to the user. Clarity at first sight is attractive.

### 1.5. Surface Phase

The wireframes could only provide assistance with the relationship and structure of information and so it is difficult to also portray extra key information such as the mood of the site, the choice of colours, the fonts and the overall appeal.

#### 1.5.1. Colour theme
The word _"haven"_ means _"a safe place"_. A safe place or refuge is a place that puts someone at ease and makes them feel welcome. So I wanted warm colours that would instantly express this.

According to [Art Therapy](http://www.arttherapyblog.com/online/color-psychology-psychologica-effects-of-colors/#warmcolors), the colours associated with warmth are Red, Orange, Yellow, Brown and Pink. I decided to play around with colour palettes and aligned the intended feel of the colours with the site goals mentioned in the previous phases of UX design.

<img src="static/images/color-gradient1.PNG" alt="Colour Palette 1" width="50%" height="auto"/>

<img src="static/images/color-gradient2.PNG" alt="Colour Palette 2" width="50%" height="auto"/>

<img src="static/images/color-gradient3.PNG" alt="Colour Palette 3" width="50%" height="auto"/>

Common colours from the palettes that I thought would present a welcoming aura as users visit StudyHaven are: [`#fdd9cc`](https://www.colorhexa.com/fdd9cc), [`#d2544a`](https://www.colorhexa.com/d2544a) and [`#A52A2A`](https://www.colorhexa.com/a52a2a).

#### 1.5.2. Font styling
A bold font is one that would capture the attention of users. Seeing as the audience are classed as the younger generation, there needs to be an element of creativity to the style; one that gives a captivating but also not too distracting so that the user focus is aligned with the designed intention described in earlier sections above.

I came across a custom font called `Lovelo` which is youthful and great for branding:

<img src="static/images/lovelo-black.png" alt="Lovelo Black Font" width="50%" height="auto"/>

### 1.6. User Stories
#### 1.6.1. Customer User Stories

User Story 1:
> As a customer, I would like to be able to make payment no more than 2 clicks after viewing items in my shopping bag.

User Story 2:
> As a customer, I would like to be able to view my order history in order to keep track of my payments.

User Story 3:
> As a customer, I would like to be browse through shop and add them to bag.

#### 1.6.2. Site User Stories

User Story 4:
> As a site user, I would like the site to be responsive enough that I should not have to scroll horizontally to see tables/content.

User Story 5:
> As a site user, when registering I would like to see options that verify my inputs.

User Story 6:
> As a site user, I would like to be able to easily save my address details after a purchase to which I could reuse automatically.

#### 1.6.3. Site Owner Stories

User Story 7:
> As a site owner, I would like to be able to add products regardless of whether they have an image or not.

User Story 8:
> As a site owner, I would like to be able to edit products freely.

User Story 9:
> As a site owner, I would like to be able to delete any unwanted or expired products.

User Story 10:
> As a site owner, I would like to be able prevent any site user or hacker from bypassing the site urls.

## 2. Features
### 2.1. General Features

#### 2.1.1. Base Elements
- Navigation Bar
- Search Bar
- Footer
#### 2.1.2. Home Page
- Carousel Header
- Sales Section
- Testimonials
#### 2.1.3. Shop Page
- Filter Tags
- Select Box
- Products
#### 2.1.4. Product Info Page
- Product image
- Product Information
- Quantity Selector
- Buttons
#### 2.1.5. Shopping bag Page
- Tabular display
- Grid display
- Bag Summary
#### 2.1.6. Checkout Page
- Checkout form
- Bag Summary
#### 2.1.7. Checkout Success Page
Order Summary
#### 2.1.8. Profile Page
- Contact & Shipping Information
- Order History
#### 2.1.9. Product Admin Page
Add a Product
#### 2.1.10. Tutoring Page
- Description of Services
- Calendly Widget
- Table of Rates
#### 2.1.11. FAQs Page
Accordion
### 2.2. Special Features
- Loading Overlay
- Go to Top Button
- Bag to Order Steps
### 2.3. Future Features
- Tick box to subscribe to discount codes when registering
- Pagination for the products in the StudyHaven Shop
- Ability to log in with Social Accounts
- Best Selling Products

## 3. Information Architecture
### 3.1. Database
### 3.2. Data Models
#### 3.2.1. User Model
#### 3.2.2. Order Model
#### 3.2.3. FAQ Model
#### 3.2.4. Review Model
#### 3.2.5. Categories Model
#### 3.2.6. Product Model
#### 3.2.7. Tutoring Model

## 4. Technologies Used
### 4.1. Languages
- [HTML](https://www.w3schools.com/html/) - Stands for Hypertext Markup Language and it is the backbone of StudyHaven. The latest version (HTML5) - was used to add and structure the site content.
- [CSS](https://www.w3schools.com/css/) - Stands for Cascading Style Sheets. The latest version (CSS3) was used to style all HTML content on the website for enhanced structure and visual appeal.
- [JavaScript](https://www.javascript.com/) - Used to add interactivity to StudyHaven and some backend handling.
- [Python](https://www.python.org/) - Used to handle the backend views, models, forms and admin which will be used to render to the HTML templates.
### 4.2. Tools

- [Balsamiq](https://balsamiq.com/) - Used to create wireframes for the collection of applications.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Used to aid in creating and managing AWS S3 Bucket.
- [BrowserStack](https://www.browserstack.com/) - For generating cross browser shots of the site.
- [Canva](https://www.canva.com/) - To produce the carousel images plus the general logo and custom font choice for the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - To add automated authentication to StudyHaven.
- [Django Countries](https://pypi.org/project/django-countries/) - For the world countries dropdown selection box to send valid two-letter country codes to stripe webhook; needed to process orders.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - To add structure and style to the Django forms.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) - Use with Boto3 in AWS S3 Management.
- [Git](https://git-scm.com/) - Version Control System.
- [GitHub](https://github.com/) - A platform to store versions of code, track progress and share with a wider community.
- [GitPod](https://www.gitpod.io/) - The main workspace environment used for the development of StudyHaven.
- [Gunicorn](https://gunicorn.org/) - Needed in order to deploy project to Heroku.
- [Heroku](https://www.heroku.com) - Application hosting platform used in deployment.
- [ImgBB](https://imgbb.com/) - Used to generate urls to the product images to view in full screen in the StudyHaven shop.
- [Pillow](https://pypi.org/project/Pillow/) - Needed to process image files stored in the database.
- [PIP](https://pip.pypa.io/en/stable/) - Used to install the tools listed.
- [Psycopg2](https://pypi.org/project/psycopg2/) - Python adapter used to connect to PostgreSQL.
- [Pylint](https://pypi.org/project/pylint/) - Used to check any code that violates PEP8.
- [Stripe](https://stripe.com) - Used to securely make orders on site by validating card payments.
- [TechSini](https://techsini.com/) - To generate the devices mockup at the top of the README.

### 4.3. Framework & Libraries
- [Bootstrap](https://getbootstrap.com/) - Provides further styling and interactivity to the web page including the structure of HTML elements.
- [Django](https://www.djangoproject.com/) - Python Framework used to develop full stack applications and quickly render more high-quality dynamic template pages easily.
- [Font Awesome](https://fontawesome.com/) - Used to load special icons to bring a bit more animation to the HTML content.
- [Google Fonts](https://fonts.google.com/) - Used to access all other fonts used in the entire application.
- [JQuery](https://jquery.com/) - JavaScript Framework used in DOM manipulation and easy selection of IDs and classes and add more site interactivity.

### 4.4. Databases
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) - Used locally for the development database by Django.
- [PostgreSQL](https://www.postgresql.org/) - Used for the deployed database by Heroku.

### 4.5. Other
- The custom `Lovelo` font was inspired by a font on canva but designed and downloaded for custom use in the branding of StudyHaven.

## 5. Testing
The full documentation on testing can be found in [testing.md](https://github.com/jerhabor/studyhaven/blob/2fbacae2a8d75e9e06540c36b6524ca84e1b1a14/testing.md).

## 6. Deployment

### 6.1. Running Project Locally
1. Make a clone of this project by going to [https://github.com/jerhabor/studyhaven](https://github.com/jerhabor/studyhaven).

2. Select `Clone` dropdown menu and click GitHub CLI. Then copy and paste the command. Insert this command into your workspace terminal.

3. Ensure that a virtual environment is present. This is needed for the Python Interpreter. For further information on this please click [here](https://docs.python.org/3/library/venv.html).

4. Ensure that you have `pip` installed. Then type the following command to ensure all of the app dependencies are installed:
`pip install -r requirements.txt`.

5. In your environment variables, add the following settings:
_(Please note that as you are running locally the URL will be different so another webhook endpoint must be generated for this URL. With this you will receive a different `STRIPE_WH_SECRET` value to that of the deployed version on Heroku)_

|        Key        |                          Value                          |
|:-----------------:|:-------------------------------------------------------:|
|    DEVELOPMENT    |     < Can be set to True only when running locally >    |
|     SECRET_KEY    | < A different key to Heroku from Django Key Generator > |
| STRIPE_PUBLIC_KEY |             < Your Stripe Publishable Key >             |
|  STRIPE_WH_SECRET |             < Your Stripe WH Endpoint Key >             |
| STRIPE_SECRET_KEY |                < Your Stripe Secret Key >               |

6. To migrate, type in the following command into your terminal: `python3 -m migrate`.

7. Create a new superuser in order to access the admin on this development version of the app using the following command:
`python manage.py createsuperuser`

8. Can now finally run the project using: `python manage.py runserver`.

9. To access the admin, simply type `/admin` after the url in the address bar and then log in with the superuser details you created earlier.

### 6.2. Deployment to Heroku

1. Ensure that you have set up a new app on Heroku. If not, create a new app and select the region applicable or closest to you.

2. Click on the `Resources` tab and in the add-on search bar, type Postgres and add the free version. This will generate a database URL.

3. In your workspace, freeze all requirements using the following command: ``` pip3 freeze > requirements.txt ```

4. Create a Procfile using the following command: ``` echo web: python app.py > Procfile ```

5. Go back to Heroku, click deploy and select 'Connect to GitHub'. Continue the necessary steps to connect to your GitHub repository. Allow automatic deploy from GitHub. 

6. Now click on the `Settings` tab in Heroku and scroll down and click `Reveal Config Vars`. Ensure that the follow config vars are listed:

|          Key          |                           Value                         |
|:---------------------:|:-------------------------------------------------------:|
|   AWS_ACCESS_KEY_ID   |                < Your AWS Access Key ID >               |
| AWS_SECRET_ACCESS_KEY |                 < Your AWS Secret Key >                 |
|      DATABASE_URL     |              < Your Postgres database URL >             |
|    EMAIL_HOST_PASS    | < Your app password found after two-step verification > |
|    EMAIL_HOST_USER    |                 < Your business email >                 |
|       SECRET_KEY      |              < From Django Key Generator >              |
|   STRIPE_PUBLIC_KEY   |             < Your Stripe Publishable Key >             |
|   STRIPE_SECRET_KEY   |                < Your Stripe Secret Key >               |
|    STRIPE_WH_SECRET   |          < Your Stripe WH endpoint Secret Key >         |
|        USE_AWS        |                < Set to True to use AWS >               |

7. Login into the Heroku Postgres Shell, migrate the models and create a superuser to access the admin in the new Heroku app. For further information please click [here](https://devcenter.heroku.com/articles/heroku-postgresql).

8. Now that the links are in place, `git commit` your changes and push them. They will be uploaded to Heroku. To verify, click the `Deploy` tab in Heroku and view build progress.

9. To access the site, copy and paste the deployed link at the end of the build progress in Heroku, into your browser address bar.

10. To access the admin, simply type `/admin` after the deployed url in the address bar and then log in with the superuser details you created earlier.

## 7. Credit
### 7.1. Content
### 7.2. Acknowledgement
### 7.3. Disclaimer