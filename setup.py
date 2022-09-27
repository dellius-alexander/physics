#!/usr/bin/env python3

from setuptools import setup, find_packages

# from dotenv import load_dotenv
# load_dotenv("development.env")

# Please see for more information:
# https://docs.python.org/3.8/distutils/apiref.html?highlight=setup#distutils.core.setup
# https://docs.python.org/3/distutils/setupscript.html
setup(
    name='physics',
    # version='1.1',
    # description='''Linear motion in physics''',
    author='Dellius Alexander',
    author_email='info@hyfisolutions.com',
    url='https://github.com/dellius-alexander/physics.git',
    maintainer="Dellius Alexander, Clayton State University, Atlanta, GA <info@hyfisolutions.com>",
    maintainer_email="info@hyfisolutions.com, dellius.alexander@gmail.com",
    #     long_description="""
    # \"Physics is devoted to the understanding of all natural phenomena.
    # In physics, we try to understand physical phenomena at all scales—from
    # the world of subatomic particles to the entire universe. Despite the
    # breadth of the subject, the various subfields of physics share a
    # common core. The same basic training in physics will prepare you to
    # work in any area of physics and the related areas of science and
    # engineering. In this section, we investigate the scope of physics;
    # the scales of length, mass, and time over which the laws of physics
    # have been shown to be applicable; and the process by which science
    # in general, and physics in particular, operates.\"
    #
    # -------------------------------------------------------------------
    # References:
    # -------------------------------------------------------------------
    # Ling, S. J., Sanny, J., &amp; Moebs, W. (2017). University Physics:
    #   Volume 1 (Vol. 1). OpenStax, Rice University.
    # -------------------------------------------------------------------
    # """,
    # download_url="",
    # py_modules=['physics', 'physics.migrations', 'physics.utils', 'src'],
    # scripts=[],
    # ext_modules=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    # distclass=types[dist],
    # script_name="",
    # script_args=[],
    # options=map[str, ],
    # license="LICENSE",
    # keywords=[],
    # platforms=[],
    # cmdclass=map[str, []],
    # data_files=[tuple(str, [])],
    # package_dir=map[str, str],
    # obsoletes=[],
    # provides=[],
    # install_requires=[
    #     'cycler==0.11.0',
    #     'fonttools==4.37.1',
    #     'kiwisolver==1.4.4',
    #     'matplotlib==3.5.3',
    #     'mpmath==1.2.1',
    #     'numpy>=1.16.5,<=1.23.2',
    #     'packaging==21.3',
    #     'pandas>=1.3.5,<=1.4.4',
    #     'pep517==0.13.0',
    #     'Pillow==9.2.0',
    #     'pyparsing==3.0.9',
    #     'python-dateutil==2.8.2',
    #     'pytz==2022.2.1',
    #     'six==1.16.0',
    #     'sympy>=1.10.1,<=1.11',
    #     'tomli==2.0.1',
    #     'pytest',
    #     'flake8~=5.0.4',
    #     'asgiref==3.5.2',
    #     'backports.zoneinfo==0.2.1',
    #     'Django==4.1.1',
    #     'mysqlclient==2.1.1',
    #     'python-dotenv==0.21.0',
    #     'sqlparse==0.4.2',
    #     'Django-MathJax'
    # ],
    # command_packages=[],
    # command_options=map[str, [str, ()]],
    # packages=find_packages(include='.', exclude=['tests']),
    # package_data={
    #     'templates': ['physics/*.html'],
    #     'static': ['physics/css/*.css', 'physics/js/*.js', 'physics/img/*.png', 'physics/img/*.jpg']
    #       },
    # include_package_data=False,
    # libraries=[],
    # headers=[],
    # ext_package="",
    # include_dirs=['templates', 'static'],
    # password="",
    # fullname=""
)
