from django.test import TestCase
from django.urls import reverse
from .models import Variety, Booking
import logging
from django.core.exceptions import ObjectDoesNotExist
from cd_reseller.settings import DATABASES
import os
from cd_reseller import credentials


# Logs
logger = logging.getLogger("Logs")
# Index page
# test that index page returns a 200
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        response = self.client.get(reverse('manage'))
        self.assertEqual(response.status_code, 302)

# Detail Page
class DetailPageTestCase(TestCase):

    def setUp(self):
        Variety.objects.create(title="TEST")
        self.variety = Variety.objects.get(title="TEST")

    # test that detail page returns a 200 if the item exists
    def test_detail_page_200(self):
        variety_id = self.variety.id
        response = self.client.get(reverse('store:detail', args=(variety_id, )))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_page_404(self):
        variety_id = self.variety.id + 1
        response = self.client.get(reverse('store:detail', args=(variety_id, )))
        self.assertEqual(response.status_code, 404)


# Booking Page
class BookingPageTestCase(TestCase):
    def setUp(self):
        variety = Variety.objects.create(title="NOSMOKE", stock=5, price=10)
        self.variety = variety
        self.quantity = 5
        self.address = "25 rue de la paix 75000 Paris France"
        self.email = 'martin@gmail.com'
        self.pgp = 'pgp example'
        self.address1 = "150 rue de La longue vue Bordeaux"
        self.email1 = "xxx@xxx.com"
        self.pgp1 = "pgp pgp exemple"
        logger.setLevel(logging.INFO)
    # test that a new booking is made

    def test_new_booking(self):
        old_bookings = Booking.objects.count()
        variety_id = self.variety.id
        self.client.post(reverse('store:booking', args=(variety_id, )), {
            'address': self.address,
            'pgp_public_address': self.pgp,
            'email': self.email,
            'quantity': self.quantity,
            'variety': self.variety
        })
        new_booking = Booking.objects.count()
        self.assertEqual(new_booking, old_bookings + 1 )

    # test that a booking belongs to an album
    def test_booking_belongs_variety(self):
        address = self.address
        pgp = self.pgp
        email = self.email
        variety_id = self.variety.id
        quantity = self.quantity
        self.client.post(reverse('store:booking', args=(variety_id, )), {
            'variety': self.variety,
            'email': email,
            'address': address,
            'pgp_public_address': pgp,
            'quantity': quantity,
        })
        booking = Booking.objects.first()
        self.assertEqual(booking.variety, self.variety)

    # test that an album is not available after a booking is made

    def test_album_available_after_booking(self):
        address = self.address
        pgp = self.pgp
        email = self.email
        variety_id = self.variety.id
        self.client.post(reverse('store:booking', args=(variety_id, )), {
            'address': address,
            'pgp_public_address': pgp,
            'email': email,
            'quantity': self.quantity,
            'variety': self.variety
        })
        self.variety.refresh_from_db()
        self.assertTrue(self.variety.available)

    def test_two_bookings_for_one_variety(self):
        variety_id = self.variety.id
        address = self.address
        pgp = self.pgp
        email = self.email
        self.client.post(reverse('store:booking', args=(variety_id, )),{
            'address': address,
            'pgp_public_address': pgp,
            'email': email,
            'quantity': self.quantity,
            'variety': self.variety
        })
        self.client.post(reverse('store:booking', args=(variety_id, )), {
            'address': self.address1,
            'pgp_public_address': self.pgp1,
            'email': self.email1,
            'quantity': self.quantity,
            'variety': self.variety
        })

        self.variety.refresh_from_db()
        self.assertTrue(self.variety.available)
        self.assertEqual(self.variety.stock, 3)

    def test_available_until_stock(self):
        address = self.address
        pgp = self.pgp
        email = self.email
        variety_id = self.variety.id
        for i in range(Variety.objects.get(pk=variety_id).stock):
            self.client.post(reverse('store:booking', args=(variety_id, )), {
                'address': address,
                'pgp_public_address': pgp,
                'email': email,
                'quantity': self.quantity,
                'variety': self.variety
            })
        self.variety.refresh_from_db()
        self.assertEqual(0, self.variety.stock)
        self.assertFalse(self.variety.available)

class ManagePageTestCase(TestCase):
    # Test logged in to pass into

    def setUp(self):
        self.fake = {
            'username': 'fake',
            'password': 'fake'
        }
        self.real = {
            'username': 'martingouv',
            'password': 'lizzy4231'
        }

    def test_CreateVariety_without_admins_rights(self):
        title = "Bonjour"
        request = self.client.post(reverse('manage'), {
            'title': title,
            'picture': 'url.com',
            'price': 25,
            'stock': 5
        })
        self.assertEqual(request.status_code, 302)
        try:
            variety = Variety.objects.get(title=title)
        except ObjectDoesNotExist:
            variety = None
        self.assertIsNone(variety)

    def test_login_WithoutAdminRights(self):
        response = self.client.post('/admin/login/', self.fake)
        self.assertFalse(response.context['user'].is_superuser)


class SettingsPage(TestCase):
    def setUp(self):
        self.db = DATABASES['default']

    def test_databases(self):
        if self.db['HOST'] == credentials.HOST_HOME:
            self.assertEqual(os.environ.get('home'), '1')
        elif self.db['HOST'] == credentials.HOST_NOT_HOME:
            self.assertEqual(os.environ.get('home'), '0')
        self.assertEqual(self.db['ENGINE'], 'django.db.backends.postgresql')
