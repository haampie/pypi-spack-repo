##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCatkinPkg(PythonPackage):
    version("1.0.0", sha256="10a6589e9edf3cd5bd18e35e094d20b516e6351bcf0da891c28a0ff526fdb7cc", url="https://pypi.org/packages/91/f7/86d933ec31f00450f513ef110fa9c0e5da4c6e2c992933a35c8d8fe7d01f/catkin_pkg-1.0.0-py3-none-any.whl")
    version("0.5.2", sha256="4f77ff462261b8f90e170c979ac8b3199e9566fab90667c1736bd9a0ec8e3459", url="https://pypi.org/packages/d7/52/a5395120c9a9a92837d7daf28c4fd26df50ed6e291244c70fef1a1caa5c2/catkin_pkg-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="0b1c2b11f9ca4300ad74d13ee3e2d89261420b107af53683795c5139d0913921", url="https://pypi.org/packages/04/5d/bf7672effe835d6383159ea05f6bde29ba9f8a684f34a1f6d67b872bb8e4/catkin_pkg-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="7dabab73f77ef64ecb23a0e7dc55e1f9dc0bd9ca7aeb83c94647edb6ff626c74", url="https://pypi.org/packages/86/2f/e69c9081bd14ec387a25979224dd9ed4480dab4df53c6bb078fd95cf4a3d/catkin_pkg-0.5.0-py3-none-any.whl")
    version("0.4.24", sha256="6ae0dddcde95689266e91dac13e1d8e9cdec4739bc7e2037b14cbcc1d7af96b2", url="https://pypi.org/packages/33/ac/66c1a11fcfa5f6aeffd4a08209ae77eb19b6a26311e26871e0ddd8d844d3/catkin_pkg-0.4.24-py3-none-any.whl")
    version("0.4.23", sha256="fbfb107e7e7f3167175b6a68bd51eee7d5a85b2e18c4dbee96d715178f029d8c", url="https://pypi.org/packages/32/36/4e418a15c6b0334503f57ff59ccb11a7a3f99c5937d725846110ae1c752d/catkin_pkg-0.4.23-py3-none-any.whl")
    version("0.4.22", sha256="50d17c66fc59bfe3ca1526e945066f19d697a5a99c29f6f9d63cddfce514a950", url="https://pypi.org/packages/55/87/9bc9a93a6f706ab8c97ca3ff65a886acf97c6f2ed009122ace6ce7de3fb7/catkin_pkg-0.4.22-py3-none-any.whl")
    version("0.4.21", sha256="a28473a515b7f4af6f332c38997fea0259b9e34903b43ada014b11ae98a41616", url="https://pypi.org/packages/2c/a3/635adec718c8b0a72eb7933efc22ad84807e9fcc17f44a6472658ad7af77/catkin_pkg-0.4.21-py3-none-any.whl")
    version("0.4.20", sha256="fde59cf9d5955a1e871377a0e6e60026d7297b7859c7698996c85d41cf54d541", url="https://pypi.org/packages/ca/13/9455ffd5f3797812d49d6187901716ebe54be2f20d6c5a3bde8f4c86eff0/catkin_pkg-0.4.20-py3-none-any.whl")
    version("0.4.19", sha256="1356fe2e38117a6d52ec9f1177f816c6384d4feb3ce17cfe84373fcf66d62c45", url="https://pypi.org/packages/d2/97/85e99a8cc0fdf20a80803b9d76760ca77d3db582bc72410dc5c29b14fa3b/catkin_pkg-0.4.19-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-docutils", when="@0.4.3:")
        depends_on("py-pyparsing", when="@0.4.3:0.4.16,0.4.19:")
        depends_on("py-python-dateutil", when="@0.4.3:")
        depends_on("py-setuptools", when="@0.5:")

