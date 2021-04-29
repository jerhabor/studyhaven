# Testing

## 1. Manual Testing of Features
### 1.1. Create (CRUD Functionalities)
### 1.2. Read (CRUD Functionalities)
### 1.3. Update (CRUD Functionalities)
### 1.4. Delete (CRUD Functionalities)
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
> As a site user, when registering I would like to see options that verify my inputs.

__User Story 6__
> As a site user, I would like to be able to easily save my address details after a purchase to which I could reuse automatically.

### 3.3. Site Owner Stories
__User Story 7__
> As a site owner, I would like to be able to add products regardless of whether they have an image or not.

__User Story 8__
> As a site owner, I would like to be able to edit products freely.

__User Story 9__
> As a site owner, I would like to be able to delete any unwanted or expired products.

## 4. Code Validation
## 5. Test on Different Browsers
## 6. Test on Different Devices
## 7. Bugs and Problems
### 7.1 Solved bugs and problems
### 7.2 Unsolved bugs and problems