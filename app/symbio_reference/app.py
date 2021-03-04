"""Application entry point."""

import logging

from symbio_reference import APP

logger = logging.getLogger(APP.name)


def main():
    """Main app entry point."""

    logger.info(f"Name:'{APP.name}'")


if __name__ == '__main__':
    main()
