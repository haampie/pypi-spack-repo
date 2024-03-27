##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAccounts(PythonPackage):
    version("10.2", sha256="9616c8c27f08baadfeea7c27fb1efac043e0785fbbbfbe05f20021402ac5295f", url="https://pypi.org/packages/7d/d6/d6027ebf887f2fa01baf3ad5f21afc3dd91c1acc198cd660204006a444ae/pyobjc_framework_Accounts-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="30da31a76f2cfd0a4021eff4d4ff69e0a70b2f293290372f5909ae267d15a010", url="https://pypi.org/packages/6d/fc/35fa2ecd24407078cbb22b665b083d95c78e49eec32087a7000dbd468173/pyobjc_framework_Accounts-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="72c67d4b1f174d2045558d7b1348d5dce642ea0907ab3dfb79d2f449e601ad42", url="https://pypi.org/packages/1d/25/7f1bcaffc534f621a76c050a16dc0d0452abc3bb09b58d87896e08fdd341/pyobjc_framework_Accounts-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="0c218717d2a87cbd0014724f05f0041306934bf4f67b41de313350170626021c", url="https://pypi.org/packages/88/0b/93cc18218fa253302a767c4e6194bb4409036197cfb8b0e8c915087e5984/pyobjc_framework_Accounts-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="4d464f975e7f2d8ee7cf1a61013410b62ac8383de31ef795722aa8b574e27dc9", url="https://pypi.org/packages/cc/84/011cfc31558c3aaa4ad75294df446da6a177531ad88dfd26ed4326411d38/pyobjc_framework_Accounts-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="dd86f3fbefc543ed9cc041253f2dc3add217e40adf53421fa37e4b05186f975f", url="https://pypi.org/packages/10/0d/bfa8f486dbfa4f232076c05ef21fa2ea9e11e4423eda9a764d51a8d38373/pyobjc_framework_Accounts-9.1-py2.py3-none-any.whl")
    version("9.1-beta1", sha256="a120ff86874019678d8ca507cfee106d01cec218f097cce1d3f62c3871dabe48", url="https://pypi.org/packages/ac/00/51578210179e6aeab914e0b99470ef68041cd96b294955d09ab0d1743cc1/pyobjc_framework_Accounts-9.1b1-py2.py3-none-any.whl")
    version("9.0.1", sha256="3cdef323228580f28d2e444d77086a542a7824c26ac0aa769fe55259a869d44a", url="https://pypi.org/packages/c4/f7/82d098e17be129c6383f16e4b87ac19528bef6b7f43fed07425123125559/pyobjc_framework_Accounts-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="3eef8804d44666c5594444b3f627628b9f0466add5d7fcfb4f241878a7ae9733", url="https://pypi.org/packages/2e/0e/f61ba947bd428ab9efa486ddbef9eb058aa76edbebc7ff141d080fa2d139/pyobjc_framework_Accounts-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="3f2783c4ab0dfd64d42be9045595d908f7bcce82dea1088ad66780719fdb3a8d", url="https://pypi.org/packages/24/11/f8a4a3cf11189e7582aa38037d9d70720d44b9121ab0412794fb580349bd/pyobjc_framework_Accounts-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="67abb8dfa974c0b1924cd13c4d95ec013b29ddac6e2b8283eab2c8dabf6cfb28", url="https://pypi.org/packages/b1/75/a6f1b584e68e0077cfc89b2f8c901e607ecbf6f077f1730edb580661e054/pyobjc_framework_Accounts-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.1-beta1:", when="@9.1-beta1")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.1-beta1:", when="@9.1-beta1")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")

