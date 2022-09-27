# Physics 2211

[![Build, Test, Package](https://github.com/dellius-alexander/physics/actions/workflows/build_test_deploy.yml/badge.svg?branch=main)](https://github.com/dellius-alexander/physics/actions/workflows/build_test_deploy.yml)


## Project Directory Structure

```text
physics
    manage.py
    README.md
    development.env  # name=value pair file of environment variables
    requirements.txt
    pyproject.toml
    config/
        __init__.py
        asgi.py
        my.conf     # mysql settings file
        settings.py
        urls.py
        wsgi.py
    templates/
        index.html
    physics/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```