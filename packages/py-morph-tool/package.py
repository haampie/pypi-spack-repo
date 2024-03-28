# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMorphTool(PythonPackage):
    # BEGIN VERSIONS
    version("2.10.2", sha256="e153c0af49de5569acd77b8db175537aeab09695348cbeef391da04a5b46d0f4", url="https://pypi.org/packages/1c/36/ded6cc552bd9a2c01d26502d20b3bf9fa36351ba7c870df84c769bf7a48d/morph-tool-2.10.2.tar.gz")
    version("2.10.1", sha256="74f1a267235e546cfd106c78687887920f2ed585fdc098165599285221f1307f", url="https://pypi.org/packages/75/59/ef317cf60e74f3981a9f0a8a822983adf7cb5b12f266788745e8e91e0917/morph-tool-2.10.1.tar.gz")
    version("2.10.0", sha256="9edb1b27cccd525a93dae77afcb0fd03cfe562a085f2f69207b959f9d1f06632", url="https://pypi.org/packages/97/18/07f2245925fee985d2b4d731a374b5ebff0c7c4115be5013f4c69e4cae82/morph-tool-2.10.0.tar.gz")
    version("2.9.1", sha256="305e9456c8047726588b23dfa070eb95ccbe5573e9fea3e0a83dc93eacdf61dc", url="https://pypi.org/packages/58/54/46395b70637868ca3a233abfcc517517b81bce814aed222e362c1ac93571/morph-tool-2.9.1.tar.gz")
    version("2.9.0", sha256="c60d4010e17ddcc3f53c864c374fffee05713c8f8fd2ba4eed7706041ce1fa47", url="https://pypi.org/packages/0b/5d/d0b3c6e3928a1ac9ea208c9273b56eab850c67ad65024ea4faf1be7abd5a/morph-tool-2.9.0.tar.gz")
    version("2.8.0", sha256="3676d200e30313afee60ba7e232edb76ffa2f3926211eb251df63ffedae96a57", url="https://pypi.org/packages/f5/82/3db384ef6e03f827c1e61c672f18632418c5fc4c66be6ad825e6c9eb9e6a/morph-tool-2.8.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("nrn", default=False)
    variant("parallel", default=False)
    variant("plot", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

