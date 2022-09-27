[![Build, Test, Package](https://github.com/dellius-alexander/physics/actions/workflows/build_test_deploy.yml/badge.svg?branch=main)](https://github.com/dellius-alexander/physics/actions/workflows/build_test_deploy.yml)

# Physics

Physics is devoted to the understanding of all natural phenomena.
In physics, we try to understand physical phenomena at all scales—from
the world of subatomic particles to the entire universe. Despite the
breadth of the subject, the various subfields of physics share a
common core. The same basic training in physics will prepare you to
work in any area of physics and the related areas of science and
engineering. In this section, we investigate the scope of physics;
the scales of length, mass, and time over which the laws of physics
have been shown to be applicable; and the process by which science
in general, and physics in particular, operates.

---

## Project Directory Structure

```text
physics
    setup.cfg
    MANIFEST.in
    manage.py
    README.md
    development.env  # name=value pair file of environment variables
    requirements.txt
    pyproject.toml
    LICENSE
    logging.conf
    .gitignore
    config/
        __init__.py
        asgi.py
        my.conf     # mysql settings file
        settings.py
        urls.py
        wsgi.py
    static/
        physics/
            css/
            js/
            img/
    templates/
        physics/
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