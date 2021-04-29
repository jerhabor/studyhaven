<img src="static/images/studyhaven-mockup.PNG" alt="StudyHaven display on devices" width="100%" height="auto"/>

# StudyHaven
Welcome to StudyHaven! This is an app that will reassure your capability for academic success. Aimed at students of ages 7 - 18, StudyHaven provides top quality stationery to aid studying, details exam question written by former examiners and professional tutors who carry evidence of high performance in there academia. This is the place to get the very best out of your learning whilst knowing you can rely on attaining the necessary studying equipment and materials to become the best student you can be. 

## 1. User Experience
Ideas for the application were divided into three. Even though users have their own goals when visiting the site, it was worth aligning them with the business goals (i.e. those of the site and store owners).
### 1.1. User Stories
#### 1.1.1. Customer User Stories

User Story 1
> As a customer, I would like to be able to make payment no more than 2 clicks after viewing items in my shopping bag.

User Story 2
> As a customer, I would like to be able to view my order history in order to keep track of my payments.

User Story 3
> As a customer, I would like to be browse through shop and add them to bag.

#### 1.1.2. Site User Stories

User Story 4
> As a site user, I would like the site to be responsive enough that I should not have to scroll horizontally to see tables/content.

User Story 5
> As a site user, when registering I would like to see options that verify my inputs.

User Story 6
> As a site user, I would like to be able to easily save my address details after a purchase to which I could reuse automatically.

#### 1.1.2. Site Owner Stories

User Story 7
> As a site owner, I would like to be able to add products regardless of whether they have an image or not.

User Story 8
> As a site owner, I would like to be able to edit products freely.

User Story 9
> As a site owner, I would like to be able to delete any unwanted or expired products.

User Story 10
> As a site owner, I would like to be able prevent any site user or hacker from bypassing the site urls.

### 1.2. Strategy Phase
### 1.3. Scope Phase
### 1.4. Structure Phase
### 1.5. Skeleton Phase
### 1.6. Surface Phase

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
#### 2.1.8. Profile Page
#### 2.1.9. Product Admin Page
#### 2.1.10. Tutoring Page
#### 2.1.11. FAQs Page
### 2.2. Special Features
- Loading Overlay
- Go to Top Button
- Bag to Order Steps
### 2.4. Future Features
- Tick box to subscribe to discount codes when registering
- Pagination for the products in the StudyHaven Shop
- Ability to log in with Social Accounts

## 3. Information Architecture
### 3.1. Database
### 3.2. Data Models
#### 3.2.1. Order Model
#### 3.2.1. FAQ Model
#### 3.2.1. Review Model
#### 3.2.1. Categories Model
#### 3.2.1. Product Model
#### 3.2.1. Tutoring Model

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
### 6.2. Deployment to Heroku

## 7. Credit
### 7.1. Content
### 7.2. Acknowledgement
### 7.3. Disclaimer