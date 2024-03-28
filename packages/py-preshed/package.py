# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPreshed(PythonPackage):
    # BEGIN VERSIONS
    version("3.0.9", sha256="721863c5244ffcd2651ad0928951a2c7c77b102f4e11a251ad85d37ee7621660", url="https://pypi.org/packages/f2/4e/76dbf784e7d4ed069f91a4c249b1d6ec6856ef0c0b2fd96992895d458b15/preshed-3.0.9.tar.gz")
    version("3.0.8", sha256="6c74c70078809bfddda17be96483c41d06d717934b07cab7921011d81758b357", url="https://pypi.org/packages/f1/78/c28a568317088b9cef21f8516bed2f41210492ae569c5842ad80251631a0/preshed-3.0.8.tar.gz")
    version("3.0.7", sha256="39cd2a0ab1adb11452c617831ea0ccea7d1712f2812d1744738735987513113a", url="https://pypi.org/packages/de/ff/3b1b47197a7c9bbf997fca9622f724bdd13eb45f608838b4551feacc624a/preshed-3.0.7.tar.gz")
    version("3.0.6", sha256="fb3b7588a3a0f2f2f1bf3fe403361b2b031212b73a37025aea1df7215af3772a", url="https://pypi.org/packages/c7/2e/f8ad19fa853727dfeee1114ee4ff45f10f259cbddf5cd23289992c06ccf4/preshed-3.0.6.tar.gz")
    version("3.0.5", sha256="c6d3dba39ed5059aaf99767017b9568c75b2d0780c3481e204b1daecde00360e", url="https://pypi.org/packages/ee/87/cabd3dc3d7ebd9b62252faca25ec5f1fec627ea88ca7ffd2924d02e1516e/preshed-3.0.5.tar.gz")
    version("3.0.4", sha256="13a779205d55ce323976ac06df597f9ec2d6f0563ebcf5652176cf4520c7d540", url="https://pypi.org/packages/8a/25/73d38655125d46a543656c0f025b3394a2ee010af3d0c46ed75d554bc1a9/preshed-3.0.4.tar.gz")
    version("3.0.3", sha256="8ad47d5d2688fabc66850f32c7b6d3b4a97e6b653726309fe09603edd6fceb23", url="https://pypi.org/packages/bd/d5/8044b241bfd384df2b3fdf1957a016dbcdfd473facd86a0339373ceb5730/preshed-3.0.3.tar.gz")
    version("3.0.2", sha256="61d73468c97c1d6d5a048de0b01d5a6fd052123358aca4823cdb277e436436cb", url="https://pypi.org/packages/5f/14/de231123ddbe0bf12bd9b1993122d67f22859643bee4dad3b6ce91986336/preshed-3.0.2.tar.gz")
    version("3.0.1", sha256="5a51b87e32382d43f675be1f538b4c307f66b33f5e7a0e87d96d3430b9b8ecb3", url="https://pypi.org/packages/e2/59/8528d263d04e7c6f6fa13c2477555fde93b36070d8b675d0532e73a4a759/preshed-3.0.1.tar.gz")
    version("3.0.0", sha256="11b67966085cea2e05303f694ed84592fa69cf387ed1e080a9bc102cd601c6d6", url="https://pypi.org/packages/6e/22/8664dd209eb837f0ee5fd05bbc7c71a797e4308973d4db176bf98584d141/preshed-3.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cymem@2:", when="@3.0.1:3.0.2,3.0.9:3")
        depends_on("py-murmurhash@0.28:1.0", when="@3.0.1:3.0.2,3.0.9:3")
    # END DEPENDENCIES

