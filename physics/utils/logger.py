##########################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# physics_2211  Copyright (C) 2022  Dellius Alexander
# This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type `show c' for details.
##########################################################################
import logging
import logging.config
import os
import string


def log(name=string or bytes, config=string or bytes):
    # get logging.conf src file and configure logger
    logging.config.fileConfig(config)
    # create logger
    return logging.getLogger(name)


# if __name__ == '__main__':
#     logger = __logger(__name__, os.path.relpath('../logging.conf'))
#     logger.debug(msg="Hello World")
