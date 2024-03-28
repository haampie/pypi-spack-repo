# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFtfy(PythonPackage):
    # BEGIN VERSIONS
    version("6.2.0", sha256="f94a2c34b76e07475720e3096f5ca80911d152406fbde66fdb45c4d0c9150026", url="https://pypi.org/packages/f4/f0/21efef51304172736b823689aaf82f33dbc64f54e9b046b75f5212d5cee7/ftfy-6.2.0-py3-none-any.whl")
    version("6.1.3", sha256="e49c306c06a97f4986faa7a8740cfe3c13f3106e85bcec73eb629817e671557c", url="https://pypi.org/packages/91/f8/dfa32d06cfcbdb76bc46e0f5d69c537de33f4cedb1a15cd4746ab45a6a26/ftfy-6.1.3-py3-none-any.whl")
    version("6.1.1", sha256="0ffd33fce16b54cccaec78d6ec73d95ad370e5df5a25255c8966a6147bd667ca", url="https://pypi.org/packages/e1/1e/bf736f9576a8979752b826b75cbd83663ff86634ea3055a766e2d8ad3ee5/ftfy-6.1.1-py3-none-any.whl")
    version("6.1.0.post1", sha256="7380481b59898382941a67e1c236e3ca7b76091f860975cd69d2552d48b95c1a", url="https://pypi.org/packages/b8/5e/5a93192eba099c6c6b59826100f164d34b6b8857a031d477c05664aa306b/ftfy-6.1.0.post1-py3-none-any.whl")
    version("6.1.0", sha256="56fa8daff1a678b689fe8fa3defbf7ece13fabfce82e3f67d8088320bbae1106", url="https://pypi.org/packages/37/4a/3777ca06a7acb52289655bc1619ba7a5b94fec72a9877b9d1130b5c7458b/ftfy-6.1.0-py3-none-any.whl")
    version("6.0.3", sha256="ba71121a9c8d7790d3e833c6c1021143f3e5c4118293ec3afb5d43ed9ca8e72b", url="https://pypi.org/packages/af/da/d215a091986e5f01b80f5145cff6f22e2dc57c6b048aab2e882a07018473/ftfy-6.0.3.tar.gz")
    version("6.0.1", sha256="9eb68533eb2a6124e96ed7f63049e6c519194fda3fae92629b5e0b5753cb2c8f", url="https://pypi.org/packages/ce/b5/5da463f9c7823e0e575e9908d004e2af4b36efa8d02d3d6dad57094fcb11/ftfy-6.0.1.tar.gz")
    version("6.0", sha256="4d7445f7c05d4ad3751147094da400dcf1f7a9c93844f5ed168bbcf17e4598ca", url="https://pypi.org/packages/78/50/ba5ec9ff8b56e09c0aa8e13d2cc6e24b31bdd23e2bab8f510929bcc4ac48/ftfy-6.0.tar.gz")
    version("5.9", sha256="8c4fb2863c0b82eae2ab3cf353d9ade268dfbde863d322f78d6a9fd5cefb31e9", url="https://pypi.org/packages/04/06/e5c80e2e0f979628d47345efba51f7ba386fe95963b11c594209085f5a9b/ftfy-5.9.tar.gz")
    version("5.8", sha256="51c7767f8c4b47d291fcef30b9625fb5341c06a31e6a3b627039c706c42f3720", url="https://pypi.org/packages/ff/e2/3b51c53dffb1e52d9210ebc01f1fb9f2f6eba9b3201fa971fd3946643c71/ftfy-5.8.tar.gz")
    version("4.4.3", sha256="3c0066db64a98436e751e56414f03f1cdea54f29364c0632c141c36cca6a5d94", url="https://pypi.org/packages/21/5d/9385540977b00df1f3a0c0f07b7e6c15b5e7a3109d7f6ae78a0a764dab22/ftfy-4.4.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-wcwidth@0.2.12:", when="@6.1.3:")
        depends_on("py-wcwidth@0.2.5:", when="@6.1:6.1.1")
    # END DEPENDENCIES

