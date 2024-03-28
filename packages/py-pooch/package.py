# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPooch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.8.1", sha256="6b56611ac320c239faece1ac51a60b25796792599ce5c0b1bb87bf01df55e0a9", url="https://pypi.org/packages/f4/72/8ae0f1ba4ce6a4f6d4d01a60a9fdf690fde188c45c1872b0b4ddb0607ace/pooch-1.8.1-py3-none-any.whl")
    version("1.8.0", sha256="1bfba436d9e2ad5199ccad3583cca8c241b8736b5bb23fe67c213d52650dbb66", url="https://pypi.org/packages/1a/a5/5174dac3957ac412e80a00f30b6507031fcab7000afc9ea0ac413bddcff2/pooch-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="74258224fc33d58f53113cf955e8d51bf01386b91492927d0d1b6b341a765ad7", url="https://pypi.org/packages/84/8c/4da580db7fb4cfce8f5ed78e7d2aa542e6f201edd69d3d8a96917a8ff63c/pooch-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="3bf0e20027096836b8dbce0152dbb785a269abeb621618eb4bdd275ff1e23c9c", url="https://pypi.org/packages/8d/64/8e1bfeda3ba0f267b2d9a918e8ca51db8652d0e1a3412a5b3dbce85d90b6/pooch-1.6.0-py3-none-any.whl")
    version("1.5.2", sha256="debb159655de9eeccc366deb111fe1e33e76efac19724436b6878c09deca4293", url="https://pypi.org/packages/76/1e/5092523703289aa1a9c14b1ed09d4eda6de76d7eee9ee6b26b54d675e73f/pooch-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="0548f1875de9aef22bef328388dd5e7e1df3985c5e5f575737327cb9a2f430b5", url="https://pypi.org/packages/91/d7/a830fcc77f79f6d3c476ab86895dcc4f3c5123962ed02a82dc51f221dfa9/pooch-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="54c9321a1cab8cd056ced497649eac69891066038319b31bebf13ec8ac79862b", url="https://pypi.org/packages/1a/57/03a879380fe8b501e25617ea59a51a390ee9a5a09769945e8cb2c21ecaf1/pooch-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="f6ee25f6638cfce239134c2d991d311dd2bde3f6a3ac11c953606313109fd5f5", url="https://pypi.org/packages/a2/50/5de294eee4babf84de51694e8f49bdbdf9f287d77af616c07898f3b4e898/pooch-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="2cec8cbd0515462da1f84446113e77a785029b8514841e0ad344dd57f7924902", url="https://pypi.org/packages/40/b9/9876662636ba451d4406543047c0b45ca5b4e830f931308c8274dad1db43/pooch-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="aee50e16ca143b581bf598890737a5838b1818bc30a5863f0b67ec405bd9081c", url="https://pypi.org/packages/ce/11/d7a1dc8173a4085759710e69aae6e070d0d432db84013c7c343e4e522b76/pooch-1.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-appdirs@1.3:", when="@1.6")
        depends_on("py-appdirs", when="@0.3:1.5")
        depends_on("py-packaging@20:", when="@1.6:")
        depends_on("py-packaging", when="@:1.5")
        depends_on("py-platformdirs@2.5:", when="@1.7:")
        depends_on("py-requests@2.19:", when="@1.6:")
        depends_on("py-requests", when="@:1.5")
    # END DEPENDENCIES

