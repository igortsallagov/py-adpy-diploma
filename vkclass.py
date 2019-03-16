import requests
from config import API_URL, VERSION, TOKEN, FIELDS


class VKUser:

    def __init__(self, user_id):
        user_id = str(user_id)
        self.error = 0
        if user_id.isdigit() is False:
            params_init = dict(access_token=TOKEN, user_ids=user_id, v=VERSION)
            method_url = f'{API_URL}/users.get'
            request = requests.get(method_url, params_init).json()
            try:
                user_id = request['response'][0]['id']
                self.user_id = user_id
            except KeyError:
                code = request['error']['error_code']
                if code == 5:
                    self.error = 5
                elif code == 18:
                    self.error = 18
                elif code == 113:
                    self.error = 113
        else:
            self.user_id = user_id
        self.user_data = {}
        self.sex = 0
        self.city = 0
        self.country = 0
        self.common_count = 0
        self.interests = ''
        self.music = ''
        self.tv = ''
        self.books = ''
        self.movies = ''
        self.score = 0

    def get_user_data(self):
        method_url = f'{API_URL}/users.get'
        params_users_get = dict(access_token=TOKEN, user_id=self.user_id, v=VERSION, fields=FIELDS)
        result = requests.get(method_url, params_users_get).json()
        try:
            self.user_data = result['response'][0]
        except KeyError:
            code = result['error']['error_code']
            if code == 18:
                self.error = 18
            elif code == 113:
                self.error = 113
        try:
            self.sex = self.user_data['sex']
        except KeyError:
            pass
        try:
            self.city = self.user_data['city']['id']
        except KeyError:
            pass
        try:
            self.country = self.user_data['country']['id']
        except KeyError:
            pass
        try:
            self.common_count = self.user_data['common_count']
        except KeyError:
            pass
        try:
            self.interests = self.user_data['interests']
        except KeyError:
            pass
        try:
            self.music = self.user_data['music']
        except KeyError:
            pass
        try:
            self.tv = self.user_data['tv']
        except KeyError:
            pass
        try:
            self.books = self.user_data['books']
        except KeyError:
            pass
        try:
            self.movies = self.user_data['movies']
        except KeyError:
            pass
        return self.user_data

    def update_user_data(self, kwargs):
        if self.city is 0:
            self.city = int(kwargs['city'])
            self.user_data['city'] = {'id': self.city, 'title': ''}
        if self.country is 0:
            self.country = int(kwargs['country'])
            self.user_data['country'] = {'id': self.country, 'title': ''}
        if self.interests is '':
            self.interests = kwargs['interests']
            self.user_data['interests'] = self.interests
        if self.music is '':
            self.music = kwargs['music']
            self.user_data['music'] = self.music
        if self.movies is '':
            self.movies = kwargs['movies']
            self.user_data['movies'] = self.movies
        if self.tv is '':
            self.tv = kwargs['tv']
            self.user_data['tv'] = self.tv
        if self.books is '':
            self.books = kwargs['books']
            self.user_data['books'] = self.books

    def get_groups(self):
        method_url = f'{API_URL}/groups.get'
        params_get_groups = dict(access_token=TOKEN, user_id=self.user_id, count=1000, v=VERSION)
        try:
            result = requests.get(method_url, params_get_groups).json()['response']['items']
        except KeyError:
            result = []
        return result

    def get_photos(self):
        method_url = f'{API_URL}/photos.get'
        params_get_groups = dict(access_token=TOKEN, owner_id=self.user_id, count=1000, v=VERSION,
                                 album_id='profile', extended=1)
        try:
            result = requests.get(method_url, params_get_groups).json()['response']['items']
        except KeyError:
            result = []
        return result

    def search_users(self, sex, age_from, age_to, offset):
        method_url = f'{API_URL}/users.search'
        params_users_search = dict(access_token=TOKEN, v=VERSION, fields=FIELDS,
                                   count=100, city=self.city, country=self.country, sex=sex,
                                   age_from=age_from, age_to=age_to, has_photo=1, sort=0, offset=offset)
        request = requests.get(method_url, params_users_search).json()
        try:
            result = request['response']['items']
            result_instances = list()
            for item in result:
                instance = VKUser(item['id'])
                result_instances.append(instance)
                try:
                    instance.sex = item['sex']
                except KeyError:
                    pass
                try:
                    instance.city = item['city']['id']
                except KeyError:
                    pass
                try:
                    instance.country = item['country']['id']
                except KeyError:
                    pass
                try:
                    instance.common_count = item['common_count']
                except KeyError:
                    pass
                try:
                    instance.interests = item['interests']
                except KeyError:
                    pass
                try:
                    instance.music = item['music']
                except KeyError:
                    pass
                try:
                    instance.tv = item['tv']
                except KeyError:
                    pass
                try:
                    instance.books = item['books']
                except KeyError:
                    pass
                try:
                    instance.movies = item['movies']
                except KeyError:
                    pass
        except KeyError:
            result = request['error']
            result_instances = None
        return result, result_instances
