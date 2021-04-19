from rest_framework.test import APITestCase
from audioapi.models import Song
from rest_framework import status


class SongTestCase(APITestCase):

    def Test_get_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/song/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        song = Song.objects.filter(id=1)
        self.assertEqual(song.count(), 1)
        self.assertEqual(Song.objects.get().id, 1)

    def Test_list_song(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/song/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        song = Song.objects.all()
        self.assertEqual(song.count(), 1)

    def Test_delete_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/song/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url)
        self.assertEqual(response.status_code,
                         status.HTTP_500_INTERNAL_SERVER_ERROR)

    def Test_post_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/'
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def Test_put_method(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/song/1'
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "world.mp3",
                "duration": 150
            }
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def Test_required_paramters(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/'
        data = {
            "audioFileMetadata": {
                "name": "hello.mp3",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = {
            "audioFileType": "song",
            "name": "kolvari.mp3",
            "duration": 50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "world.mp3",
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "duration": 150
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sequence(self):
        self.Test_post_method()
        self.Test_get_method()
        self.Test_list_song()
        self.Test_put_method()
        self.Test_delete_method()
        self.Test_required_paramters()
