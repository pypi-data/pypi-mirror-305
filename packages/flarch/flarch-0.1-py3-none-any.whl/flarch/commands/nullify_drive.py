import shlex
import os

from flarch.utils.size_of_drive import size_of_drive


def nullify_drive(drive_name):
    drive_name = shlex.quote(drive_name)

    print(f"Nullification of '{drive_name}' has started")
    os.system(
        f"dd if=/dev/zero | pv -s {size_of_drive(drive_name)} | dd of={drive_name}"
    )
