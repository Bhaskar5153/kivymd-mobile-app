from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton, MDTextButton, MDRoundFlatButton, MDFlatButton


Window.size = (300, 500)




class First_screen(MDScreen):
    pass

class Second_screen(MDScreen):
    def __init__(self, **kwargs):
        super(Second_screen, self).__init__()

        

        product_items = [
            'Vijaya TM 250ml',
            'Vijaya TM 500ml',
            'Vijaya TM 1000ml',
            'Vijaya SM ',
            'Vijaya WM',
            'Vijaya CM',
            'Amul Taza',
            'Amul Gold',
            'Jersey',
            'Vishaka',
            'Heritage'
        ]

        menu_items = [
            {
                'text': f"{product}",
                'viewclass': 'OneLineListItem',
                'on_release': lambda x=f"{product}": self.product_options(x),
            } for product in product_items
        ]


        self.menu = MDDropdownMenu(caller=self.ids.products, items=menu_items, width_mult=10)

    def product_options(self, product_name):
        self.ids.products.text = product_name


    def pick_date(self):

        calendar = MDDatePicker()
        calendar.bind(on_save=self.get_date, on_cancel=self.get_cancel)
        calendar.open()

    def get_date(self, instance, value, date_range):
        self.ids.date.text = str(value)

    def get_cancel(self, instance, value):
        pass

    def bill(self, user_bill, price, quantity):

        if self.ids.products.text == "Vijaya TM 250ml":

            price = self.ids.price_id.text

            price = int('10')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)

        elif self.ids.products.text == "Vijaya TM 500ml":

            price = self.ids.price_id.text

            price = int('20')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)

        elif self.ids.products.text == "Vijaya TM 1000ml":

            price = self.ids.price_id.text

            price = int('40')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)


        elif self.ids.products.text == "Amul Taza":

            price = self.ids.price_id.text

            price = int('40')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)


        elif self.ids.products.text == "Amul Gold":

            price = self.ids.price_id.text

            price = int('30')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)

        elif self.ids.products.text == "Jersey":

            price = self.ids.price_id.text

            price = int('45')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)


        elif self.ids.products.text == "Vishaka":

            price = self.ids.price_id.text

            price = int('25')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)

        
        elif self.ids.products.text == "Heritage":

            price = self.ids.price_id.text

            price = int('45')

            quantity = self.ids.Qty.text 

            quantity = int(quantity)

            user_bill = price * quantity

            self.ids.bill_id.text = str(user_bill)

            self.ids.price_id.text = str(price)
    

class Window_manager(ScreenManager):
    pass





class trackapp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        kv_lang = Builder.load_file('track.kv')

        return kv_lang

if __name__ == '__main__':
    trackapp().run()