from flask import current_app, url_for, flash, redirect, request
import urllib3
import json

http = urllib3.PoolManager()


class Service:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class OAuthSignIn:
    providers = None
    __instance = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.client_id = credentials['client_id']
        self.client_secret = credentials['client_secret']
        self.redirect_url = request.host_url + credentials['redirect_uri']
        print("REDIRECT", self.redirect_url)
        self.service = None

    def authorize(self):
        url = f'{self.service.authorize_url}/?client_id={self.client_id}&display=page&redirect_uri={self.redirect_url}&scope=friends&response_type=code&v=5.122'
        response = http.request('GET', url=url)
        return response

    def authorize_access_token(self, code):
        url = f'{self.service.access_token_url}/?client_id={self.client_id}&client_secret={self.client_secret}&redirect_uri={self.redirect_url}&code={code}'
        response = http.request('GET', url=url)
        return response

    @classmethod
    def get_instance(cls, provider_name):
        if not cls.__instance:
            cls.__instance = cls(provider_name)
            return cls.__instance
        else:
            return cls.__instance


class VKSignIn(OAuthSignIn):
    def __init__(self, provider_name):
        super(VKSignIn, self).__init__('vk')
        self.service = Service(
            name='vk',
            client_id=self.client_id,
            client_secret=self.client_secret,
            authorize_url='https://oauth.vk.com/authorize',
            access_token_url='https://oauth.vk.com/access_token',
            base_url='https://oauth.vk.com/'
        )

    def get_info(self, access_token):
        user_data = {}
        url = f'https://api.vk.com/method/users.get?access_token={access_token}&fields=photo_200&v=5.52'
        response = http.request('GET', url=url)
        data = json.loads(response.data.decode('utf-8'))
        if "error" in data:
            flash(data.get("error"))
            flash(data.get("error_description"))
            return None

        user_data.update(data['response'][0])

        url = f'https://api.vk.com/method/friends.get?access_token={access_token}&count=5&fields=photo_200&v=5.52'
        response = http.request('GET', url=url)
        data = json.loads(response.data.decode('utf-8'))
        if "error" in data:
            flash(data.get("error"))
            flash(data.get("error_description"))
            return redirect('/')
        user_data.update({'friends': data['response']['items']})
        return user_data
