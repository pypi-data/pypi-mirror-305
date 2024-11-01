import argparse

from flarch.commands.format_drive import format_drive
from flarch.commands.nullify_drive import nullify_drive
from flarch.commands.write_image import write_image
from flarch.utils.commands_exist import ensure_commands_exist


def main():
    parser = argparse.ArgumentParser(description="Work with floppies with ease!")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # region Format floppy
    format_parser = subparsers.add_parser("format", help="Format the floppy into FAT")
    format_parser.add_argument("drive", type=str, help="Floppy drive")
    # endregion

    # region Nullify floppy
    nullify_parser = subparsers.add_parser(
        "nullify", help="Turn all floppy sectors into zeroes"
    )
    nullify_parser.add_argument("drive", type=str, help="Floppy drive")
    # endregion

    # region Write image
    write_parser = subparsers.add_parser(
        "write", help="Turn all floppy sectors into zeroes"
    )
    write_parser.add_argument(
        "-from", "--image-from", type=str, help=".img file", required=True
    )
    write_parser.add_argument(
        "-to", "--drive-to", type=str, help="Floppy drive", required=True
    )
    write_parser.add_argument(
        "-N",
        "--skip-nullification",
        action="store_true",
        help="Skip drive nullification. Faster, but the resulting floppy may work unexpectedly",
    )
    # endregion

    args = parser.parse_args()

    ensure_commands_exist(["blockdev", "mkfs.vfat", "dd", "pv"])

    if args.command == "nullify":
        nullify_drive(args.drive)

    if args.command == "format":
        nullify_drive(args.drive)
        format_drive(args.drive)

    if args.command == "write":
        if not args.skip_nullification:
            nullify_drive(args.drive_to)

        write_image(image_path=args.image_from, drive=args.drive_to)


if __name__ == "__main__":
    main()
