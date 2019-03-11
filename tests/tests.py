import unittest
from vkclass import VKUser
from config import FIELDS
from db.db_config import START, STOP


class VKUserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = VKUser('1')
        self.user_data = self.user.get_user_data()

    def test_user_id_isdigit(self):
        value = self.user.user_id.isdigit()
        self.assertTrue(value, 'User ID is not a number')

    def test_user_data_is_dict(self):
        self.assertIsInstance(self.user_data, dict, 'User_data is not a dict type')

    def test_get_groups_is_list(self):
        value = self.user.get_groups()
        self.assertIsInstance(value, list, 'User groups are not type list')

    def test_get_photos_is_list(self):
        value = self.user.get_photos()
        self.assertIsInstance(value, list, 'User groups is not type list')

    def test_search_results_is_list(self):
        value = self.user.search_users(0, 20, 50, 0)
        self.assertIsInstance(value[1], list, 'Search results is not type list')

    def test_search_results_are_instances(self):
        value = self.user.search_users(0, 20, 50, 0)
        self.assertIsInstance(value[1][0], VKUser, 'Search results are not instances of VKUser')


class ParamsTestCase(unittest.TestCase):
    def test_sex_in_fields(self):
        self.assertIn('sex', FIELDS.split(', '), 'Sex is not in FIELDS')

    def test_city_in_fields(self):
        self.assertIn('city', FIELDS.split(', ')[1:3], 'City is not in FIELDS')

    def test_country_in_fields(self):
        self.assertIn('country', FIELDS.split(', ')[1:3], 'Country is not in FIELDS')

    def test_interests_in_fields(self):
        self.assertIn('interests', FIELDS.split(', ')[4:], 'Interests is not in FIELDS')

    def test_music_in_fields(self):
        self.assertIn('music', FIELDS.split(', ')[4:], 'Music is not in FIELDS')

    def test_movies_in_fields(self):
        self.assertIn('movies', FIELDS.split(', ')[4:], 'Movies is not in FIELDS')

    def test_tv_in_fields(self):
        self.assertIn('tv', FIELDS.split(', ')[4:], 'TV is not in FIELDS')

    def test_books_in_fields(self):
        self.assertIn('books', FIELDS.split(', ')[4:], 'Books is not in FIELDS')

    def test_stop_gt_start(self):
        self.assertGreater(STOP, START, 'STOP is not greater than START')
