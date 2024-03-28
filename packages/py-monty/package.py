# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMonty(PythonPackage):
    # BEGIN VERSIONS
    version("2024.2.26", sha256="8137bac170c045a3aacfec5ef65cabeaa8b9977a2e2fc9d99ab187881d7ebfb7", url="https://pypi.org/packages/3b/91/05be7fe6b4d66cdf63dc388de80df6a48a4e24780e9997e5ea2e916e679a/monty-2024.2.26-py3-none-any.whl")
    version("2024.2.2", sha256="d84b739315f02e337cc5d3fed70b196e6beb2b1bb8f2520a6e567a1bc31bf9d0", url="https://pypi.org/packages/52/39/4498be12d8025905f1c339ff2bcc7781e76900f8f85f522f71c854370103/monty-2024.2.2-py3-none-any.whl")
    version("2024.1.26", sha256="ffaaa3bfa628b853b9def134c09a622f53e9fe07634a998c1b428440bb2e5b44", url="https://pypi.org/packages/18/95/cbc6d4aceb71839664cf5c7fc59a698000234e55562ab53d21ec93a04174/monty-2024.1.26-py3-none-any.whl")
    version("2024.1.23", sha256="4699bf52ee04e6a67632ed8bf1f780e2ab0575c1d6a705b3287e1e19a9122bfc", url="https://pypi.org/packages/a8/f8/9bc0ddde2e4a296b589ac809d930a4c7a6040e897ace1bc031ed4c0f5c8b/monty-2024.1.23-py3-none-any.whl")
    version("2023.11.3", sha256="45ec3db046a77ca696041553d8403bc43162ad4892096a6c4c825acdb8b5e819", url="https://pypi.org/packages/28/0b/71fd3a6c7825847df91703b58119f2461a2773575d8b4f78710b511b5082/monty-2023.11.3-py3-none-any.whl")
    version("2023.9.25", sha256="5c77061fc910b9a2112ab457167910d21794c3f8c0abee626d7afcc55c996fd0", url="https://pypi.org/packages/5e/e5/d1d98b6c601ecab8d460efbff288724996e5c7aa7d54886fc67d8b2e5f57/monty-2023.9.25-py3-none-any.whl")
    version("2023.9.5", sha256="db9a4ca372cb68a7cb95845de010b5c09b2ae90d1ff1d1dc0755bc8c039e6e61", url="https://pypi.org/packages/e4/f6/48d2daf13a8bc8f636091a1465a037ac5804268cef22d03e2d7ccef6ee90/monty-2023.9.5-py3-none-any.whl")
    version("2023.8.8", sha256="32b352db16909791504762e1523463233d5cce711b8ad31856af7b748dd04f24", url="https://pypi.org/packages/b6/0a/fc3568d741e8494fcc24cdfd7688eea64ceb34dffbd639c41d2605b9c1c7/monty-2023.8.8-py3-none-any.whl")
    version("2023.8.7", sha256="bdc5f52bc817391c4a2c06f2c5b5291e08238a107227e79033ddd5e28feca352", url="https://pypi.org/packages/89/d8/bf876cd436aa564f6530b6c3d72061ed0aceb9de856cdaed9e3f65a08dff/monty-2023.8.7-py3-none-any.whl")
    version("2023.5.8", sha256="d8b8a00f146b6f56728b9e36399d2761718037ce86f67430cf98759aaf40bf78", url="https://pypi.org/packages/1d/9f/382152df1da45bc3645cc385bf51173604f86f6d9ad64abfa34ba3fa55e0/monty-2023.5.8-py3-none-any.whl")
    version("2021.8.17", sha256="adeda46dbf2231f0647be725fea9b290c292899d4f39d6d1e18838b4c5a6ca0c", url="https://pypi.org/packages/d0/ad/c19627ffddbd45097780431333ab1659dcbfcafede32c28d85c202b55467/monty-2021.8.17-py3-none-any.whl")
    version("0.9.6", sha256="bbf05646c4e86731c2398a57b1044add7487fc4ad03122578599ddd9a8892780", url="https://pypi.org/packages/53/61/b42d8ed8d28ee5ebd4dd3dce315e1e5176f70a138c869b15e2cc6f1ef468/monty-0.9.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.11:")
    # END DEPENDENCIES

