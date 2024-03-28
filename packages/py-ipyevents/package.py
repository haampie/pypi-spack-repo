# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpyevents(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.2", sha256="60c2a9e992bdc41e8577aa27e57b124efafa48a59a3bff886029fe5700d546b3", url="https://pypi.org/packages/af/49/5692d363a82838282f5c33a787922f07115d7ba4b452391e51db95c9d247/ipyevents-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="9f255fdab40e7598b1143ace90153c5f4e52be15dc6f1b94f575a043a5970c17", url="https://pypi.org/packages/45/9c/b2ae585af6f6b436df3924f45fada2a36e3a083cc4b01f50d9a291e0ca92/ipyevents-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="3186ac61189f3b4ab3ab6ba51d3580ac0fa37de1e7723da4b5d45bfc30db0daa", url="https://pypi.org/packages/c6/d0/7651e9991463e290c9abe2c1e56ffd7b8192c333366766d9116b6e2ab61c/ipyevents-2.0.0-py2.py3-none-any.whl")
    version("0.9.0", sha256="553b98cbf2ad48c127e5a98dfe7fca09d668474d32cf41e6ef13c98e64525f7e", url="https://pypi.org/packages/82/81/17278d0c9bbf8f6270ec297055d76bd23dfc9655f5d91b2a53cdcfdc18e5/ipyevents-0.9.0-py2.py3-none-any.whl")
    version("0.8.2", sha256="3f55583e43b744bd347cd0ae9404dfc3b55c4e8cc0e6e48c86198b210d5521cc", url="https://pypi.org/packages/ba/b5/b5861db870aa465be738996da9833fdf39e395b9aa0802ed2fc347297ae8/ipyevents-0.8.2-py2.py3-none-any.whl")
    version("0.8.1", sha256="c402034de0f8a6877f16307a9c958c0ab803822cd010abcee8ce0c40b1716859", url="https://pypi.org/packages/08/09/d82f7a20c7b036a0b160c80c2e968e6fd569f8cb23400f053842def96120/ipyevents-0.8.1-py2.py3-none-any.whl")
    version("0.8.0", sha256="09f9d3b93697d872546c1f08b304d1e2293e0607514f04075282609a759083bd", url="https://pypi.org/packages/85/f5/c653d1664db62f3b616a288eabe06b28f0bcee4a9884ee214e24dfcb29dd/ipyevents-0.8.0-py2.py3-none-any.whl")
    version("0.7.1", sha256="5d60cf06db9fd467287110271fec320458f2e335e8a89464fdd9b59361e00f4e", url="https://pypi.org/packages/7b/4c/1a399da7d9dd042cb69439d7e54de20ea6f8406bdd356aa5479627c16b1d/ipyevents-0.7.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="d7b4bf4b10a7cf0b94d5f29d8f290309167b8ceb486fc144b0bd30e4ea42800c", url="https://pypi.org/packages/99/ee/fcc8d01fbac08c27f2b7b937b3e0cdb091e5df87105e1d3465cf741a60d2/ipyevents-0.7.0-py2.py3-none-any.whl")
    version("0.6.3", sha256="bb6ad8c510830f5a96cf9ae69d502484c6a5af8e2e54ce42bb6a427c4593e9ec", url="https://pypi.org/packages/ed/18/06d1143f2ba91f04edf533e974442bcf64da5a6858f25f9f71380c259e1e/ipyevents-0.6.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ipywidgets@7.6.0:", when="@0.9:")
        depends_on("py-ipywidgets@7.0.0:", when="@0.2,0.4:0.4.0,0.5:0.8")
    # END DEPENDENCIES

