from config import *
from selenium import webdriver
import time
DRIVER = webdriver.Chrome('./chromedriver')

class Jeeves:
    def __init__(self, orders):
        self.orders = orders
        if self.orders:
            print(f'Jeeves was handed {len(orders)} orders to be processed.')
            self.login_to_postnord()
            self.new_order(self.orders)
        else:
            print(f'Jeeves got {len(self.orders)} to process, jeeves is done.')

    @staticmethod
    def login_to_postnord():

        print('Jeeves is loading Postnord')
        DRIVER.get('https://portal.postnord.com/login/')

        time.sleep(10)

        print('Jeeves gratefully accept cookies')
        accept_all_cookies_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
        accept_cookies = DRIVER.find_element_by_xpath(accept_all_cookies_button_xpath)
        accept_cookies.click()

        time.sleep(5)

        print('Jeeves fills in the credentials and logs in to postnord')
        email_field_xpath = '//*[@id="email"]'
        password_field_xpath = '//*[@id="password"]'
        login_button_xpath = '/html/body/app-root/app-start/div[1]/form/pn-button-container/button'
        email_element = DRIVER.find_element_by_xpath(email_field_xpath)
        password_element = DRIVER.find_element_by_xpath(password_field_xpath)
        login_button_element = DRIVER.find_element_by_xpath(login_button_xpath)
        email_element.send_keys(POSTNORD_EMAIL)
        password_element.send_keys(POSTNORD_PASSWORD)
        login_button_element.click()

        time.sleep(3)

        print('Jeeves goes to shippingtoolpro')
        # Go to Skicka Direkt Business
        DRIVER.get("https://portal.postnord.com/shippingtoolpro/")

        time.sleep(5)

        print('Jeeve dont need no silly introduction')
        close_intro_xpatch = '/html/body/div[1]/div/onboarding/div/main/material-icon'
        close_intro_element = DRIVER.find_element_by_xpath(close_intro_xpatch)
        close_intro_element.click()

    def new_order(self, orders):

        number_of_orders = len(orders)
        current_order = 1
        for order in orders:

            DRIVER.get("https://portal.postnord.com/shippingtoolpro/new-shipment/recipient/add")

            # @Page Mottagare
            print(f'Jeeves is processing {current_order} of {number_of_orders} orders.')
            print(f'Current order: {order.id} | {order.customer["first_name"]} {order.customer["last_name"]} | Worth {order.total}kr | Shipping option MyPack Home {order.weight}g')
            current_order += 1

            time.sleep(5)
            full_name = order.shipping['first_name'] + ' ' + order.shipping['last_name']
            full_name_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[3]/div/field-label[1]/label/ng-transclude/input'
            full_name_element = DRIVER.find_element_by_xpath(full_name_xpath)
            full_name_element.send_keys(full_name)

            address_1 = order.shipping['address_1']
            address_1_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[1]/field-label/label/ng-transclude/input'
            address_1_element = DRIVER.find_element_by_xpath(address_1_xpath)
            address_1_element.send_keys(address_1)

            address_2 = order.shipping['address_2']
            address_2_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[2]/field-label/label/ng-transclude/input'
            address_2_element = DRIVER.find_element_by_xpath(address_2_xpath)
            address_2_element.send_keys(address_2)

            postcode = order.shipping['postcode']
            postcode_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[1]/div/field-label[1]/label/ng-transclude/input'
            postcode_element = DRIVER.find_element_by_xpath(postcode_xpath)
            postcode_element.send_keys(postcode)

            city = order.shipping['city']
            city_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[1]/div/field-label[2]/label/ng-transclude/input-area-autocomplete/input'
            city_element = DRIVER.find_element_by_xpath(city_xpath)
            city_element.send_keys(city)

            email = order.customer['email']
            email_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/fieldset[4]/div[3]/field-label[1]/label/ng-transclude/input'
            email_element = DRIVER.find_element_by_xpath(email_xpath)
            email_element.send_keys(email)

            phone = order.customer['phone']
            phone_xpath = '//*[@id="recipient-tel"]'
            phone_element = DRIVER.find_element_by_xpath(phone_xpath)
            phone_element.send_keys(phone)

            time.sleep(3)

            accept_button_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-sender-recipient-recipient/form/button'
            accept_button_element = DRIVER.find_element_by_xpath(accept_button_xpath)
            accept_button_element.click()

            time.sleep(5)

            light_freigt_button_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type/fieldset/div/label[1]/input'
            light_freigt_button_element = DRIVER.find_element_by_xpath(light_freigt_button_xpath)
            light_freigt_button_element.click()

            time.sleep(3)

            if order.weight == 250:
                #set valuenow to 3 = 250g
                weight_slider_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type-pane/new-shipment-details-weight/fieldset/label/div[1]/ol/li[4]'
                weight_slider_element = DRIVER.find_element_by_xpath(weight_slider_xpath)
                weight_slider_element.click()
            elif order.weight == 500:
                #set valuenow to 4 = 500g
                weight_slider_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type-pane/new-shipment-details-weight/fieldset/label/div[1]/ol/li[4]'
                weight_slider_element = DRIVER.find_element_by_xpath(weight_slider_xpath)
                weight_slider_element.click()
            elif order.weight == 1000:
                #set valuenow to 5 = 1000g
                weight_slider_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type-pane/new-shipment-details-weight/fieldset/label/div[1]/ol/li[6]'
                weight_slider_element = DRIVER.find_element_by_xpath(weight_slider_xpath)
                weight_slider_element.click()
            else:
                #set valuenow to 6 = 2000g
                weight_slider_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type-pane/new-shipment-details-weight/fieldset/label/div[1]/ol/li[7]'
                weight_slider_element = DRIVER.find_element_by_xpath(weight_slider_xpath)
                weight_slider_element.click()

            time.sleep(3)

            klimatkompensation_tickbox_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-product-type-pane/new-shipment-details-addons/fieldset[2]/div/div[2]/new-shipment-details-addon/div/div/label/input'
            klimatkompensation_tickbox_element = DRIVER.find_element_by_xpath(klimatkompensation_tickbox_xpath)
            klimatkompensation_tickbox_element.click()

            time.sleep(3)

            booking_id = order.id
            booking_ref_input_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-description/fieldset/div[1]/field-label[1]/label/ng-transclude/input'
            booking_ref_input_element = DRIVER.find_element_by_xpath(booking_ref_input_xpath)
            booking_ref_input_element.send_keys(booking_id)
            description_ref_input_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/div/new-shipment-details-description/fieldset/div[1]/field-label[2]/label/ng-transclude/input'
            description_ref_input_element = DRIVER.find_element_by_xpath(description_ref_input_xpath)
            description_ref_input_element.send_keys(booking_id)

            save_order_button_xpath = '/html/body/div[1]/div/ui-view/main-columns/main/new-shipment-details/form/button'
            save_order_button_element = DRIVER.find_element_by_xpath(save_order_button_xpath)
            save_order_button_element.click()

            time.sleep(5)
