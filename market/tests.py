from django.test import TestCase
from django.contrib.auth.models import User
from .models import Listing


class MarketTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        user = User()
        user.save()

        critter = Listing(title="Test Listing", created_by=user, name="test name", desc="test content",
                          species="unknown", age=0, age_Format="Years", sex='?', price=0.00)
        critter.save()

        # slug should be name field + 4 random characters slugified
        self.assertEqual(critter.slug[0:-4], "test-name-")

    def test_listing_fields(self):
        """ Tests the slug generated when saving a Page. """
        user = User()
        user.save()

        critter = Listing(title="Test Listing", created_by=user, name="test name", desc="test content",
                          species="Unknown", age=0, age_Format="Years", sex='?', price=0.10)
        critter.save()

        self.assertEqual(critter.species, 'Unknown')
        self.assertEqual(critter.created_by, user)
        self.assertEqual(critter.name, "test name")
        self.assertEqual(critter.desc, "test content")
        self.assertEqual(critter.age, 0)
        self.assertEqual(critter.age_Format, 'Years')
        self.assertEqual(critter.sex, '?')
        self.assertEqual(critter.price, 0.10)
        self.assertEqual(critter.category, '???')
