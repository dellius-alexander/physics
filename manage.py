#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
import django

load_dotenv('development.env')


def main():
    try:
        """Checking DJANGO_ENV settings."""
        if not os.environ.get('DJANGO_ENV', False):
            raise EnvironmentError('Please define DJANGO_ENV environment variable')

        """Run administrative tasks."""
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'config.settings.{}'.format(os.environ.get('DJANGO_ENV')))

        """Set mysql home my.cnf we have our custom settings"""
        os.environ.setdefault('MYSQL_HOME',
                              'config.settings.{}'.format(os.environ.get('MYSQL_HOME')))

        # Override default port and address for `runserver` command
        from django.core.management.commands.runserver import Command
        Command.default_port = os.environ.get('ALLOWED_PORTS')
        Command.default_addr = os.environ.get('DEFAULT_ADDRESS')

        from django.core.management import execute_from_command_line

    except Exception as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
