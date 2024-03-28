# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReportlab(PythonPackage):
    # BEGIN VERSIONS
    version("4.1.0", sha256="28a40d5000afbd8ccae15a47f7abe2841768461354bede1a9d42841132997c98", url="https://pypi.org/packages/d2/70/c44e5fb6099cf28d01255ff1dfc6a4c8f2b981f314707018c802ac179e4e/reportlab-4.1.0-py3-none-any.whl")
    version("4.0.9", sha256="c9656216321897486e323be138f7aea67851cedc116b8cc35f8ec7f8cc763538", url="https://pypi.org/packages/cc/da/de8af288738de0980a7e982c62853efe9994ee7d07e59ed20fdccc8a658e/reportlab-4.0.9-py3-none-any.whl")
    version("4.0.8", sha256="d00693de8ab8761b122e409de883ba976c24839f93867090c0d40b5d5906e847", url="https://pypi.org/packages/44/2c/f09a5abefa8f2b575acfc19ed4536a365ef0432ae3bce94a57a2de9b4f52/reportlab-4.0.8-py3-none-any.whl")
    version("4.0.7", sha256="956d5874ee56e88753cf4c49452d6a7fa54a64e049a0382bd0c0b2013a26ef9a", url="https://pypi.org/packages/60/8b/fdd40ce4206bab7c8034f70925b8735c6fd57334d81e8aea9cfd0eb18603/reportlab-4.0.7-py3-none-any.whl")
    version("4.0.6", sha256="ec062675202eb76f6100ed44da64f38ed3c7feb5016cf4fe7f17ce35423ab14a", url="https://pypi.org/packages/7e/4b/f1d01a4e2712310ebb4715d38d01c5c72ce0fe27cc4540b9c1fd54a6d1df/reportlab-4.0.6-py3-none-any.whl")
    version("4.0.5", sha256="1344dbe779b9049a1888105503837d0e5b62163bf5c6b33bd1fbe84bad484f50", url="https://pypi.org/packages/c8/25/b4293db7882e9e3b8fb865325e3be0363aef2ca806efdaa21cddfdfa9cc7/reportlab-4.0.5-py3-none-any.whl")
    version("4.0.4", sha256="3dcda79ce04baf70721e2ec54854722644262cac2feec3d5c4c5e77015504cb0", url="https://pypi.org/packages/db/8a/68ad8fb26592f1749c19b6e651296eeffb808a81f56be3dc09a739120676/reportlab-4.0.4-py3-none-any.whl")
    version("4.0.0", sha256="a1433a24cee3119fdc142487c6594d72621dd1d5d33df2d032c559aa0bb8b115", url="https://pypi.org/packages/a2/31/ebd3d48525ddb71790e61cdb28621517d1c4a245feb87fb503384b103eb8/reportlab-4.0.0-py3-none-any.whl")
    version("3.6.13", sha256="6f75d33f7a3720cf47371ab63ced0f0ebd1aeb6db19386ae92f8977a09be9611", url="https://pypi.org/packages/65/82/45b443db5acaf7edb471be57335a22d9f3bb6e4e9c9133ffa926f8ecdf2a/reportlab-3.6.13.tar.gz")
    version("3.6.12", sha256="b13cebf4e397bba14542bcd023338b6ff2c151a3a12aabca89eecbf972cb361a", url="https://pypi.org/packages/b8/ac/10d68a650b321bd8c4d8cbefd9994e7727d57b381c9bdb0a013273011e62/reportlab-3.6.12.tar.gz")
    version("3.4.0", sha256="5beaf35e59dfd5ebd814fdefd76908292e818c982bd7332b5d347dfd2f01c343", url="https://pypi.org/packages/87/f9/53b34c58d3735a6df7d5c542bf4de60d699cfa6035e113ca08b3ecdcca3f/reportlab-3.4.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-chardet", when="@4.0.8:")
        depends_on("py-freetype-py@2.3", when="@4:4.0.0")
        depends_on("py-pillow@9:", when="@4:")
        depends_on("py-rlpycairo@0.2:", when="@4:4.0.0")
    # END DEPENDENCIES

