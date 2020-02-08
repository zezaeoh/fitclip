import datetime
import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class DatePathAndRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        now = datetime.datetime.now()
        ext = filename.split('.')[-1]  # eg: 'jpg'
        uid = uuid.uuid4().hex[:10]  # eg: '567ae32f97'

        renamed_filename = f'{uid}.{ext}'
        path = f"{now.year}/{now.month}/{now.day}/{renamed_filename}"
        return os.path.join(self.path, path)


@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]  # eg: 'jpg'
        uid = uuid.uuid4().hex[:10]  # eg: '567ae32f97'

        renamed_filename = f'{instance.product.name}/{uid}.{ext}'
        return os.path.join(self.path, renamed_filename)