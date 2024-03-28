# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpyvue(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.10.2", sha256="c5926f50a90cd090d58dc5ec10afed57e6726c4ba8a51ab1aa6f9f7fcbe284bc", url="https://pypi.org/packages/a9/f7/5f899dac3dc430921ba7100d189bc90035fc7476d326a5fac07a4bc95059/ipyvue-1.10.2-py2.py3-none-any.whl")
    version("1.10.1", sha256="572057b4b003b5a1b8cbe04eef2c41baa561fa74199cd2b9dd76cc4b5f2c5985", url="https://pypi.org/packages/5f/dc/107a9756ce488fbf4bb2dc8c08a3c4a680c96f2c7476b5014e14e9b71868/ipyvue-1.10.1-py2.py3-none-any.whl")
    version("1.10.0", sha256="dc971aa717c87539be9560cc209f5079ab606d90032e4086ee8ebc01a79bfb00", url="https://pypi.org/packages/04/6e/c50ef830cc3569458f0f23afb5d15c6f582f81de8ea2284dab6df8bf5097/ipyvue-1.10.0-py2.py3-none-any.whl")
    version("1.9.2", sha256="e35979c2ca980c227c681179d9c52fb5c04468c419ff50a23fc719c9239671ca", url="https://pypi.org/packages/82/c9/9c83d4f315915a7ebe11808394f052c96b55e7a226b22fbcf95b91283bd7/ipyvue-1.9.2-py2.py3-none-any.whl")
    version("1.9.1", sha256="b9df601979f3db142df7842e3c486b13fe84d7ade62ce18a478cd4bc4a819e15", url="https://pypi.org/packages/28/fb/ccaecc3f0ccd4c15865d2197e504d6e1d21a8951240edf45e972ff83ec12/ipyvue-1.9.1-py2.py3-none-any.whl")
    version("1.9.0", sha256="d0f2474c7c0eea1e07fa13c7e865283d58e3ad4189d2d50a964596b397f86241", url="https://pypi.org/packages/8f/43/7ee448890b2cbbb6e25fb281a5131922a13e47838dc5fbc2f5838ef33aec/ipyvue-1.9.0-py2.py3-none-any.whl")
    version("1.8.0", sha256="491b66bf80a3d2d601457e6d3c694acf4de36d2e1d174d4cb96a5c40edd7108a", url="https://pypi.org/packages/9b/ac/805253dd87452affe76b8291af7e37b0206ee5b9aa2f3295f6c99eda5227/ipyvue-1.8.0-py2.py3-none-any.whl")
    version("1.7.0", sha256="92039bfe6afdec45c93c0aba09e4efd44d64036947b4e3c4011275b4b11b4629", url="https://pypi.org/packages/4f/c7/4e0f0b2b0652b55149aab245cb5eec073a554724deae30315de7c118dd9d/ipyvue-1.7.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ipywidgets@7.0.0:", when="@1.4:")
    # END DEPENDENCIES

