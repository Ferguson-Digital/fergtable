import json
import os
import sys

from django.core.management.base import BaseCommand

from baserow.core.handler import CoreHandler
from baserow.core.models import Application


class Command(BaseCommand):
    help = (
        "Exports a single application to a JSON file that can later be "
        "imported via the `import_group_applications` management command. A ZIP file "
        "containing all the files is also exported, this will for example contain the "
        "files uploaded to a file field."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "app_id", type=int, help="The id of the application that must be exported."
        )
        parser.add_argument(
            "--indent",
            action="store_true",
            help="Indicates if the JSON must be formatted and indented to improve "
            "readability.",
        )
        parser.add_argument(
            "--name",
            type=str,
            help="The JSON and ZIP files are going to be named `app_ID.json` and "
            "`app_ID.zip` by default, but can optionally be named differently by "
            "proving this argument.",
        )

    def handle(self, *args, **options):
        app_id = options["app_id"]
        indent = options["indent"]
        name = options["name"]

        try:
            application = Application.objects.get(pk=app_id)
        except Application.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f"The application with id {app_id} was not " f"found.")
            )
            sys.exit(1)

        file_name = name or f"app_{application.id}"
        current_path = os.path.abspath(os.getcwd())
        files_path = os.path.join(current_path, f"{file_name}.zip")
        export_path = os.path.join(current_path, f"{file_name}.json")

        with open(files_path, "wb") as files_buffer:
            exported_application = CoreHandler().export_single_application(
                application, files_buffer=files_buffer
            )

        with open(export_path, "w") as export_buffer:
            json.dump(
                [exported_application,], export_buffer, indent=4 if indent else None
            )
