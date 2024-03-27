##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaracoTiming(PythonPackage):
    version("2.0", sha256="debf23993f2983a4cfda22da65ef612f0a3d5b19ff1e5c6e7ec368eaa8e49745", url="https://pypi.org/packages/36/38/f4aa8b81780004e3131240d090f2422e46d31975de9a9688856a4303a5c1/jaraco.timing-2.0-py2.py3-none-any.whl")
    version("1.3.2", sha256="e595a7700c8988a42909a35dfa5f87951c5abdeb75e6909003d47ad6e1d2e257", url="https://pypi.org/packages/36/6f/7840605160cdc928504495396c848f3d313056366f83e0e7a10e6a87a016/jaraco.timing-1.3.2-py2.py3-none-any.whl")
    version("1.3.1", sha256="ec35e6aaccbe5c40a5f6358ba970c7fe56fac60e7fb62a47f5041527d62fdd09", url="https://pypi.org/packages/12/26/929634429530ad709091249579a08dc6717555b7a3ef2fd7ab08ed995a7d/jaraco.timing-1.3.1-py2.py3-none-any.whl")
    version("1.3", sha256="b65de2845763d95fe016492209a9dc4a18651244c662f3f5c1c27d68f252607e", url="https://pypi.org/packages/26/36/44cf01983bb1b55bab41323668413ab3ad73cf17c010c1be6ca70e608ec8/jaraco.timing-1.3-py2.py3-none-any.whl")
    version("1.2.2", sha256="e1b7482bb98bc569503802e1caf100782090020c5978a856364f1a191c4173aa", url="https://pypi.org/packages/2c/0f/fabea092a0e715dd3815d495672fde5b055e82f1db9262dbb9b503f3fd6f/jaraco.timing-1.2.2.tar.gz")
    version("1.2.1", sha256="1b4d13ab4c8b5c1b3889fa0f1ba1253ce1dc72a12913b669a2e74d7d51d32db7", url="https://pypi.org/packages/98/f9/4090ea9c22b655e7f2bf61e6a370ed99db9508f599a406441b21cef97582/jaraco.timing-1.2.1.tar.gz")
    version("1.2", sha256="3351831de02228f2fb66c702357796368d8e8c677d43ba49d1e7758143a50bb5", url="https://pypi.org/packages/b8/70/e0b56a45acc63bb2359cb2b02c4bf222a982caa02c459b655cadb8fe0451/jaraco.timing-1.2.tar.gz")
    version("1.1.5", sha256="700edf62af810f025a5a8331ac6005913d16fdd34678afc1006a966288043ae2", url="https://pypi.org/packages/4a/4f/3515b0a74aa6914fa1051b78fe520ab9417e7d567c90e94a18048ce03eb2/jaraco.timing-1.1.5.tar.gz")
    version("1.1.3", sha256="302083998d2dab46abf7ad6e623620241ae5d221db3ca4ab30660aace761b5c7", url="https://pypi.org/packages/8c/fe/c037fe6287605a6639fd1dba37e371a033af674b54c2861369bd2ea6ec6d/jaraco.timing-1.1.3.zip")
    version("1.1.2", sha256="e5b3e2e47d9941e74b4098e1fa9638edc6173882eb062da14a781854827f93d1", url="https://pypi.org/packages/a3/a4/bf61307a59ee9aae126ab096d0a43422203071aa6e4d9bccd26f227a2be9/jaraco.timing-1.1.2.zip")

    with default_args(type="run"):
        depends_on("py-tempora@1.5:", when="@1.3:")

