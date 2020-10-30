# aiwoo
### Automate order management for woocommerce.
Application fetches unprocessed orders from a woocommerce shop. It then logs on to https://portal.postnord.com/ and prepare all orders with the correct recipient and shipping weight etc. The user are left to preview and confirm the purchase of shipping for the aquired orders.  
 
#### Requirements: 
- Woocommerce : https://pypi.org/project/WooCommerce/
- Selenium : https://selenium-python.readthedocs.io/installation.html
- Google Chrome : https://www.google.se/chrome/
- Corresponding Chrome Driver : https://chromedriver.chromium.org/downloads

#### Configuration: 

Log on to the woocommerce admin panel and activate the API: https://docs.woocommerce.com/document/woocommerce-rest-api/ 
Create config.py and set credentials for Woocommerce and Postnord : 
- URL = ""
- CONSUMER_KEY = ""
- CONSUMER_SECRET = ""
- VERSION = ""

Set Postnord Credentials:
- POSTNORD_EMAIL = ""
- POSTNORD_PASSWORD = ""

#### Usage

Run main.py