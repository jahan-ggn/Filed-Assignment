from rest_framework.test import APITestCase
from audioapi.models import Podcast
from rest_framework import status


class PodcastTestCase(APITestCase):

    def Test_get_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/podcast/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        podcast = Podcast.objects.filter(id=1)
        self.assertEqual(podcast.count(), 1)
        self.assertEqual(Podcast.objects.get().id, 1)

    def Test_list_podcast(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/podcast/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        podcast = Podcast.objects.all()
        self.assertEqual(podcast.count(), 1)

    def Test_delete_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/podcast/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url)
        self.assertEqual(response.status_code,
                         status.HTTP_500_INTERNAL_SERVER_ERROR)

    def Test_post_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/'
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50,
                "host": "localhost",
                "participants": "'jahan','gagan'"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def Test_put_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/podcast/1'
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50,
                "host": "localhost",
                "participants": "'jahan','gagan'"
            }
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def Test_required_paramters(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/'
        data = {
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50,
                "host": "localhost",
                "participants": "'jahan'"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = {
            "audioFileType": "podcast",
            "name": "hello.mp3",
            "duration": 50,
            "host": "localhost",
            "participants": "'jahan','gagan'"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "duration": 50,
                "host": "localhost",
                "participants": "'jahan','gagan'"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "hello.mp3",
                "host": "localhost",
                "participants": "'jahan','gagan'"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50,
                "participants": "'jahan','gagan'"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50,
                "participants": "'jahan','gagan','a','b','c','d','e','f','g','h','i'"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50,
                "participants": "'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sequence(self):
        self.Test_post_method()
        self.Test_get_method()
        self.Test_list_podcast()
        self.Test_put_method()
        self.Test_delete_method()
        self.Test_required_paramters()
