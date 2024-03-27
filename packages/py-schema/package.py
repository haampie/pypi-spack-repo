##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySchema(PythonPackage):
    version("0.7.5", sha256="f3ffdeeada09ec34bf40d7d79996d9f7175db93b7a5065de0faa7f41083c1e6c", url="https://pypi.org/packages/0d/93/ca8aa5a772efd69043d0a745172d92bee027caa7565c7f774a2f44b91207/schema-0.7.5-py2.py3-none-any.whl")
    version("0.7.4", sha256="fbb6a52eb2d9facf292f233adcc6008cffd94343c63ccac9a1cb1f3e6de1db17", url="https://pypi.org/packages/2b/91/42bc143289fd5f032ab1b01c5da32dc162ae808a585122f27ed5bf67268f/schema-0.7.4.tar.gz")
    version("0.7.3", sha256="c331438b60f634cab5664ab720d3083cc444f924d55269530c36b33e3354276f", url="https://pypi.org/packages/57/ac/cb6fd3fb0c443aeb55e5d8cace0bd2922e798a0fab29386f02c396b9d877/schema-0.7.3-py2.py3-none-any.whl")
    version("0.7.2", sha256="3a03c2e2b22e6a331ae73750ab1da46916da6ca861b16e6f073ac1d1eba43b71", url="https://pypi.org/packages/6d/ae/835f2e0d304c9533c58fe5cbcdd9124708d32e82289fcb8d6084c908ba29/schema-0.7.2-py2.py3-none-any.whl")
    version("0.7.1", sha256="10b550886f5ff402e1fdef85bd7be761b0e09a35a43633311807a57a5bc4db50", url="https://pypi.org/packages/45/ae/a7e3cc8b885e681cbfee89d8d43dbc0168dbd033e2b2745eda6223477467/schema-0.7.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="5b0e0f47923164190513db2e91b9ab1941162b2dc400cc9b1803c2abab579e62", url="https://pypi.org/packages/74/f5/a14c01bcc9dbf99fd164fe2c55229569456f991a162daf62d3275714d241/schema-0.7.0-py2.py3-none-any.whl")
    version("0.6.8", sha256="d994b0dc4966000037b26898df638e3e2a694cc73636cb2050e652614a350687", url="https://pypi.org/packages/7b/6e/2b6b764a9a3d3aa366a857f4c5f34d27de4fca54c2b9b88f93ccf2821353/schema-0.6.8-py2.py3-none-any.whl")
    version("0.6.7", sha256="a058daf5d926e4ece9f13c4c2366a836143ca7913ef053c5023c569e00175b2a", url="https://pypi.org/packages/5d/42/32c059aa876eb16521a292e634d18f25408b2441862ff823f59af273d720/schema-0.6.7-py2.py3-none-any.whl")
    version("0.6.6", sha256="0e1b5453ea462a10744c612bc8989e2a058609beac7deba9edbac8c5b1a2e2b0", url="https://pypi.org/packages/7b/46/657c4b2a4dbfd353df49cf39edf5955cd10a63a5111751e7e80d2676398d/schema-0.6.6-py2.py3-none-any.whl")
    version("0.6.5", sha256="d9c2a189e541c26ebd846156110fd6a14827efd0e4710f33a8ab2ef0f05f0d63", url="https://pypi.org/packages/af/be/3e2d5254cabb0bd1e18f7c16babd38363acc96d4d704120e247f1614ceca/schema-0.6.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-contextlib2@0.5.5:", when="@0.7.2:0.7.3,0.7.5:")
        depends_on("py-contextlib2@0.5.5:0.5", when="@0.7:0.7.1")

