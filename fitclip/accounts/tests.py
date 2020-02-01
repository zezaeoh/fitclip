from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class UserProfileTestCase(APITestCase):
    profiles_url = reverse('profiles')

    def setUp(self):
        # create a new user making a post request to djoser endpoint
        self.user = self.client.post(
            '/auth/users/',
            data={
                'username': 'mario',
                'password': 'i-keep-jumping'
            })
        self.user_pk = self.user.json()['id']

        # obtain a json web token for the newly created user
        response = self.client.post(
            '/auth/jwt/create/',
            data={
                'username': 'mario',
                'password': 'i-keep-jumping'
            })

        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    # retrieve a list of all user profiles while the request user is authenticated
    def test_user_profile_list_authenticated(self):
        response = self.client.get(self.profiles_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # retrieve a list of all user profiles while the request user is unauthenticated
    def test_user_profile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profiles_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # check to retrieve the profile details of the authenticated user
    def test_user_profile_detail_retrieve(self):
        response = self.client.get(reverse('profile', kwargs={'pk': self.user_pk}))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # populate the user profile that was automatically created using the signals
    def test_user_profile_profile(self):
        profile_data = {
            'description': 'I am a very famous game character',
            'location': 'nintendo world',
            'is_creator': 'true',
        }
        response = self.client.put(reverse('profile', kwargs={'pk': self.user_pk}), data=profile_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
