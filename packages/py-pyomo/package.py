# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyomo(PythonPackage):
    # BEGIN VERSIONS
    version("6.7.1", sha256="735b66c45937f1caa43f073d8218a4918b6de658914a699397d38d5b8c219a40", url="https://pypi.org/packages/24/12/e8fe851bdaecfd99f7a9054cda020a4d3984318559ba2fa193cc526a238f/Pyomo-6.7.1.tar.gz")
    version("6.7.0", sha256="a245ec609ef2fd907269f0b8e0923f74d5bf868b2ec0e62bf2a30b3f253bd17b", url="https://pypi.org/packages/43/46/80bf188f20812381b29d95f3123ced89be68955c821b8d229af0a0439e79/Pyomo-6.7.0.tar.gz")
    version("6.6.2", sha256="c8ad55213ff8b1a2c4e469110db8079722d5a6f364c6c46a42e2f750fc9e4d26", url="https://pypi.org/packages/9b/73/0c11bb78ef7db2bf04424a4a7511c1f0a63777d7120f98a6f1d9e59e9dc7/Pyomo-6.6.2.tar.gz")
    version("6.6.1", sha256="3fb0aba7b0f4120e6ce0f242502c0e61478d61e326bc90b7dc392bbefd114b34", url="https://pypi.org/packages/ef/70/ea738ea23c23399e5e04f184bf78fb181e91284369b4fb3ce74b107edcea/Pyomo-6.6.1.tar.gz")
    version("6.6.0", sha256="8766c08041b8d91fbc5166d220c9e723fed6057d18be1178bae3b6583376c65e", url="https://pypi.org/packages/57/33/b61a59ef3c48b5e2878af072b030fa3cf6bc05d07c17d2361b295bd0853a/Pyomo-6.6.0.tar.gz")
    version("6.5.0", sha256="5a23e775bba9fdbad22698fa1a841e662482edc979f2dea41cc6c54b1bb4b968", url="https://pypi.org/packages/f6/e1/4245e936293827a8491cc6c80a89537946e69738fd83053f7ae2928ada7d/Pyomo-6.5.0.tar.gz")
    version("6.4.4", sha256="922dd8e6e3e421550acf884bd27f74cab2fe6552cdde36715d116b0c8345c367", url="https://pypi.org/packages/f0/dd/9d2143b0ec2f7eb4bd7e84a4367c1667f765de8e8be03f128753158c7149/Pyomo-6.4.4.tar.gz")
    version("6.4.3", sha256="7f3f67f61a6e5c2dd9c4dd930356d3176bad1572f1abee780592e725d6445288", url="https://pypi.org/packages/65/c8/971ade593e5eeb0d920932512926b885ab457caa549d6dd355f0571b0867/Pyomo-6.4.3.tar.gz")
    version("6.4.2", sha256="6f5a867e77bdd6ac2ba0da5d4a251e38543ae05eba5a0c5cf8ab39e7fa8e1ea9", url="https://pypi.org/packages/57/5c/2a35e0a1c748be041f82669687d47bbb290370862026732bf1416a670772/Pyomo-6.4.2.tar.gz")
    version("6.4.1", sha256="a636a3a1c8314b8be85899cb6fac5d6a9a78fc75c6d58b74d3ec106ae5ed8f59", url="https://pypi.org/packages/57/e1/0314a85b62538a78bbad3ba68807fc015f1d42ad0732af434dc6b87621ca/Pyomo-6.4.1.tar.gz")
    version("6.4.0", sha256="b548825301b6bd4073a0620a8265d956153d53c12fca37cc7184fa54fce96222", url="https://pypi.org/packages/ed/08/ea0a30fe5376761ef7e846d57b95bc19426b5d0c345b6bf65b8b457c0852/Pyomo-6.4.0.tar.gz")
    version("6.3.0", sha256="b4df6305438a2b6ec75bd2e1588b919feb97089ed179a944b334432723781f81", url="https://pypi.org/packages/91/aa/e68aac982bf62904a6ff8262e9921933d409b64395b10f0de0a4b4f9021a/Pyomo-6.3.0.tar.gz")
    version("6.2", sha256="89bc69a9a0afe10f5d229abe508b04ebbd3d2e213aa6c8ec2db2562798fa0400", url="https://pypi.org/packages/00/48/3253d0e353ce6e3e8b3fc39205d6eb60c7adcb18a607739f03275e517b9b/Pyomo-6.2.tar.gz")
    version("6.1.2", sha256="f2a58977c3c72e706aef7ab7d016bdf66df85df8ea5b25cc0ba387e2cef880bb", url="https://pypi.org/packages/98/2b/8d63b5f16faa4a58ce54ca38d3cc167f1db4e39de76e50fa25a1e16e9e52/Pyomo-6.1.2.tar.gz")
    version("6.1.1", sha256="32f378fda748ff299b4492b12b04ed1d8b11c857117fa0e5e6b609aa322fcade", url="https://pypi.org/packages/9c/a0/428080199113d41229feb20c45b5fe9a77bb4a034d70f62ab9389fa6d1c3/Pyomo-6.1.1.tar.gz")
    version("6.1", sha256="7d087b186a43b2ffd032bc4db87cdbcf2fdc187607211f3e6cdc0f54b6f516f4", url="https://pypi.org/packages/50/7a/b92bcf1195799281004be6fa294b57fd829cd20010cfb0364580f69915b6/Pyomo-6.1.tar.gz")
    version("6.0.1", sha256="4b27bc917b12a6011e7eb3442a54619f0f42f1087d4defa14b903dd985fdbe7c", url="https://pypi.org/packages/60/f4/6379800a79088d814934870783bf2284028145e16f68149a1c64cbdfb0f7/Pyomo-6.0.1.tar.gz")
    version("6.0", sha256="3dbfb1c7a8ef76dfd99d82c211845cdba9bf31a179269b57b6b28ad635ae34f9", url="https://pypi.org/packages/86/cd/f79c09cc84dabf8a809f0ad76d6ba09ddc8ba745e7a6cb0b48efaed0f810/Pyomo-6.0.tar.gz")
    version("5.7.3", sha256="2c4697107477a1b9cc9dad534d8f9c2dc6ee397c47ad44113e257732b83cfc8f", url="https://pypi.org/packages/4f/49/0db54700062f288c1ee7ff1d273ef7ab391fdcea2c77c01b07f8d09d7244/Pyomo-5.7.3.tar.gz")
    version("5.7.2", sha256="f10ada18ade84b16225dc519ef1788dd6d5f22cb22d0ea44db64c96d14cb7bb0", url="https://pypi.org/packages/b0/e2/4376eb79e00e1ccfeaf9e8105cacf1f16df47d098e8d3293637d3e34cd2f/Pyomo-5.7.2.tar.gz")
    version("5.7.1", sha256="1228204d7eb4cdd217fed6323a7434de68e89a2aaa74085ea47f1b42fb64d8cd", url="https://pypi.org/packages/2a/63/8346a9a444835ba6ba3deffbb626f1f513085f9f3db4ce01d2106db669fa/Pyomo-5.7.1.tar.gz")
    version("5.7", sha256="27e3a3c8411de9bc52e5e6aa88e9a0de0dd7369126bc905996e23057775905d7", url="https://pypi.org/packages/ef/92/cfeec79a5949d4b16e3789015e1adea9c35d0ab7711a8994255e0f5dba8f/Pyomo-5.7.tar.gz")
    version("5.6.9", sha256="ad7c41ce82d55a7a1d093413b7df758599163e883f658c89c5946488350e146c", url="https://pypi.org/packages/17/12/a6270a9153d767787ccde6f3166cab01ea99c6c7dd60ee261d8925402f85/Pyomo-5.6.9-py2.py3-none-any.whl")
    version("5.6.8", sha256="cba1c1598f07c6ed0755df7db61d09a46065d576419c0f1863d60d17f690515a", url="https://pypi.org/packages/af/27/e42538d57971eac8b5f7bc994db13231037169143fe0e5efeedc26f13f30/Pyomo-5.6.8-py3-none-any.whl")
    version("5.6.7", sha256="1337cf686ee7f3d1203c7f109f11d7ad0ba470efafd7013e62375c2c8a401a19", url="https://pypi.org/packages/39/77/0d57b41656d786e456f94764daeae96cdcdac41b4d8ef38d0f433d8580aa/Pyomo-5.6.7-py3-none-any.whl")
    version("5.6.6", sha256="55aa16663c662adf9ab0b935fca8d71d0b6bc2139a0a51c3c27d338c9f76a53b", url="https://pypi.org/packages/3a/13/a6e4e1b4aa9c0d49feb9c4a13ccefbc7f5249fd145bc94932eac566d05a3/Pyomo-5.6.6-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cython", default=False)
    variant("docs", default=False)
    variant("optional", default=False)
    variant("tests", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.9", when="@6.2")
        depends_on("py-appdirs", when="@5.5.1:5.7.0")
        depends_on("py-ply", when="@5.5.1:5.7.0")
        depends_on("py-pyutilib@6:", when="@5.7:5.7.0")
        depends_on("py-pyutilib@5.8:", when="@5.6.9:5.6")
        depends_on("py-pyutilib@5.7.3:", when="@5.6.8")
        depends_on("py-pyutilib@5.7.2:", when="@5.6.7")
        depends_on("py-pyutilib@5.7.1:", when="@5.6.6")
        depends_on("py-six@1.4:", when="@5.5.1:5.7.0")
    # END DEPENDENCIES

