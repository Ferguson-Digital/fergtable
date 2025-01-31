import mimetypes

from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

from PIL import Image

from baserow.core.user_files.handler import UserFileHandler
from baserow.core.user_files.models import UserFile


class Command(BaseCommand):
    help = (
        "Regenerates all the user file thumbnails based on the current settings. "
        "Existing files will be overwritten."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "name",
            type=str,
            nargs="?",
            help="The name of the thumbnails to regenerate (tiny, small or card_cover).",
            default=None,
        )

    def handle(self, *args, **options):
        """
        Regenerates the thumbnails of all image user files. If the USER_THUMBNAILS
        setting ever changes then this file can be used to fix all the thumbnails.
        """

        i = 0
        handler = UserFileHandler()
        buffer_size = 100
        queryset = UserFile.objects.all()
        count = queryset.count()

        while i < count:
            user_files = queryset[i : min(count, i + buffer_size)]
            for user_file in user_files:
                i += 1

                full_path = handler.user_file_path(user_file)
                mime_type = mimetypes.guess_type(full_path)[0]
                try:
                    stream = default_storage.open(full_path)
                except FileNotFoundError:
                    continue

                image = None

                try:
                    image = Image.open(stream)
                except IOError:
                    pass

                handler.generate_and_save_file_thumbnails(
                    stream,
                    mime_type,
                    image,
                    user_file,
                    storage=default_storage,
                    only_with_name=options["name"],
                )

                stream.close()

                if image:
                    image.close()

        self.stdout.write(self.style.SUCCESS(f"{i} thumbnails have been regenerated."))
