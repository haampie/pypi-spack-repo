# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCwltool(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.1.20221201130942", sha256="8a816169cc97c9b6afe1b33df597351a060ea6c788b40762ea8de6ea6470b8a4", url="https://pypi.org/packages/1f/39/5ce0a18bcfc0b3381c4fbe6957d19a04f5753778cbc1a0640c32da3a74a8/cwltool-3.1.20221201130942-py3-none-any.whl")
    version("3.1.20221109155812", sha256="5936faeeef171417ad37784b1d6c899ac4803a7d7a0b973f2078ac98866f3cdf", url="https://pypi.org/packages/43/ee/8cad1c1d021f7aa25713a8865ba428e7bf0a19463a7f6d67aa3086dbddf5/cwltool-3.1.20221109155812-py3-none-any.whl")
    version("3.1.20211107152837", sha256="91521eee31a37831ac6228eb031eafcbbe9486b79b29eede01ad98ef20b69ab9", url="https://pypi.org/packages/76/98/14d603751d228fb6981d40fe97ee085badc50c169193303fcce0bb4d0be7/cwltool-3.1.20211107152837-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-argcomplete", when="@3.0.20201109103151:")
        depends_on("py-bagit@1.6.4:", when="@:1.0.0,1.0.20180711112827:3.1.20230526180938")
        depends_on("py-coloredlogs", when="@1.0.20190603140227:")
        depends_on("py-cwl-utils@0.19:", when="@3.1.20220913185150:3.1.20221201130942")
        depends_on("py-mypy-extensions", when="@:1.0.0,1.0.20180615183820:")
        depends_on("py-prov@1.5.1", when="@:1.0.0,1.0.20180711112827:")
        depends_on("py-psutil@5.6.6:", when="@3.1.20210616134059:")
        depends_on("py-pydot@1.4.1:", when="@3.0.20200720165847:")
        depends_on("py-pyparsing@:3.0.1,3.0.3:", when="@3.1.20211103193132:")
        depends_on("py-rdflib@4.2.2:6.2", when="@3.1.20220801180230:3.1.20230302145532")
        depends_on("py-rdflib@4.2.2:6.0", when="@3.1.20210816212154:3.1.20211107152837")
        depends_on("py-requests@2.6.1:", when="@1.0.20180906112546:")
        depends_on("py-ruamel-yaml@0.15:0.17.21", when="@3.1.20220217190813:3.1.20230425144158")
        depends_on("py-ruamel-yaml@0.15:0.17.17", when="@3.1.20211107152837")
        depends_on("py-schema-salad@8.2.20211104054942:", when="@3.1.20211104071347:3.1.20221201130942")
        depends_on("py-setuptools", when="@:1.0.0,1.0.20170713151519:1.0.20170721221557,1.0.20170803160545,1.0.20170817131858,1.0.20171107133715:1.0.20171227212058,1.0.20180116213856,1.0.20180224111654:")
        depends_on("py-shellescape@3.4.1:", when="@3.1.20210616134059:")
        depends_on("py-typing-extensions", when="@:1.0.0,1.0.20180806154020:3.1.20230906142556")
    # END DEPENDENCIES

