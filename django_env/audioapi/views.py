from django.core.exceptions import ObjectDoesNotExist
from .serializers import SongSerializer, AudioBookSerializer, PodcastSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .models import Song, Podcast, AudioBook


class AudioApi(APIView):
    def post(self, request):

        data = request.data
        audio_type = data.get("audioFileType", None)
        metadata = data.get("audioFileMetadata", None)

        if audio_type is None or metadata is None:
            return Response(
                {"msg": "required parameters are not given"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = None

        if audio_type == "song":
            serializer = SongSerializer(data=metadata)
        elif audio_type == "podcast":
            participants = metadata.get("participants", None)
            if participants is not None:
                participants = participants.split(",")

                if len(participants) > 10:
                    return Response(
                        {"msg": "maximum 10 participants are allowed"},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                if any(i for i in participants if len(i) > 100):
                    return Response(
                        {
                            "msg": "length of participants cannot be greater than 100 characters"
                        },
                        status=status.HTTP_404_NOT_FOUND,
                    )

            serializer = PodcastSerializer(data=metadata)

        elif audio_type == "audiobook":
            serializer = AudioBookSerializer(data=metadata)

        if serializer is not None:

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "msg": "{} added successfully".format(audio_type),
                        audio_type: serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {"msg": "something went wrong", "error": serializer.errors},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"msg": "something is wrong with audiotype parameter"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def get(self, request, audio_type, pk=None):

        audio = None
        serializer = None

        try:

            if pk is not None:
                if audio_type == "song":
                    audio = Song.objects.get(id=pk)
                    serializer = SongSerializer(audio)
                elif audio_type == "podcast":
                    audio = Podcast.objects.get(id=pk)
                    serializer = PodcastSerializer(audio)
                elif audio_type == "audiobook":
                    audio = AudioBook.objects.get(id=pk)
                    serializer = AudioBookSerializer(audio)

            else:
                if audio_type == "song":
                    audio = Song.objects.all()
                    serializer = SongSerializer(audio, many=True)
                elif audio_type == "podcast":
                    audio = Podcast.objects.all()
                    serializer = PodcastSerializer(audio, many=True)
                elif audio_type == "audiobook":
                    audio = AudioBook.objects.all()
                    serializer = AudioBookSerializer(audio, many=True)

        except ObjectDoesNotExist:
            return Response(
                {"msg": "{} matching query does not exists".format(
                    audio_type)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if audio and serializer:
            return Response(
                {
                    "msg": "{} fetched successfully".format(audio_type),
                    audio_type: serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"msg": "something went wrong"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, audio_type, pk):

        data = request.data
        audio_type = data.get("audioFileType", None)
        metadata = data.get("audioFileMetadata", None)
        id = pk

        if audio_type is None or metadata is None:
            return Response(
                {"msg": "required parameters are not given"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if audio_type == "podcast":
            participants = metadata.get("participants", None)
            if participants is not None:
                participants = participants.split(",")

                if len(participants) > 10 or any(
                    i for i in participants if len(i) > 100
                ):
                    return Response(
                        {"msg": "something wrong with participants field"},
                        status=status.HTTP_404_NOT_FOUND,
                    )

        serializer = None

        try:
            if audio_type == "song":
                audio = Song.objects.get(pk=id)
                serializer = SongSerializer(audio, data=metadata)
            elif audio_type == "podcast":
                audio = Podcast.objects.get(pk=id)
                serializer = PodcastSerializer(audio, data=metadata)
            elif audio_type == "audiobook":
                audio = AudioBook.objects.get(pk=id)
                serializer = AudioBookSerializer(audio, data=metadata)

        except ObjectDoesNotExist:
            return Response(
                {"msg": "{} matching query does not exists".format(
                    audio_type)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if serializer is not None:
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "msg": "{} updated successfully".format(audio_type),
                        audio_type: serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                {"msg": "something went wrong", "error": serializer.errors},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"msg": "something is wrong with audiotype parameter"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def delete(self, request, audio_type, pk):
        id = pk

        try:
            if audio_type == "song":
                audio = Song.objects.get(pk=id)
            elif audio_type == "podcast":
                audio = Podcast.objects.get(pk=id)
            elif audio_type == "audiobook":
                audio = AudioBook.objects.get(pk=id)

        except ObjectDoesNotExist:
            return Response(
                {"msg": "{} matching query does not exists".format(
                    audio_type)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        audio.delete()

        return Response(
            {"msg": "{} deleted successfully".format(audio_type)},
            status=status.HTTP_200_OK,
        )
