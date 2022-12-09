# MeegsBay

Website that allows users to create listings. Others can then view those listings, bid on them, add the listings to a watchlist, and even leave comments on the listings.


## Workflow

The image below displays the general workflow of MeegsBay. The default page is the active listings page. On this page you can see all the active listings if there are any.

The header of the website changes whether the user is logged in or not.

When the user **is not** logged in, the user has the option to register, to log in or to view the active listings. On the active listings page, the user can also access the individual listings. However, some parts of the individual listing page are not visible when a user is not logged in. Parts such as the bidding option and the option to add the listing to the watchlist are not yet present.

When the user **is** logged in, the header changes. The user is now also able to create a new listing.

However, that is not all. On top of this, the user can also access parts of the website that were previously locked. Such as:
- Add listings to their watchlist and observe this watchlist
- Bid on active listings
- Comment on active listings

Lastly, the "Log in" button changed to "Log out" and the user is immediately logged out, and returned to the main page upon clicking this button.

When the logged in user is on an individual listings page of their own, then there is also a button which enables the user to close the auction. The user that has won the auction is able to view that they won the bidding when they enter the url of the closed bidding.

### Class Diagram

TODO

#### Databases per page

TODO
