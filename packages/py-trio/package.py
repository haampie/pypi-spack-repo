# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.25.0", sha256="e6458efe29cc543e557a91e614e2b51710eba2961669329ce9c862d50c6e8e81", url="https://pypi.org/packages/17/c9/f86f89f14d52f9f2f652ce24cb2f60141a51d087db1563f3fba94ba07346/trio-0.25.0-py3-none-any.whl")
    version("0.24.0", sha256="c3bd3a4e3e3025cd9a2241eae75637c43fe0b9e88b4c97b9161a55b9e54cd72c", url="https://pypi.org/packages/14/fb/9299cf74953f473a15accfdbe2c15218e766bae8c796f2567c83bae03e98/trio-0.24.0-py3-none-any.whl")
    version("0.23.2", sha256="5a0b566fa5d50cf231cfd6b08f3b03aa4179ff004b8f3144059587039e2b26d3", url="https://pypi.org/packages/3e/14/746bb2b403af4be680ca0ae240d62473c4ec3b836024c2e85f27856d7991/trio-0.23.2-py3-none-any.whl")
    version("0.23.1", sha256="bb4abb3f4af23f96679e7c8cdabb8b234520f2498550d2cf63ebfd95f2ce27fe", url="https://pypi.org/packages/39/46/620fbe56f41fa3ccdda2136d947fb9bacce3d1eb163f057f0262a0ddf5e0/trio-0.23.1-py3-none-any.whl")
    version("0.23.0", sha256="213cd69a05962b1ba24d48caf08f7e7acf02bf1ebfac17c06d1248497f05795e", url="https://pypi.org/packages/a3/79/51dddde218dddbdebcb8bfdd42bba7b216eb3a5703f9a5aefef5d565aee0/trio-0.23.0-py3-none-any.whl")
    version("0.22.2", sha256="f43da357620e5872b3d940a2e3589aa251fd3f881b65a608d742e00809b1ec38", url="https://pypi.org/packages/a3/dd/b61fa61b186d3267ef3903048fbee29132963ae762fb70b08d4a3cd6f7aa/trio-0.22.2-py3-none-any.whl")
    version("0.22.1", sha256="1270da4a4a33caf33f85c6a255f2ef5f71629a3ec9aea31a052062b673ae58d3", url="https://pypi.org/packages/70/2f/6428bcc201e4db129b3320bd33d803a41e0706cf1aec44fa2f8425777493/trio-0.22.1-py3-none-any.whl")
    version("0.22.0", sha256="f1dd0780a89bfc880c7c7994519cb53f62aacb2c25ff487001c0052bd721cdf0", url="https://pypi.org/packages/f1/ed/3623a910f9bb7a31b067d6baef476ed6e294e92a245f94ab992988e4a666/trio-0.22.0-py3-none-any.whl")
    version("0.21.0", sha256="4dc0bf9d5cc78767fc4516325b6d80cc0968705a31d0eec2ecd7cdda466265b0", url="https://pypi.org/packages/a9/bc/aef5a15725e95df49d41838dd816b95aad7df07de9f87e4ff453a3326615/trio-0.21.0-py3-none-any.whl")
    version("0.20.0", sha256="fb2d48e4eab0dfb786a472cd514aaadc71e3445b203bc300bad93daa75d77c1a", url="https://pypi.org/packages/39/b3/c6fc163c9343e95432d60a2b681bc14d78fda70dff50210687314d94143d/trio-0.20.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-async-generator@1.9:", when="@0.11:0.22.0")
        depends_on("py-attrs@23.2:", when="@0.25:")
        depends_on("py-attrs@20:", when="@0.22.1:0.24")
        depends_on("py-attrs@19.2:", when="@0.13:0.22.0")
        depends_on("py-exceptiongroup", when="@0.23.2: ^python@:3.10")
        depends_on("py-exceptiongroup@1.0.0-rc9:", when="@0.22:0.23.1 ^python@:3.10")
        depends_on("py-idna", when="@0.2:0.3,0.11:")
        depends_on("py-outcome", when="@0.11:")
        depends_on("py-sniffio@1.3:", when="@0.23:")
        depends_on("py-sniffio", when="@0.11:0.22")
        depends_on("py-sortedcontainers", when="@0.1:0.3,0.11:")

        # marker: os_name == "nt"
        # depends_on("py-cffi@1.14:", when="@0.14")

        # marker: os_name == "nt" and implementation_name != "pypy"
        # depends_on("py-cffi@1.14:", when="@0.15:")
    # END DEPENDENCIES

