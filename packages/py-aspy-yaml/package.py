# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAspyYaml(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.0", sha256="463372c043f70160a9ec950c3f1e4c3a82db5fca01d334b6bc89c7164d744bdc", url="https://pypi.org/packages/99/ce/78be097b00817ccf02deaf481eb7a603eecee6fa216e82fa7848cd265449/aspy.yaml-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="c7390d79f58eb9157406966201abf26da0d56c07e0ff0deadc39c8f4dbc13482", url="https://pypi.org/packages/c0/15/8f38955cbd3bf2f1bfbf7bec2a22517cdd098aa8eee60dafe49b2f7fd405/aspy.yaml-1.2.0-py2.py3-none-any.whl")
    version("1.1.2", sha256="19dd2ee74f96b72a3096d78be1a872914c70982299cda137725478954870a896", url="https://pypi.org/packages/c3/9d/16224e88f34048d1e7a251de7b77fa98f70f21a70c134fb6c21d6848380f/aspy.yaml-1.1.2-py2.py3-none-any.whl")
    version("1.1.1", sha256="04d26279513618f1024e1aba46471db870b3b33aef204c2d09bcf93bea9ba13f", url="https://pypi.org/packages/9f/e3/5d2ba9d098b687d3676a5a557f7edc15bb544d4c2af9fc7105469d2ba624/aspy.yaml-1.1.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="c959530fab398e2391516bc8d5146489f9273b07d87dd8ba5e8b73406f7cc1fa", url="https://pypi.org/packages/ae/c5/d4b43ea5d448ad68c234bcbd6e8c646449826bc6e3de617902738f3733ad/aspy.yaml-1.1.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="be70cc0ccd1ee1d30f589f2403792eb2ffa7546470af0a17179541b13d8374df", url="https://pypi.org/packages/90/b8/655098005544536b276c289eacf4fe99b04779741d737c59a11993313246/aspy.yaml-1.0.0-py2.py3-none-any.whl")
    version("0.3.0", sha256="ef9d73953d35eb995c0f16a3708fab3d9a9176e471fcc47eb0f2969085354ca9", url="https://pypi.org/packages/06/ee/8cf053404f46817db1145245d0260ca78da7d0b9e579bb338d3e7f7bb83e/aspy.yaml-0.3.0-py2.py3-none-any.whl")
    version("0.2.2", sha256="05a85584c9801a9f914fcc9089b0e25fbface9bd401f7db554a1512f60943b28", url="https://pypi.org/packages/f6/c8/c8e1d6cc88bf1020b90dc8ebc39f98d0433a492031e148deda6223ff104e/aspy.yaml-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="a91370183aea63c87d8487e7b399ed2d99a7c2f14b108d27c0bc8ad9ef595d9a", url="https://pypi.org/packages/f0/68/49af646ea5d7ea4a53209109c89a811e5b2569e802d4fcd28763cdded43c/aspy.yaml-0.2.1.tar.gz")
    version("0.2.0", sha256="b7b201524ab4b47abebb09c5cce219c14448febc56a3243fc1d7b534eb53632d", url="https://pypi.org/packages/c8/94/abcb14a1a7c8979cab58b86bc6c3bb4712c860c263b424a8d9647ba837a4/aspy.yaml-0.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyyaml", when="@0.2.2:")
    # END DEPENDENCIES

