from rest_framework.test import APITestCase
from audioapi.models import AudioBook
from rest_framework import status


class AudioBookTestCase(APITestCase):
    def test_invalid_audiotypefield(self):
        url = 'http://127.0.0.1:8000/api/v1/audio/'
        data = {
            "audioFileType": "filed",
            "audioFileMetadata": {
                "name": "kolvari.mp3",
                "duration": 50
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


def test_invalid_audiofilemetadatakey(self):
    url = 'http://127.0.0.1:8000/api/v1/audio/'
    data = {
        "audioFileType": "song",
        "metadata": {
            "name": "kolvari.mp3",
            "duration": 50
        }
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
