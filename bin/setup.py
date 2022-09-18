#!/usr/bin/env python3

from distutils.core import setup
from distutils import dist
import types

# Please see for more information:
# https://docs.python.org/3.8/distutils/apiref.html?highlight=setup#distutils.core.setup
# https://docs.python.org/3/distutils/setupscript.html
setup(name='physics',
      version='0.1.1',
      description='''Linear motion in physics''',
      author='Dellius Alexander',
      author_email='info@hyfisolutions.com',
      url='https://github.com/dellius-alexander/physics.git',
      packages=['physics', 'physics.motion_3d', 'physics.utils', 'tests'],
      maintainer="Dellius Alexander, Clayton State University, Atlanta, GA <info@hyfisolutions.com>",
      maintainer_email="info@hyfisolutions.com, dellius.alexander@gmail.com",
      long_description="""
      \"Physics is devoted to the understanding of all natural phenomena. 
      In physics, we try to understand physical phenomena at all scales—from 
      the world of subatomic particles to the entire universe. Despite the 
      breadth of the subject, the various subfields of physics share a 
      common core. The same basic training in physics will prepare you to 
      work in any area of physics and the related areas of science and 
      engineering. In this section, we investigate the scope of physics; 
      the scales of length, mass, and time over which the laws of physics 
      have been shown to be applicable; and the process by which science 
      in general, and physics in particular, operates.\"
      
      -------------------------------------------------------------------
      References:
      -------------------------------------------------------------------
      Ling, S. J., Sanny, J., &amp; Moebs, W. (2017). University Physics: 
          Volume 1 (Vol. 1). OpenStax, Rice University. 
      -------------------------------------------------------------------    
      """
      # download_url="",
      # py_modules=[],
      # scripts=[],
      # ext_modules=[],
      # classifiers=[],
      # distclass=types[dist],
      # script_name="",
      # script_args=[],
      # options=map[str, ],
      # license="",
      # keywords=[],
      # platforms=[],
      # cmdclass=map[str, []],
      # data_files=[tuple(str, [])],
      # package_dir=map[str, str],
      # obsoletes=[],
      # provides=[],
      # requires=[],
      # command_packages=[],
      # command_options=map[str, [str, ()]],
      # package_data=map[str, [str]],
      # include_package_data=False,
      # libraries=[],
      # headers=[],
      # ext_package="",
      # include_dirs=[],
      # password="",
      # fullname=""
      )
