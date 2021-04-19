from rest_framework.test import APITestCase
from audioapi.models import AudioBook
from rest_framework import status


class AudioBookTestCase(APITestCase):

    def Test_get_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/audiobook/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        audiobook = AudioBook.objects.filter(id=1)
        self.assertEqual(audiobook.count(), 1)
        self.assertEqual(AudioBook.objects.get().id, 1)

    def Test_list_audiobook(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/audiobook/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        audiobook = AudioBook.objects.all()
        self.assertEqual(audiobook.count(), 1)

    def Test_delete_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/audiobook/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url)
        self.assertEqual(response.status_code,
                         status.HTTP_500_INTERNAL_SERVER_ERROR)

    def Test_post_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/'
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "hello",
                "author": "jahan",
                "narrator": "filed",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def Test_put_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/audiobook/1'
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "hello",
                "author": "jahan",
                "narrator": "filed",
                "duration": 50
            }
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def Test_required_paramters(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/'
        data = {
            "audioFileMetadata": {
                "title": "hello",
                "author": "jahan",
                "narrator": "filed",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = {
            "audioFileType": "audiobook",
            "title": "hello",
            "author": "jahan",
            "narrator": "filed",
            "duration": 50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "author": "jahan",
                "narrator": "filed",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "hello",
                "narrator": "filed",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "hello",
                "author": "jahan",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "hello",
                "author": "jahan",
                "narrator": "filed"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sequence(self):
        self.Test_post_method()
        self.Test_get_method()
        self.Test_list_audiobook()
        self.Test_put_method()
        self.Test_delete_method()
        self.Test_required_paramters()
