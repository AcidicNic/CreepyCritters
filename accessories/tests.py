from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item
from CreepyCrittersMain.settings import STATIC_ROOT


class AccessoriesTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_item_slugify_on_save(self):
        """ Tests the slug generated when saving an Item """
        user = User()
        user.save()

        item = Item(title="Test Item", created_by=user, info="test content", item_img=STATIC_ROOT+'/default-icon.jpg', price=105.97)
        item.save()

        # slug should be name field + 3 random characters slugified
        self.assertEqual(item.slug[0:-3], "test-item-")

    def test_item_fields(self):
        """ Tests Item fields """
        user = User()
        user.save()

        item = Item(title="Test Item", created_by=user, info="test content", item_img=STATIC_ROOT+'/default-icon.jpg', price=105.97)
        item.save()

        self.assertEqual(item.title, 'Test Item')
        self.assertEqual(item.created_by, user)
        self.assertEqual(item.info, "test content")
        self.assertEqual(item.item_img, STATIC_ROOT+'/default-icon.jpg')
        self.assertEqual(item.price, 105.97)
