# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOutcome(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.0.post0", sha256="e771c5ce06d1415e356078d3bdd68523f284b4ce5419828922b6871e65eda82b", url="https://pypi.org/packages/55/8b/5ab7257531a5d830fc8000c476e63c935488d74609b50f9384a643ec0a62/outcome-1.3.0.post0-py2.py3-none-any.whl")
    version("1.3.0", sha256="7b688fd82db72f4b0bc9e883a00359d4d4179cd97d27f09c9644d0c842ba7786", url="https://pypi.org/packages/fa/63/0807d3bc1742adffd2bac458829f3f71ce3aa29bec44a8ac008aed2b467c/outcome-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="c4ab89a56575d6d38a05aa16daeaa333109c1f96167aba8901ab18b6b5e0f7f5", url="https://pypi.org/packages/e9/4f/2f2d3f65d851852712b4de3fd0cfdcec9c5e9a9c347430e004ba770ef4db/outcome-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="c7dd9375cfd3c12db9801d080a3b63d4b0a261aa996c4c13152380587288d958", url="https://pypi.org/packages/0d/bb/f60ce97b304b1979d1fef96b6517af47b9bb026770b1f198b6e921b5edf5/outcome-1.1.0-py2.py3-none-any.whl")
    version("1.0.1", sha256="ee46c5ce42780cde85d55a61819d0e6b8cb490f1dbd749ba75ff2629771dcd2d", url="https://pypi.org/packages/ff/c7/c4ac99243794a6159ae9335bb26b021e104215390e12e95e40d51007c79b/outcome-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="7357af9ba2a08fdff8c742818909c5d146fc1fe75aee4bddadaa4f8ad726d262", url="https://pypi.org/packages/b9/3e/88cf8cbc591682e4ef27f61044496ca66733210b57ce01000ffec8b29d88/outcome-1.0.0-py2.py3-none-any.whl")
    version("0.1.0", sha256="de68deb145ace3b9217a9461d6bfb4f720fdf01f77bfd65936906d8301bd08d2", url="https://pypi.org/packages/3d/d5/701ce5cccd245841557191c087bfa0a56d8b0231191f5ab7bc27f62a5876/outcome-0.1.0-py2.py3-none-any.whl")
    version("0.1.0-alpha0", sha256="a6329de82a1789015fd55d83a788bbba7b55e187eceee026ef627804795b5cc6", url="https://pypi.org/packages/8d/5b/a95966a9200f05bc97ee581006aa2083792aae9cd1f966960c43c88729fe/outcome-0.1.0a0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19.2:", when="@1.0.1:")
        depends_on("py-attrs", when="@:1.0.0")
    # END DEPENDENCIES

