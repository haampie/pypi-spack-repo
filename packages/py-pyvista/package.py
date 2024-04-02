# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyvista(PythonPackage):
    # BEGIN VERSIONS
    version("0.42.3", sha256="b6170689209eec58246b32abb3c5f99246b45948e51228504cda2d4d301e7463", url="https://pypi.org/packages/6d/ee/24d100341e673347f80347ec8f20b4e48b1326fd968d7fb1139829f8bb66/pyvista-0.42.3-py3-none-any.whl")
    version("0.38.6", sha256="661c0c550fa63a748a2361bc4bbff52ba5e8f22a32991be64ec8ec6b14754a1d", url="https://pypi.org/packages/f7/67/21198db0c97bdff0cd5b6c3913765cca1faf1168068c66370e2fe13c01aa/pyvista-0.38.6-py3-none-any.whl")
    version("0.22.4", sha256="1647b08530c48d58b39dfcca86c3af913946a3859ffff4c4a1b1a657679ffea4", url="https://pypi.org/packages/3d/00/d4904a3b587beb4d42980a40323726926b82ba5beeadfb0c367f879f804b/pyvista-0.22.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.39:")
        depends_on("python@3.7:", when="@0.38")
        depends_on("py-imageio", when="@0.38")
        depends_on("py-matplotlib@3.0.1:", when="@0.39:")
        depends_on("py-numpy", when="@0.38:0.42")
        depends_on("py-pillow", when="@0.38:")
        depends_on("py-pooch", when="@0.38:")
        depends_on("py-scooby@0.5.1:", when="@0.38:")
        depends_on("py-typing-extensions", when="@0.38 ^python@:3.7")
        depends_on("py-vtk", when="@0.38:")
    # END DEPENDENCIES

