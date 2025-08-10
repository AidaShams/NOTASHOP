from django.test import TestCase
from django.urls import reverse
from .models import Category, Sticker
# Create your tests here.

class StickerModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Movies", slug="movies")
        self.sticker = Sticker.objects.create(
            name="Green Mile",
            description="An inspiring movie.",
            price=170,
            tags="movie,inspiring",
            stock=10,
            is_active=True,
            category=self.category
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), "Movies")

    def test_sticker_str(self):
        self.assertEqual(str(self.sticker), "Green Mile ($170)")

    def test_slug_auto_generated(self):
        self.assertEqual(self.sticker.slug, "green-mile")

    def test_fields_values(self):
        self.assertEqual(self.sticker.name, "Green Mile")
        self.assertEqual(self.sticker.description, "An inspiring movie.")
        self.assertEqual(self.sticker.price, 170)
        self.assertEqual(self.sticker.stock, 10)
        self.assertTrue(self.sticker.is_active)
        self.assertEqual(self.sticker.category, self.category)

    def test_get_absolute_url(self):
        expected_url = reverse('sticker_detail', args=[self.sticker.slug])
        self.assertEqual(self.sticker.get_absolute_url(), expected_url)


class StickerViewsTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Movies", slug="movies")
        self.sticker = Sticker.objects.create(
            name="Green Mile",
            description="An inspiring movie.",
            price=170,
            tags="movie,inspiring",
            stock=10,
            is_active=True,
            category=self.category
        )

    def test_sticker_list_view(self):
        response = self.client.get(reverse('sticker_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/sticker_list.html')

    def test_sticker_detail_view(self):
        response_ok = self.client.get(self.sticker.get_absolute_url())
        response_not_found = self.client.get('/stickers/not-a-real-slug/')
        self.assertEqual(response_ok.status_code, 200)
        self.assertEqual(response_not_found.status_code, 404)
        self.assertTemplateUsed(response_ok, 'store/sticker_detail.html')