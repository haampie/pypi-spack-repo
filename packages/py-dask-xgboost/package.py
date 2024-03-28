# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDaskXgboost(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="47b7d96e981d8d7aa81bd15578f470d80ee92ae5aac122adc3bc7e1c9f941682", url="https://pypi.org/packages/0d/33/90fec71df94921d9e604c1f3812b7bb9573ce93aec0637df8a319a7ea42b/dask_xgboost-0.2.0-py2.py3-none-any.whl")
    version("0.1.11", sha256="903609b5ace44c25f021cae53964ce913eec34e73c449dca64755dae5a26efd9", url="https://pypi.org/packages/38/cd/7ee92d372176068f7f445f062e1748d0d75491e5d14902bbe48da78df636/dask_xgboost-0.1.11-py2.py3-none-any.whl")
    version("0.1.10", sha256="9d7ef5e1708f76a5d4e7279b91a4b76e41d541171cdb25addc6fbdaad79fdf82", url="https://pypi.org/packages/c5/8f/ad8cfa16b37d7aa8cc48b89d33a8d77d85d59488a69771cb1d0cd4bca8ce/dask_xgboost-0.1.10-py2.py3-none-any.whl")
    version("0.1.9", sha256="63db4a006a155c80b06d3c1a5bb7cc7dd249e9bba8cd2373e84a4c85ad82ca93", url="https://pypi.org/packages/1c/bd/d69f0546e7652daa7717aa44ef5346e023e7dd6cc6a50e397872dee27add/dask_xgboost-0.1.9-py2.py3-none-any.whl")
    version("0.1.7", sha256="8b122c15d3180dd318afe4ddf0862d93add71c34c12ad87853c87f92067e990d", url="https://pypi.org/packages/9f/0a/717a74df509093abffca80bdae0b1f23c8728172598ea406d54a2667aaea/dask_xgboost-0.1.7-py2.py3-none-any.whl")
    version("0.1.5", sha256="bea11a461790d4153918486c53bc020a3aeacfc7c9ed920a3ea563bf5775ffd7", url="https://pypi.org/packages/ca/e2/2aca20f6d99cafb6e614b73ff685eedf91cbebf3e557806f78a1188a1e28/dask_xgboost-0.1.5-py2.py3-none-any.whl")
    version("0.1.3", sha256="315d774179ad82be301b9d87e119757d1c937f046fe9340b32ad7dc08545be20", url="https://pypi.org/packages/71/62/1374455839b504fa67ec837d074b6a9210cf60934b2c17402b288f4daf20/dask_xgboost-0.1.3-py2.py3-none-any.whl")
    version("0.1.2", sha256="f5f69a6d0ba8ec2c116e09e785b618d5e71757c5801c8f1e8783149dea22071b", url="https://pypi.org/packages/5a/58/5259a559ec776ce69cb7b4d95dca3c0af5a1d0931f3eab6f142d995e0b33/dask_xgboost-0.1.2-py2.py3-none-any.whl")
    version("0.1.0", sha256="2b381395fd1dff1ee144f3340b85cbe559df3e641fb5c2ebd20ceb1944cf21b9", url="https://pypi.org/packages/33/d3/ba9dcfacb52f7059268797c689845a3e9cd663d049ffc897893ed1bdcd11/dask_xgboost-0.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dask", when="@:0.1.3,0.1.7:")
        depends_on("py-distributed@1.15.2:", when="@:0.1.3,0.1.7:")
        depends_on("py-xgboost@:0", when="@0.1.11:")
        depends_on("py-xgboost", when="@:0.1.3,0.1.7:0.1.10")
    # END DEPENDENCIES

