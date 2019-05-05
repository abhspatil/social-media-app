#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agri_django_server_public.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)