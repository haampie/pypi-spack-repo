# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMffpy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.0", sha256="4c30cfcd2e20962a3c4c0a922590c35315092a6bb65a83951c4849ec251dc720", url="https://pypi.org/packages/97/b6/07e63c68c8ad38a8e76a8c09ba95d7140e903af428e40f33ecacf9c671eb/mffpy-0.8.0-py3-none-any.whl")
    version("0.7.4", sha256="3610d5e6724b89d2cd37d1df9220380ab08dfcf2b53f15dc4fb2fb541f779113", url="https://pypi.org/packages/31/f1/90641e23ae3675b0e72f49b4877775fe7543b2b2020aedccf59672ddda94/mffpy-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="1bcd54c946d0d19a7e4922365ee8788d47c4fd3df8900f0a267b7916611abd30", url="https://pypi.org/packages/fb/65/eba4b938e6fdb2bec21fb837e3da709c722d5eb79e7dd1b04ff77a4b5c9f/mffpy-0.7.3-py3-none-any.whl")
    version("0.7.2", sha256="8bf254bfea70cb336676d3846741bd901e84e6378013943b97d7a90ab7677e24", url="https://pypi.org/packages/90/18/ca132b27d8886ce3c7f063f422eaf4ad577aab7820f9d234c5c7882675a8/mffpy-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="8424b7c6799dbffc68c5d88166d7e68130e76f377e3c5bde200a5eafd063dcc0", url="https://pypi.org/packages/92/92/7ef73b39d2d260dbcd898b6d302e984e113fae8f33f40ade57a0f0db3401/mffpy-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="c69b873f861a011bd9ea1554b7a0d30ff1315e6533b191abf8a7a0dfde603f6c", url="https://pypi.org/packages/bf/b5/d19443f4a7e644b06356a02a6faf80faa5b6a7087d771059e2afebb0d7dc/mffpy-0.7.0-py3-none-any.whl")
    version("0.6.3", sha256="e10cbdaeb56c5c743c28ddae8b1e694bcc36c3fdba01f6f9210fea717caf8efb", url="https://pypi.org/packages/05/bf/9f59c5c9ad675efe44240e205c730fa4b9d363d5235646dd58a06fd099e4/mffpy-0.6.3-py3-none-any.whl")
    version("0.6.2", sha256="4e1a34a85860f82692c6f8dce4b18219ba862689d173e6a6b3369ad175934f25", url="https://pypi.org/packages/5f/f0/019343d6ebf46905982550ad267e6c34feddc2f96670e2bee3ff416be676/mffpy-0.6.2-py3-none-any.whl")
    version("0.6.0", sha256="a6a172fcc37f50e0d50007c52eb912dc05df76bf160ff049b6ba8897185de043", url="https://pypi.org/packages/3b/18/f91d1853d35593a5f28139229fbb7797a36e2b041d2774f39b200f6cc070/mffpy-0.6.0-py3-none-any.whl")
    version("0.5.9", sha256="c84823a00d5dc469543d5adef928fa04d48041363700c295afb452fb02b80ef7", url="https://pypi.org/packages/9f/38/c75cb09925c0e6ccdc9887a0788a475a05df4309f6296c7693d8ddce02d0/mffpy-0.5.9-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-deprecated@1.2.12:", when="@0.6.3:")
        depends_on("py-lxml@4.8:", when="@0.7.4:")
        depends_on("py-lxml@4.8", when="@0.7.3")
        depends_on("py-numpy@1.15.1:", when="@0.5.5:")
        depends_on("py-pytz@2019.2:", when="@0.5.5:")
    # END DEPENDENCIES

