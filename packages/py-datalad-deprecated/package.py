##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDataladDeprecated(PythonPackage):
    version("0.3.0", sha256="4c95890996ee50aa67b813fc7bf47f4e07ac25eb8148932c0aac3bc838567b71", url="https://pypi.org/packages/94/dc/280c34ac6efc0099c787a80067605cebdbbae572db9d3e0180fa8b632450/datalad_deprecated-0.3.0-py3-none-any.whl")
    version("0.2.8", sha256="590ce559d736e8355858ee856da35ce3b77b2e5d37d8e3c61a42d2be87cc6a9c", url="https://pypi.org/packages/2c/d5/dd5dc1a76894824935976ae1af69ea3d9f7bd93779f441a4725a859e17af/datalad_deprecated-0.2.8-py3-none-any.whl")
    version("0.2.7", sha256="1af2739aa2d593b5c510e4113b3edf5b3f4428255bd9df1b2d076b35ecf1629a", url="https://pypi.org/packages/07/af/c70306b22952af37abf8ba496768d86a1365d413dd3772b24a2ff7d52968/datalad_deprecated-0.2.7-py3-none-any.whl")
    version("0.2.6", sha256="57bc4c730b3be858c88e3615588fb5a97e9ee46ee375b9e83ec77dadb69d266b", url="https://pypi.org/packages/e1/91/dcf53330ac2f65853d67355eb0976569384b0faa6cc1a254ff29bcf181d3/datalad_deprecated-0.2.6-py3-none-any.whl")
    version("0.2.5", sha256="6d88f1219837514aaa0bc5fc3190e43c21db3e6ca0db188513bcdb3e6021d0fa", url="https://pypi.org/packages/2a/da/cc7e1fbb66c664604278cc60275a1d6c831264b756eee2f624f88275459f/datalad_deprecated-0.2.5-py3-none-any.whl")
    version("0.2.4", sha256="44778a614e9d004013fd6afa1f3fdb35c0329670a551cdb81849ad848e0a7884", url="https://pypi.org/packages/fc/c1/1cb563e46964f89970f0506cbb106331d6408065597f10e8186b6e52d2c9/datalad_deprecated-0.2.4-py3-none-any.whl")
    version("0.2.3", sha256="950fc56334c348d530422f0534a94cf5c37d9ef541e586261331e983f5ea23d9", url="https://pypi.org/packages/92/29/efac257fe1c010a4558d80f3f3b5659d2341b8e2791b70f0906d0606b331/datalad_deprecated-0.2.3-py3-none-any.whl")
    version("0.2.2", sha256="fc7f6135fc39164ca7b91560f1e4524627e8cb7cd94775e8405fb27e2906ad13", url="https://pypi.org/packages/4e/7c/96214934bb94d41b02d2863dd8ddac8494d9a79f9eee68853987811ad773/datalad_deprecated-0.2.2-py3-none-any.whl")
    version("0.1", sha256="316293313b85f6bd729b74348110d1605f6ec25a07af4bd1c52dfbda8d67a779", url="https://pypi.org/packages/f7/9e/e96c74eded6c46ac54f84e8055ce391afae45020a0601f39779ee8415496/datalad_deprecated-0.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-datalad@0.18:", when="@0.3:")
        depends_on("py-datalad@0.15:", when="@0.2.3:0.2")
        depends_on("py-datalad@0.12.0:", when="@:0.2.2")
        depends_on("py-exifread", when="@0.2.3:")
        depends_on("py-jsmin")
        depends_on("py-mutagen@1.36:", when="@0.2.3:")
        depends_on("py-pillow", when="@0.2.3:")
        depends_on("py-python-xmp-toolkit", when="@0.2.3:")
        depends_on("py-pyyaml", when="@0.2.3:")
        depends_on("py-whoosh", when="@0.2.3:")

