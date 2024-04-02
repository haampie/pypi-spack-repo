# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySqlalchemy(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.19", sha256="77a14fa20264af73ddcdb1e2b9c5a829b8cc6b8304d0f093271980e36c200a3f", url="https://pypi.org/packages/e5/07/a928d473438adb98ebd2264f584c4bd2dd711dfe6caf4b1906cba14dd375/SQLAlchemy-2.0.19.tar.gz")
    version("1.4.49", sha256="06ff25cbae30c396c4b7737464f2a7fc37a67b7da409993b182b024cec80aed9", url="https://pypi.org/packages/27/7c/ab28273996e8e5b78ddaeddbc1df54033231ff325827b3149d51334ed852/SQLAlchemy-1.4.49.tar.gz")
    version("1.4.45", sha256="fd69850860093a3f69fefe0ab56d041edfdfe18510b53d9a2eaecba2f15fa795", url="https://pypi.org/packages/76/d5/9ce70fd0d2858c72ecacff0c0518e9ddfbbaf4753b85e49f6d94ad74de36/SQLAlchemy-1.4.45.tar.gz")
    version("1.4.44", sha256="2dda5f96719ae89b3ec0f1b79698d86eb9aecb1d54e990abb3fdd92c04b46a90", url="https://pypi.org/packages/eb/71/f5f512914b86bd007bf842d9b95dba78eedb899d46025ab86b197b22ae62/SQLAlchemy-1.4.44.tar.gz")
    version("1.4.25", sha256="1adf3d25e2e33afbcd48cfad8076f9378793be43e7fec3e4334306cac6bec138", url="https://pypi.org/packages/69/2b/f0ee898c3270d965300ec30b0bf06e062c4cc92f35d17ae6046f429c5067/SQLAlchemy-1.4.25.tar.gz")
    version("1.4.20", sha256="38ee3a266afef2978e82824650457f70c5d74ec0cadec1b10fe5ed6f038eb5d0", url="https://pypi.org/packages/b6/6b/d802a9223430cc4f55d7993ede4cdafa683fb8a1260516c48bcd59729c74/SQLAlchemy-1.4.20.tar.gz")
    version("1.3.19", sha256="3bba2e9fbedb0511769780fe1d63007081008c5c2d7d715e91858c94dbaa260e", url="https://pypi.org/packages/e3/aa/63c30deea197969211eb5bdf31f30abc9e3fc91eb01b78b6f328a36c31e5/SQLAlchemy-1.3.19.tar.gz")
    version("1.3.9", sha256="272a835758908412e75e87f75dd0179a51422715c125ce42109632910526b1fd", url="https://pypi.org/packages/89/4e/f10fc5063d1048b3813c0caf99f06ec2b73851ae1a939feb85315dacb3fc/SQLAlchemy-1.3.9.tar.gz")
    version("1.2.19", sha256="5bb2c4fc2bcc3447ad45716c66581eab982c007dcf925482498d8733f86f17c7", url="https://pypi.org/packages/f9/67/d07cf7ac7e6dd0bc55ba62816753f86d7c558107104ca915e730c9ec2512/SQLAlchemy-1.2.19.tar.gz")
    version("1.2.10", sha256="72325e67fb85f6e9ad304c603d83626d1df684fdf0c7ab1f0352e71feeab69d8", url="https://pypi.org/packages/8a/c2/29491103fd971f3988e90ee3a77bb58bad2ae2acd6e8ea30a6d1432c33a3/SQLAlchemy-1.2.10.tar.gz")
    version("1.1.18", sha256="8b0ec71af9291191ba83a91c03d157b19ab3e7119e27da97932a4773a3f664a9", url="https://pypi.org/packages/cc/4d/96d93ff77cd67aca7618e402191eee3490d8f5f245d6ab7622d35fe504f4/SQLAlchemy-1.1.18.tar.gz")
    version("1.0.12", sha256="6679e20eae780b67ba136a4a76f83bb264debaac2542beefe02069d0206518d1", url="https://pypi.org/packages/5c/52/9b48cd58eac58cae2a27923ff34c783f390b95413ff65669a86e98f80829/SQLAlchemy-1.0.12.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("backend", default=False, description="backend")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2:")
    # END DEPENDENCIES

