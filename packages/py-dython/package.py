# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDython(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.4", sha256="3ae49dc2c654decc55166fe0210f494903a7cd61cd99637f43ab16643d946753", url="https://pypi.org/packages/16/65/7e2ba587f7854ce45ac5a69348fdfb1872fd39c138dc5ebf45934beda65b/dython-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="dfd81ffdc9bd4268ed1e212eaf552b46b1a1a7dc02350bce7d1cdc7e7232ac7a", url="https://pypi.org/packages/2e/6a/b9ff600c9efc076542cf2a62295d0290253f0d66742de2696fe06e0efb27/dython-0.7.3-py3-none-any.whl")
    version("0.7.2", sha256="6d7579358aa047f4c706ce0c09007ceeb3102b1efa3571b51a9b0c08a2711456", url="https://pypi.org/packages/35/5c/72694034f02fd3ec58cb344682c863d8bac726302cc3b59493f2018a95d2/dython-0.7.2-py3-none-any.whl")
    version("0.7.1.post4", sha256="6938864891583eb72a788902b39ec6366ce73aacc103c4666e16607e4f3c827e", url="https://pypi.org/packages/12/16/395de7fba8a833aaf6917ac4926e8d1d2972b3e9110249640f6e4991b090/dython-0.7.1.post4-py3-none-any.whl")
    version("0.7.1.post3", sha256="49be283a641b601a27b18db3256f554ab2148678f4a2ccd1145385ad9252ec24", url="https://pypi.org/packages/0e/17/e0aec9dd7ab240e7eb295f58456d6f474ad5146b381b270832aaba3adc58/dython-0.7.1.post3-py3-none-any.whl")
    version("0.7.1.post2", sha256="fc9c3347a527e43cc52b622ca6169a554cd6d74caef4701a0757a7c75b8c8db6", url="https://pypi.org/packages/6d/f4/041798bde39732a86dc3ded435cf8ff60823886f6dd026de6acfe8b59906/dython-0.7.1.post2-py3-none-any.whl")
    version("0.7.1.post1", sha256="d126ef753e1b77c59de6fd7ebd3c31c9bf31d41e3850ca53f645cd91dadf2961", url="https://pypi.org/packages/fc/71/d3c71308ad573cd19228dc1394b768d30b23b39ba61880568ae621bd1bff/dython-0.7.1.post1-py3-none-any.whl")
    version("0.7.1", sha256="ae2c66309e82b9a214279d2e93071b46f7e141c78602b404deb829eb5f287615", url="https://pypi.org/packages/2d/a8/3da2d77ee25a5d89d2969d8adc9975654658d4fb5c8144e06cb95ffd5a75/dython-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="f637cbb777e832bb6558dabc38bc52698dd85c6824e6caa241ceca31a639d324", url="https://pypi.org/packages/63/64/e491b1f5765763153fdd0af54c2f7cff1ce39483f6ca98c20a602a3bc71c/dython-0.7.0-py3-none-any.whl")
    version("0.6.8", sha256="27d0a54e105fb2daff38ee70c8d50971e07f856be2d1b9456c3137b4c826a0a9", url="https://pypi.org/packages/93/47/d5e88dafdd077f42f93bd12cc57753c5b6a41847efe358171c0c20f429b2/dython-0.6.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib@3.5.3:", when="@0.7.3:0.7.4")
        depends_on("py-matplotlib@3.4.3:", when="@0.7:0.7.2")
        depends_on("py-matplotlib", when="@:0.6")
        depends_on("py-numpy@1.23.0:", when="@0.7.3:")
        depends_on("py-numpy@1.19.5:", when="@0.7:0.7.2")
        depends_on("py-numpy", when="@:0.6")
        depends_on("py-pandas@1.4.2:", when="@0.7.3:")
        depends_on("py-pandas@1.3.2:", when="@0.7:0.7.2")
        depends_on("py-pandas@0.23.4:", when="@0.5.2:0.6")
        depends_on("py-psutil@5.9.1:", when="@0.7.2:")
        depends_on("py-scikit-learn@0.24.2:", when="@0.7:")
        depends_on("py-scikit-learn", when="@:0.6")
        depends_on("py-scikit-plot@0.3.7:", when="@0.6.5:0.7.4")
        depends_on("py-scipy@1.7.1:", when="@0.7:")
        depends_on("py-scipy", when="@:0.6")
        depends_on("py-seaborn@0.12.0:", when="@0.7.3:")
        depends_on("py-seaborn@0.11.0:", when="@0.7:0.7.2")
        depends_on("py-seaborn", when="@:0.6")
    # END DEPENDENCIES

