# Testing

## 1. Manual Testing of Features
### 1.1. Create (CRUD Functionalities)
The Create feature of the site lies in the "Add a Product" feature. Only the site owner can perform this.

__How to add a product:__

1. Sign in as a superuser
2. Click or hover over "My Account" to initiate dropdown and select "Product Admin".
3. Populate the input fields; the choose image and image_url fields are not compulsory.
4. Click Add Product and be redirected to the newly added product's info page in the shop.

Please see section 3.3. User Story 7 for images as proof of these steps.

### 1.2. Read (CRUD Functionalities)

All aspects of the website carry readable functionalities from accessing the shop and viewing the products and their product information to viewing one's order summary and history. This proves that the models, forms have all been rendered well through the view to the templates.

Please see section 3. Achieve of User Stories for images as proof of these functionalities.

### 1.3. Update (CRUD Functionalities)

Only a site owner holds the ability to update a product; they are called the Superuser.

__How to update a product__

1. Sign in as a superuser
2. Go to shop
3. Site Owner should expect to see all product cards with Edit and Delete buttibs.
4. Select Edit and update the product information
5. Click Edit Profile.

Please see section 3.3. User Story 8 for images as proof of these steps.

### 1.4. Delete (CRUD Functionalities)

Similarly, only a site owner can delete a product. There were no templates required as this is a just a button functionality. However there is a 2-step process. Clicking the red button will leave superusers with a modal box asking for their confirmation to delete. This is added security to the functionality.

__How to delete a product__
1. Sign in as a superuser
2. Go to shop or product info page
3. Click the red "Delete" button
4. Press the read delete button again if very sure.
5. Product delete as confirmed by message in the top right.

Please section 3.3. User Story 9 for images as proof of these steps.

## 2. Automated Testing
## 3. Achievement of User Stories
### 3.1. Customer User Stories
__User Story 1__
> As a customer, I would like to be able to make payment no more than 2 clicks after viewing items in my shopping bag.

Upon arriving at the shopping bag page, the customer will see the following:

<img src="static/images/bag-step-1.PNG" alt="Bag Step 1" width="50%" height="auto"/>

Customer must then scroll through, checking their items if necessary and clicking the button at the bottom:

<img src="static/images/secure-checkout.PNG" alt="Secure Checkout" width="50%" height="auto"/>

The next page then shows the customer that they have completed the first step and that this is the last step:

<img src="static/images/checkout-step-2.PNG" alt="Checkout Step 2" width="50%" height="auto"/>

If customer scrolls to the bottom, they will see a field for card details input to pay. This procedure only took 1 click from the shopping bag which is better than what they had requested.

<img src="static/images/payment.PNG" alt="Payment Input" width="50%" height="auto"/>

__User Story 2__
> As a customer, I would like to be able to view my order history in order to keep track of my payments.

The order history is found in "My Profile" and this table will always be present to show where orders will be populated. The table automatically populates data with the customer's order. The field include order number, order date and order items and the price paid at the time of purchase.

<img src="static/images/order-history.PNG" alt="Order History Table" width="50%" height="auto"/>

Confirmation emails are also sent to the customer in the event that they are not a registered site user. This also ensure that customers can keep track of their payments in their own personal inbox.

<img src="static/images/order-success-message.png" alt="Order Success Message" width="50%" height="auto"/>

__User Story 3__
> As a customer, I would like to be browse through shop and add them to bag.

Go to Shop on the Main Navigation and the customer is greeted with all of the StudyHaven products. The customer also has the option to filter them as they please until they reach a favourite. 

<img src="static/images/shop-page.PNG" alt="StudyHaven Shop Page" width="50%" height="auto"/>

The search bar also goes straight to the shop. Once a product is found, adding to bag is as easy as clicking the product for full information and then the "Add to Bag" button.

<img src="static/images/search-test.PNG" alt="Search Test" width="50%" height="auto"/>

A message in the top right corner will then be displayed with a preview of the shopping bag contents.

<img src="static/images/add-to-bag.PNG" alt="Added to Bag Message" width="50%" height="auto"/>


### 3.2. Site User Stories
__User Story 4__
> As a site user, I would like the site to be responsive enough that I should not have to scroll horizontally to see tables/content.

All aspects of the site were relatively straightforward to make responsive apart from the shopping bag table. As a developer, the approach was to divide this table elements into smaller components which will be piled together using Bootstrap's grid.

<img src="static/images/bag-mobile.PNG" alt="Shopping Bag mobile view" width="20%" height="auto"/>

<img src="static/images/bag-desktop.PNG" alt="Shopping Bag desktop view" width="50%" height="auto"/>

__User Story 5__
> As a site user, when registering I would like to see options that verify my inputs incase I enter the wrong email or password.

Django-allauth comes with authetication which are easily imported to the whole application. Fortunately, the authetication does require a confirmation for the email address and passwords. The system is also strict on the type of password that should be used.

<img src="static/images/sign-up-form-test.PNG" alt="Sign Up Form Test" width="50%" height="auto"/>

__User Story 6__
> As a site user, I would like to be able to easily save my address details after a purchase to which I could reuse automatically.

StudyHaven was designed to make things easier and by checking the box underneath the Postcode input on checkout, the details will be stored. However, please note that this is only viewable to registered users. 

<img src="static/images/save-info.PNG" alt="Save Shipping Info Checkbox" width="50%" height="auto"/>

Those that have not registered will have an option to register or login instead:

<img src="static/images/save-info2.PNG" alt="Save Shipping Info Checkbox" width="50%" height="auto"/>

Once payment has gone through, the user can find their contact and shipping details immediately populated on their profile page. 

### 3.3. Site Owner Stories
__User Story 7__
> As a site owner, I would like to be able to add products regardless of whether they have an image or not.

This is possible as in the `Product` model, the `image` and `image_url` fields are not required so therefore they will not be required on the rendered form.

<img src="static/images/add-product-field.PNG" alt="Image field vs Price Field" width="50%" height="auto"/>

Instead an `if` statement handles the "No Image" display in the event that the site owner does not upload an image:

_(From products.html lines 73-81)_
```
{% if product.image %}
<a href="{% url 'product_info' product.id %}">
    <img class="card-img-top img-fluid" src="{{ product.image.url }}" alt="{{ product.name }}">
</a>
{% else %}
<a href="{% url 'product_info' product.id %}">
    <img class="card-img-top img-fluid" src="{{ MEDIA_URL }}no-image.jpg" alt="{{ product.name }}">
</a>
{% endif %}
```
Non-required Image Fields vs the required Price fields:

<img src="static/images/add-product-field.PNG" alt="Image field vs Price Field" width="50%" height="auto"/>

Test product now added to the StudyHaven shop:

<img src="static/images/test-add-without-image.PNG" alt="Test product added to shop" width="50%" height="auto"/>

Test product info page:

<img src="static/images/test-product-info.PNG" alt="Test product info" width="50%" height="auto"/>

__User Story 8__
> As a site owner, I would like to be able to edit and update products freely.

When the site owner clicks on the blue Edit button on either the product info page or in the shop, they should expect to see the following:

<img src="static/images/editing-test-product.PNG" alt="Editing Test Product" width="50%" height="auto"/>

The image above shows an alert message in the top right to keep the site owner informed of the decision that they have made to edit a particular product in the shop.

The site owner can also now change the product image to another of their choice:

<img src="static/images/change-test-image.PNG" alt="Editing Test Product Image" width="50%" height="auto"/>

Updated product after pressing "Edit Product" being redirected to product info page:

<img src="static/images/updated-test-product.PNG" alt="Updated Test Product Image" width="50%" height="auto"/>

__User Story 9__
> As a site owner, I would like to be able to delete any unwanted or expired products.

Using the test product as an example, the site owner can simply click the red delete button link to be greeted with a confirm delete modal. This add security in the event that the site owner mistakenly pressed the delete button link.

<img src="static/images/confirm-delete.PNG" alt="Updated Test Product Image" width="50%" height="auto"/>

Once the site owner presses delete, a confirmation message is displayed in the top right as the page redirects to the shop.

<img src="static/images/confirmed-deleted.PNG" alt="Updated Test Product Image" width="50%" height="auto"/>

__User Story 10__
> As a site owner, I would like to be able prevent any site user or hacker from bypassing the site urls.

A custom 404 page has been created for whenever someone types a url that is not part of the site infrastructure:

<img src="static/images/404page.PNG" alt="Updated Test Product Image" width="50%" height="auto"/>

If a regular registered site user / non-site owner attempts to add a product an error message is displayed:

<img src="static/images/only-site-owners.PNG" alt="Updated Test Product Image" width="50%" height="auto"/>

If an unregistered user attempts to bypass, they will be directed to the login page.

## 4. Code Validation
## 5. Test on Different Browsers
## 6. Test on Different Devices
## 7. Bugs and Problems
### 7.1 Solved bugs and problems
### 7.2 Unsolved bugs and problems