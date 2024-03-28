# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySupervisor(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.2.5", sha256="2ecaede32fc25af814696374b79e42644ecaba5c09494c51016ffda9602d0f08", url="https://pypi.org/packages/2c/7a/0ad3973941590c040475046fef37a2b08a76691e61aa59540828ee235a6e/supervisor-4.2.5-py2.py3-none-any.whl")
    version("4.2.4", sha256="bbae57abf74e078fe0ecc9f30068b6da41b840546e233ef1e659a12e4c875af6", url="https://pypi.org/packages/3d/47/b4030b2b01f6c559bd528974cee72bee7fe75594b31cc3e064678a454548/supervisor-4.2.4-py2.py3-none-any.whl")
    version("4.2.3", sha256="515d3649314b1ee2dbc77a0b6c37780a57d7400490b687492c33e1db5fb7254e", url="https://pypi.org/packages/17/bd/67ca5b63c1c58530d64e859a9c0b8588d892f2603cba8f5b556bf52d0ebf/supervisor-4.2.3-py2.py3-none-any.whl")
    version("4.2.2", sha256="4adf63c8f18cf42313171ce06a73c9ae2c5e88ef27c2bb0de3b8405368595c04", url="https://pypi.org/packages/de/c9/50b1575b46ad9802e1b8d444c1ba0db842a1006ff7c9bea9d5e0ea700f2d/supervisor-4.2.2-py2.py3-none-any.whl")
    version("4.2.1", sha256="75ae1d758fd6a1cb5f878333b309e0e2cb351bd6487188e4c457cc1c8ec29904", url="https://pypi.org/packages/08/b2/6f9f199774860e3c180dcdf9bf3191a8588f5ece417d03661d25155cfdfe/supervisor-4.2.1-py2.py3-none-any.whl")
    version("4.2.0", sha256="7720750ebb83ac16204ff7037c3d828ba2e0502fa0b29e6de40bc6482b08a55c", url="https://pypi.org/packages/2f/43/130066cd6003233401142f5f98cd09c93165f5c6408f850dd965b4f2470e/supervisor-4.2.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="a76b2f77a560f2dc411c0254a4eb15f555e99faac48621b0f1fc9ab013944f47", url="https://pypi.org/packages/ca/1f/07713b0e1e34c312450878801d496bce8b9eff5ea9e70d41ff4e299b2df5/supervisor-4.1.0-py2.py3-none-any.whl")
    version("4.0.4", sha256="43e87c7b572a94acdb586aaebb06844dae1aa02856b984c5a738032abd753fb7", url="https://pypi.org/packages/a5/27/03ee384818f4fc5f678743bb20ac49c5b4fc9f531bd404dec4b61a8b5d42/supervisor-4.0.4-py2.py3-none-any.whl")
    version("4.0.3", sha256="a3289b9124e59aee1621d43b55cd1634468cb3212d09c5b0114a3183cc080cca", url="https://pypi.org/packages/3f/1c/78026a80b8ff35e7c14adb331efb28e6ff2964dbae7e8bd9c52ef7c377a0/supervisor-4.0.3-py2.py3-none-any.whl")
    version("4.0.2", sha256="cb16df95144b68f016d652a2311a47d0f8cd8935a524d77b7c490eae77c44989", url="https://pypi.org/packages/a3/cf/38490f22074863763c3cedddce893e5a2423ac144ec77a04d78a43b4ab75/supervisor-4.0.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-meld3@1:", when="@4:4.0")
        depends_on("py-setuptools", when="@4.2.3:")
    # END DEPENDENCIES

