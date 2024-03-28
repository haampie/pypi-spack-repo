# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEdflibPython(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.8", sha256="0c4ac78a0ac7af00e1c0aec582223ff9e330544d5b758f0e06508ed5188dd9e4", url="https://pypi.org/packages/d9/74/3152076443abeee13bcc3c91585863d3a1491e337c983751d30e21b98aea/EDFlib_Python-1.0.8-py3-none-any.whl")
    version("1.0.7", sha256="9d81fbca705934b43fd568e20a01250aad475d591787fc0cc9f4bd68166f4cf9", url="https://pypi.org/packages/5c/f9/5348b05af9e50879d4d9198b04c13e116ff56308f4fb99b690cb5b6727d3/EDFlib_Python-1.0.7-py3-none-any.whl")
    version("1.0.6", sha256="b1f8fa4d72af5947aaf86fbe47a50cc5107dd0a57d10445f66a56561bda50359", url="https://pypi.org/packages/83/1e/8fa810ea73170f6957500077a2d5f26445d78c98e97a981cb352fffbc1e2/EDFlib_Python-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="bbc06bddd769fcfb7bc736b68f4641d6c58dff6267217d8f7e94bb5cd1bc45ea", url="https://pypi.org/packages/f9/28/8dc3202620d11eec18806809ee26f20faa3f0ba4843a92d7c02b5fdc4dd5/EDFlib_Python-1.0.5-py3-none-any.whl")
    version("1.0.3", sha256="0e91be00addaff9068bb846df9898727f4b41d25d5a96db292a7ba08e80e02e5", url="https://pypi.org/packages/75/25/e4b19ba2abfff013331bb76a4b90e5b043549b7eb101818487a0606932c6/EDFlib_Python-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="ea884d82f699dce8b4e1198cec5fb3505806441ff1ea0b45af6d75f765339db2", url="https://pypi.org/packages/86/33/2bbdaadba1a62a06dce8781591da3920d779f2e575686dc8eaf12203c236/EDFlib_Python-1.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.17.0:")
    # END DEPENDENCIES

