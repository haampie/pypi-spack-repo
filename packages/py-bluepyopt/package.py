##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBluepyopt(PythonPackage):
    version("1.14.10", sha256="911277935d102ea24254747ef13d8e831eabe6bcdea8e6ad1d25f93fc6fe2255", url="https://pypi.org/packages/a7/0f/970455244ced0df79c3a64aea32a131c958fc555e61d3cf0b9d6c318ff94/bluepyopt-1.14.10-py3-none-any.whl")
    version("1.14.9", sha256="00fe48939abd6ab8479382ec708f645304fd050135f69bc4bb00e89e704b1c3a", url="https://pypi.org/packages/82/88/48d5dd3fc3fe5b8ee0752a9adff1b08ad5d37877a5fd48a53eab088057b9/bluepyopt-1.14.9-py3-none-any.whl")
    version("1.14.8", sha256="4cde42455670b040d1c18653a3be355b1e6c2c91d527ace6f2cd6608643fca53", url="https://pypi.org/packages/67/89/7666e9afe68c2cb8520c9b32633aae37ec4c1516376c3780476a58c3b77d/bluepyopt-1.14.8-py3-none-any.whl")
    version("1.14.7", sha256="ebbeb23fba66e7e089f8d102045778e9a707807c77c263e840c5f5d7bc8e7f61", url="https://pypi.org/packages/bb/a0/828be312d34120bff20ad46390a91c172ccc22197092dbf252c5fa369d1d/bluepyopt-1.14.7-py3-none-any.whl")
    version("1.14.6", sha256="4f431d0da4a00d8abc4f87482ef0f2e2bdc9b5c1d15a3b6eb3ede6a83101ccd6", url="https://pypi.org/packages/60/e6/a3656802ad4fd08e3dc4be4c984bdc141574b34bcb4999d83d3716dc8e7b/bluepyopt-1.14.6-py3-none-any.whl")
    version("1.14.5", sha256="1efee9f7c826a006c5ab173295c08a0784dbb3eeebf36d4c9dd1f28b482b7643", url="https://pypi.org/packages/b0/a4/cd94dadb4825e911a3f2801e6d842753592763e6692ad259362c9ecc340d/bluepyopt-1.14.5-py3-none-any.whl")
    version("1.14.4", sha256="11de74999036d3d6dd8a003dd0eb073c6325f7feb8c0a38c5f19267275ff424c", url="https://pypi.org/packages/5e/45/3494c5c3f9abd414b66f3b4ef93545464b22bbf8c3e81c2896ef5e6899dc/bluepyopt-1.14.4-py3-none-any.whl")
    version("1.14.3", sha256="fb45d179ac6f852e3180d0f0dff4c18aa4b3d60e3c898f0fb4c061461bdfc36f", url="https://pypi.org/packages/26/83/0d2867e904829b5bde4b0f35adcfc7eb956dcd12300928400bc5674e840a/bluepyopt-1.14.3-py3-none-any.whl")
    version("1.14.2", sha256="93da0cdb78a8eec074248235817c87e172cae3468feb872b25388b509ec9c391", url="https://pypi.org/packages/af/42/fefb1a450232b382b2658dd0945d76e72079c0f2923c07e9446c9db972e8/bluepyopt-1.14.2-py3-none-any.whl")
    version("1.14.1", sha256="45a4f657666d90b0ed2c743cca1dc7be5eb9e369b76ef1c126b87f076ec41978", url="https://pypi.org/packages/08/a1/5ac391f7b6385cc0dc008721ce179874eb7fd60ee0572b5007206a50542e/bluepyopt-1.14.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-deap@1.3.3:", when="@:0.0,1.12.63:")
        depends_on("py-efel@2.13:", when="@:0.0,1.12.7:")
        depends_on("py-future", when="@:0.0,1.12.7:1.14.4")
        depends_on("py-ipyparallel", when="@:0.0,1.12.7:")
        depends_on("py-jinja2@2.8:", when="@:0.0,1.12.7:")
        depends_on("py-neuron@7.8:", when="@1.14.6:")
        depends_on("py-numpy@1.6:", when="@:0.0,1.12.7:")
        depends_on("py-pandas@0.18:", when="@:0.0,1.12.7:")
        depends_on("py-pebble@4.6:", when="@1.14.1:")
        depends_on("py-pickleshare@0.7.3:", when="@:0.0,1.12.7:")

