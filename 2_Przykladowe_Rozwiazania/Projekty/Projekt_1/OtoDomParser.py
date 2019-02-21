# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Parser import Parser
import BeautifulSoup



class OtoDomParser(Parser):

    def __init__(self, html_content):
        self.html_content = html_content
        self.soup_html = BeautifulSoup.BeautifulSoup(self.html_content)
        self.html_flats = self.find_flats()
        self.flats = {}
        self.flat_title = ''
        self.link = ''
        self.to_negotiate = ''
        self.price = ''
        self.city_district = ''
        self.renting_or_selling = ''


    def find_flats(self):
        find_flats = []
        for offer_item in self.soup_html.findAll('div', {'class': 'offer-item-details'}):
            if offer_item.find('span', {'class': 'offer-item-title'}):
                find_flats.append(offer_item)
        return find_flats


    def collect_flats_info(self):
        for i, flat in enumerate(self.html_flats):
            flat = Flat(flat)
            self.flat_title = flat.title_of_flat()
            self.link = flat.link()
            self.to_negotiate = flat.to_negotiate()
            self.price = flat.price()
            self.city_district = flat.city_disctrict()
            self.renting_or_selling = flat.renting_or_selling() #replace
            self.add_flat(i)

    def add_flat(self, id_flat):
        self.flats.update({id_flat: {'flat_title': self.flat_title, 'link': self.link, 'to_negotiate': self.to_negotiate,
                                 'price': self.price, 'city_district': self.city_district,
                                 'renting_or_selling': self.renting_or_selling}})

    def get_flats_info(self):
        return self.flats


class Flat(Parser):

    def __init__(self, flat):
        self.flat = flat

    def title_of_flat(self):
        flat_title = self.flat.find('span', {'class':'offer-item-title'}).getText()
        return flat_title.replace(',',' ').encode('utf=8')

    def link(self):
        flat_link = self.flat.find('a')
        return flat_link['href'].encode('utf=8')

    def to_negotiate(self):
        span_key = self.flat.find('span', {'class': 'normal inlblk pdingtop5 lheight16 color-2'})
        if span_key:
            to_negotiate = span_key.getText().encode('utf=8')
        else:
            to_negotiate = None
        return to_negotiate

    def price(self):
        flat_price = self.flat.find('li', {'class': 'offer-item-price'}).getText()
        return flat_price.encode('utf=8')

    def city_disctrict(self):
        city_district = self.flat.find('p', {'class': 'text-nowrap hidden-xs'}).getText()
        return city_district.replace(',',':').replace("Mieszkanie na sprzedaĹĽ: ","").encode('utf=8')

    def renting_or_selling(self): #wyrazenie regularne, jak zlapac wzorzec
        flat_renting_or_selling = self.flat.find('p', {'class': 'text-nowrap hidden-xs'}).getText()
        return flat_renting_or_selling.encode('utf=8')


