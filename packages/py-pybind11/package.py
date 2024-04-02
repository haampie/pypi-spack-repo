# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybind11(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.11.1", sha256="33cdd02a6453380dd71cc70357ce388ad1ee8d32bd0e38fc22b273d050aa29b3", url="https://pypi.org/packages/06/55/9f73c32dda93fa4f539fafa268f9504e83c489f460c380371d94296126cd/pybind11-2.11.1-py3-none-any.whl")
    version("2.11.0", sha256="307443ea89b73ce88f68fa48687d160c036622a54bc2a25aae9d5ea792bef268", url="https://pypi.org/packages/6d/88/37445fde2baddf06e13753b722c4d82b60a9844784567a80a04e9b6c6c74/pybind11-2.11.0-py3-none-any.whl")
    version("2.10.4", sha256="ec9be0c45061c829648d7e8c98a7d041768b768c934acd15196e0f1943d9a818", url="https://pypi.org/packages/52/ed/68e989fdac8f352cb6d506fac111ba1e1b74c0ef3660fadeeeeb765bc03c/pybind11-2.10.4-py3-none-any.whl")
    version("2.10.1", sha256="ebf3eeac46859a2e10077ae45378ba3f33d999a9064697a3464fba1a4a04fc0a", url="https://pypi.org/packages/1d/53/e6b27f3596278f9dd1d28ef1ddb344fd0cd5db98ef2179d69a2044e11897/pybind11-2.10.1-py3-none-any.whl")
    version("2.10.0", sha256="6bbc7a2f79689307f0d8d240172851955fc214b33e4cbd7fdbc9cd7176a09260", url="https://pypi.org/packages/9a/7f/855560aa568e50bea6012ed535e6b8c436e99394f3e5a649d44d2e557242/pybind11-2.10.0-py3-none-any.whl")
    version("2.9.2", sha256="20f56674da31c96bca7569b91e60f2bd30d693f0728541412ec927574f7bc9df", url="https://pypi.org/packages/fd/24/efc9e62aa1baa48622028c59ae2c70fa134801e8acbdf30e5b594fe5a360/pybind11-2.9.2-py2.py3-none-any.whl")
    version("2.9.1", sha256="b570d17ed34b0f8ff43f5647833db87353be9afca0c7d1d69e92706b10a9c961", url="https://pypi.org/packages/11/88/98f65ae2e34cb52cda4ce16fd0839d482fbb5b690cb2f8b93d24aaa018fa/pybind11-2.9.1-py2.py3-none-any.whl")
    version("2.9.0", sha256="0c178c6e5806e8e58a7eec5a363d052bb9dac860a3ff64fbddb7226110644977", url="https://pypi.org/packages/70/1e/c7995fc7a0b0ec24bdb20b38f738e4f242250842717efa869e3fc4ce22fe/pybind11-2.9.0-py2.py3-none-any.whl")
    version("2.8.1", sha256="4ecbc2a0d4d1f3636edd8296705cc164991b704f3389ebcfa52986a0101f913b", url="https://pypi.org/packages/a8/3b/fc246e1d4c7547a7a07df830128e93c6215e9b93dcb118b2a47a70726153/pybind11-2.8.1-py2.py3-none-any.whl")
    version("2.8.0", sha256="498c5ef8eb7454011d05f91d1faccf8c3c3685992811b0ece3d6fd6141a94bd8", url="https://pypi.org/packages/6f/b5/754ce725516aa10d6bb5fd6e2c94208433a0a205c89ae105676f6c61196e/pybind11-2.8.0-py2.py3-none-any.whl")
    version("2.7.1", sha256="34663b2a16e7ac6ae8b77fef13e2b135e9fbc5ec13d2505d34bd35b3a41b9d82", url="https://pypi.org/packages/8a/98/90f6c89b799c2b18891a4286bce09b928a3a453be8b7c05d7ba45edfb722/pybind11-2.7.1-py2.py3-none-any.whl")
    version("2.7.0", sha256="71dfd6e61f6aef3e24eda3b9770a0d53072346871f9f5a0510598ec86b5f9dc2", url="https://pypi.org/packages/00/30/57fe5b30b484277a5db2d0098465e2665b171162dba7afa87a7f326647c9/pybind11-2.7.0-py2.py3-none-any.whl")
    version("2.6.2", sha256="2d8aebe1709bc367e34e3b23d8eccbf3f387ee9d5640548c6260d33b59f02405", url="https://pypi.org/packages/8d/43/7339dbabbc2793718d59703aace4166f53c29ee1c202f6ff5bf8a26c4d91/pybind11-2.6.2-py2.py3-none-any.whl")
    version("2.6.1", sha256="c3691da74b670a4850dec30c1145a0dad53a50eeca78b7e7cdc855b5c98fd32d", url="https://pypi.org/packages/00/84/fc9dc13ee536ba5e6b8fd10ce368fea5b738fe394c3b296cde7c9b144a92/pybind11-2.6.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="205d9f9615eac190811cb8c3c2b2f95f6844ddba0fa0a1d45d00793338741601", url="https://pypi.org/packages/89/e3/d576f6f02bc75bacbc3d42494e8f1d063c95617d86648dba243c2cb3963e/pybind11-2.5.0-py2.py3-none-any.whl")
    version("2.4.3", sha256="06398d054acd33d3b89d4b12000fadc36e946001438425a96c9e30048655ab96", url="https://pypi.org/packages/4b/4d/ae1c4d8e8b139afa9682054dd42df3b0e3b5c1731287933021b9fd7e9cc4/pybind11-2.4.3-py2.py3-none-any.whl")
    version("2.3.0", sha256="5531dee811310ff02ff69fe4f45feb56d845154ba692b8e4660ae2c478ee313a", url="https://pypi.org/packages/5d/85/c7a8dffda52ce25a8bcfe9a28b6861bdd52da59ae001fdd4173e054b7d9b/pybind11-2.3.0-py2.py3-none-any.whl")
    version("2.2.4", sha256="bd68159013d20c79bf79893b174a6ee7f74af740bf60ae731565f5d8d4094403", url="https://pypi.org/packages/f2/7c/e71995e59e108799800cb0fce6c4b4927914d7eada0723dd20bae3b51786/pybind11-2.2.4-py2.py3-none-any.whl")
    version("2.2.3", sha256="7f2847016313068f6fc24e8996b30345b1b8ceb74de7ea45eb2c0fa9f8fa639d", url="https://pypi.org/packages/12/90/0f92a575dc60c8fba6d0c91d6b45abdb1058da9ebed40400cbcfad2ac0a7/pybind11-2.2.3-py2.py3-none-any.whl")
    version("2.2.2", sha256="1454f0cb00552365832b1d8a95bb4c5404befd42a496d3b7515b5b47e8c16eec", url="https://pypi.org/packages/ff/3e/421f90f8d9e7fd43bd4e22781ad04d4ea3d6f4571b73c4e9dca29669a599/pybind11-2.2.2-py2.py3-none-any.whl")
    version("2.2.1", sha256="6c907b0c4faa3fd38d13c8bb765d0c9b855bcfc23898bb32847a56ccd47f1f99", url="https://pypi.org/packages/52/df/c438df9d06a43d4b90a3d0656736e34a992e6bd646a4124310aab02d3eea/pybind11-2.2.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="a0b94be592b8ee6cadf947eff6e5ddda1a9ea5cb9a9407cb57c16c111630bd34", url="https://pypi.org/packages/5a/df/4d1d08b4b84446e95ae994e65b12f30971c1015163018eb41c20810c6fa6/pybind11-2.2.0-py2.py3-none-any.whl")
    version("2.1.1", sha256="46296035478dd331c4b9f2809a71b8b02c6d473129b7819978badd628f2f93d2", url="https://pypi.org/packages/5d/f4/ebdd28792c8ceb852428b7edf983375cee4cfdae75d6791dcb1b1d43bf7c/pybind11-2.1.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="a886cc3427749a7a023821f1bd1bfa4d862ec4326cf3700c6d86b9c3bb01df1e", url="https://pypi.org/packages/ab/50/3fecb101c9cde13bb842c53c7bb8a8b22ae54a47ac12d02cc16ad4c8a1d6/pybind11-2.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("build_type", default=False, description="build_type")
    variant("generator", default=False, description="generator")
    variant("ipo", default=False, description="ipo")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

