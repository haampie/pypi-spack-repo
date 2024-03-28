# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyupgrade(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.15.2", sha256="ce309e0ff8ecb73f56a45f12570be84bbbde9540d13697cacb261a7f595fb1f5", url="https://pypi.org/packages/7f/d8/2f5c6481ce50886a29cd2bfa8070a0f76672272446549ddcfe6baa5ec6bc/pyupgrade-3.15.2-py2.py3-none-any.whl")
    version("3.15.1", sha256="c5e005de2805edcd333d1deb04553200ec69da85e4bc9db37b16345ed9e27ed9", url="https://pypi.org/packages/aa/06/2ee12cb0825497f3b9a5afca35a0388bf98f0fe7842cd19cd9209dffad07/pyupgrade-3.15.1-py2.py3-none-any.whl")
    version("3.15.0", sha256="8dc8ebfaed43566e2c65994162795017c7db11f531558a74bc8aa077907bc305", url="https://pypi.org/packages/fc/70/884486403d78b58b4048863d34d15c59b48ce093dea80646df436ef00314/pyupgrade-3.15.0-py2.py3-none-any.whl")
    version("3.14.0", sha256="221923c5cd6171e4adb78bfd331ce95500112294c36fb61a0947c55c78cb1924", url="https://pypi.org/packages/9b/5e/6b65c23a06f0770b515057e0eea09a721fdb53177136a4fd7f1bbcbd1b82/pyupgrade-3.14.0-py2.py3-none-any.whl")
    version("3.13.0", sha256="8add43ca1fea6eaeb6815b0b987d1f6ff49ec48085169b2a32e9a797e2d2f8fd", url="https://pypi.org/packages/86/dd/cc79bcbab215cba72e4f01df9bb1c80c12dc0bf8230a85dd1105adc3a588/pyupgrade-3.13.0-py2.py3-none-any.whl")
    version("3.12.0", sha256="c6f9c129560b9538e75b93fb0aee20508faae454714e8373d462e408985bd96a", url="https://pypi.org/packages/a7/a7/8b4da61b21f56bc49620ee1acb57850d0b04df5486434c3e8ca5b04b99b1/pyupgrade-3.12.0-py2.py3-none-any.whl")
    version("3.11.2", sha256="f2291925693902afda3c1b7b4a255cd7083db45356b8aff5b1e6e209c4690322", url="https://pypi.org/packages/58/d3/da7092b16d2e8b3926750cc0f06cb2a3fbd1239971cd731b4ec2c96ae76c/pyupgrade-3.11.2-py2.py3-none-any.whl")
    version("3.11.1", sha256="6e9dd362394b3068123e06ca268de5845d41e2bb29f387b38323cc1009fb3100", url="https://pypi.org/packages/b7/33/95a23fe8c3075bd68e5e15cf2370540942929ac4ca25c0958425d883eb1b/pyupgrade-3.11.1-py2.py3-none-any.whl")
    version("3.11.0", sha256="7bd8b83bc1a61b3a4c8fea5e16313b7b29e5cdf1be6184f8c6c467557e9cfab3", url="https://pypi.org/packages/14/9a/47060e247da528f39168c124a209f800bb9e5db0032d5553d03d6a952508/pyupgrade-3.11.0-py2.py3-none-any.whl")
    version("3.10.1", sha256="f565b4d26daa46ed522e98746834e77e444269103f8bc04413d77dad95169a24", url="https://pypi.org/packages/82/46/050ffe4cfcab0ab5dea257fa92dfd39046fc059af38ac02ae49eeef916fb/pyupgrade-3.10.1-py2.py3-none-any.whl")
    version("3.3.1", sha256="3b93641963df022d605c78aeae4b5956a5296ea24701eafaef9c487527b77e60", url="https://pypi.org/packages/31/ee/dda0d7b86c4c0cd02494566243ad14f152e10994f1c345d57e9b9edd0c8a/pyupgrade-3.3.1-py2.py3-none-any.whl")
    version("2.38.4", sha256="944ff993c396ddc2b9012eb3de4cda138eb4c149b22c6c560d4c8bfd0e180982", url="https://pypi.org/packages/61/ac/985b625486935d7738829d98d6b873a8fa22fff183377882a6ee27861be5/pyupgrade-2.38.4-py2.py3-none-any.whl")
    version("2.38.3", sha256="7772a14bf5598a50135a9b6754f312a9a43adf3f86b1df036f6d9561bac011c4", url="https://pypi.org/packages/a4/93/a9518f1d79c0b28a5b57cdded56e8fbf5e4027b87dc798b4917c02bfd251/pyupgrade-2.38.3-py2.py3-none-any.whl")
    version("2.38.2", sha256="41bb9a9fd48fe57163b0dacffff433d6d5a63a0f7c2402918917b5f1a533342b", url="https://pypi.org/packages/2a/2e/15742fe9d036cfaae267e07eacb9ae1a2d25caed15dc7970206335ef8676/pyupgrade-2.38.2-py2.py3-none-any.whl")
    version("2.38.1", sha256="6ef3e7409d6e3648f1c4d71d7654e524a4fa59c58c4c9dc12aa750344ead96c7", url="https://pypi.org/packages/f8/55/d912fa7ae65d54a800e84b175d6d05cb6913fc12e0d773fd8b5e3a4f5cd9/pyupgrade-2.38.1-py2.py3-none-any.whl")
    version("2.38.0", sha256="e68e033603de3b4b675c7bd733723fb2bb7930a1898b6da61fb503643322e2f9", url="https://pypi.org/packages/20/c1/0ecb1890442196bb452cbfb160d675c90faaaaae07c0f13b4e1b753f9346/pyupgrade-2.38.0-py2.py3-none-any.whl")
    version("2.37.3", sha256="9746efd064dbf53d7f86d6f88a1d48120f58dbfc378f517768634740ea2225e2", url="https://pypi.org/packages/65/96/f99201ed9b18823c5c6c624528cc19c5a6868fa471ff9e143bc277bcab9a/pyupgrade-2.37.3-py2.py3-none-any.whl")
    version("2.37.2", sha256="5394cd5b1a8e1e4973c98ed2725449492dd2f2a285079c7b62ebaf06095bfce7", url="https://pypi.org/packages/00/84/cdf54461f81a35637df0fe066b7e88ec4b2de8164784a4ddc7801ccc34ed/pyupgrade-2.37.2-py2.py3-none-any.whl")
    version("2.37.1", sha256="dd2a32628d6d2a7dd6c086d98420e234b9e60c1e1d4c55431578491703e762a5", url="https://pypi.org/packages/fe/04/50f1a2abe56583ba194651c4835b906cbca6eebbb2343c17b2448a435163/pyupgrade-2.37.1-py2.py3-none-any.whl")
    version("2.37.0", sha256="0942c038aab199bed81274f259c6920f1b0065abde32f4092e3d0f55c970de29", url="https://pypi.org/packages/0a/e5/59de459eb22f6445e160eedfe11dea0ec05c08a3b79bb731bd544704a02f/pyupgrade-2.37.0-py2.py3-none-any.whl")
    version("2.36.0", sha256="3a68f9dd0d5b0c5e9768b00b5f94d796ff3945392211c2878daf309de6cf3493", url="https://pypi.org/packages/85/a2/09ffd90efc2adfb97bb9884042351bce142fd76ed766399c69d3760d13ae/pyupgrade-2.36.0-py2.py3-none-any.whl")
    version("2.31.1", sha256="4060a7c20c79d373a3dcf34566b275c6de6cd2b034ad22465d3263fb0de82648", url="https://pypi.org/packages/87/c5/5db2c423c83b9369f5985d2a9ca9318524756c028b46ab1827e15807e306/pyupgrade-2.31.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@3.9:")
        depends_on("py-tokenize-rt@5.2:", when="@3.10.1:")
        depends_on("py-tokenize-rt@:4", when="@2.38.4:2")
        depends_on("py-tokenize-rt@:3", when="@2.38.3")
        depends_on("py-tokenize-rt@3.2:", when="@1.20.2:2.38.2,3:3.9")
    # END DEPENDENCIES

