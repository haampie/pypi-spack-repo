##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtKeyvault(PythonPackage):
    version("10.3.0", sha256="3410cf6c703e9570ed3c8e9716e483c02b1804adde6ab437ddc8feac4545acd6", url="https://pypi.org/packages/8e/6f/565d9e7970d5098e7cb84d8b141f7936173ccb2b9046f397dde81a56cf4b/azure_mgmt_keyvault-10.3.0-py3-none-any.whl")
    version("10.2.3", sha256="0b8d02b1a3dbed36bca8b9c9b1cef547b82079b79203acefa3e9321d64f18f13", url="https://pypi.org/packages/14/be/66c3d7ce8e32e4eb32a7f4eaa99f6c12a3f1932f86c9d182440bba563754/azure_mgmt_keyvault-10.2.3-py3-none-any.whl")
    version("10.2.2", sha256="e59f35d43df274237ccf0a4d128adddcb3f3836c3399b1b6b24c7b592ed5a2ad", url="https://pypi.org/packages/ae/ab/154625ada3175d90b51aeedb8b1c4f257e0552141512b563002051e12d59/azure_mgmt_keyvault-10.2.2-py3-none-any.whl")
    version("10.2.1", sha256="3d7636bfb523d11f81024542857b9f7cc3b95945d5cd1c8aca97a85f4703c248", url="https://pypi.org/packages/03/17/d810951f9178520141b1c7395b3222fe34e4bf9182e9d12b58181c576355/azure_mgmt_keyvault-10.2.1-py3-none-any.whl")
    version("10.2.0", sha256="59a6ef61868bb4d72543359eaefc617992c510a2677566ca19da922d91900c35", url="https://pypi.org/packages/b3/20/b527fab17864f783785b892cdfb04288a0029c3c7bd5c71b5382afbc11d3/azure_mgmt_keyvault-10.2.0-py3-none-any.whl")
    version("10.1.0", sha256="c6f0e7ef65802d78f21476b7230f11921a8cdbcea5e63ef406fbb75704d65157", url="https://pypi.org/packages/84/49/6ec20461b154c725f199dfa8321928ac092c1ac131ea52e273baffc2c779/azure_mgmt_keyvault-10.1.0-py3-none-any.whl")
    version("10.0.0", sha256="af9f6894f3be794729d224872a90ef5258d54e16cb4f0b1317671ac2ce702326", url="https://pypi.org/packages/06/3c/4b7100fcfa770fe3377d826bf20194074523cd136c3d41d100fdcc09aa0a/azure_mgmt_keyvault-10.0.0-py3-none-any.whl")
    version("9.3.0", sha256="4ef0285292de9d833e5b1a56b9667ef7f7fd435ac44ad179b917ed3f3470c974", url="https://pypi.org/packages/49/54/a9494db523d449f02cc079ff99e28b45252c14503ebbe6009603a4731025/azure_mgmt_keyvault-9.3.0-py2.py3-none-any.whl")
    version("9.2.0", sha256="44029badad96201483e361c4b864c6d77acf62a0cc54324feea2a24ee7ea19e2", url="https://pypi.org/packages/4b/f3/894da6591ad123bcaa1f65efc437e7a879619a6a4473a39fb94ec9557d8b/azure_mgmt_keyvault-9.2.0-py2.py3-none-any.whl")
    version("9.1.0", sha256="81587675b0bbc4cc2b5f1d446aa8c065f62cc7069227d3a1de3d499359073d88", url="https://pypi.org/packages/93/c7/eb528a6bc644fdb7735802ae30783eb643e785017226eacc040dbd31fa13/azure_mgmt_keyvault-9.1.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="8b490af44d389b918b4feca41a27eab0e77d724f64db69e3e6e00c8b984e07f2", url="https://pypi.org/packages/f1/af/1ba15e7176bcf6b1531b453e410ae41a983c09f834d8700dfce739451b53/azure_mgmt_keyvault-2.2.0-py2.py3-none-any.whl")
    version("2.1.1", sha256="87547cb18a0cd6bc6a8d0aa62143d8338733545e3950c471be1ec6b228d642f1", url="https://pypi.org/packages/0e/b5/e48717d072714a7cf4d1e582cc720aaaa411dd70e81d18e82ecee2301b12/azure_mgmt_keyvault-2.1.1-py2.py3-none-any.whl")
    version("2.1.0", sha256="77c36e5a043dd09994c650d1992d919822733d4af80697a4335bf08786d4e5d0", url="https://pypi.org/packages/7d/b4/348115266e0def9f68998077a7d95c70b8878450c102f58df70bcb9f91b7/azure_mgmt_keyvault-2.1.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="70d0c5df6df6a8d1e40b834fb6b4728a509d6a272d96834d35224743211180c5", url="https://pypi.org/packages/b3/d1/9fed0a3a3b43d0b1ad59599b5c836ccc4cf117e26458075385bafe79575b/azure_mgmt_keyvault-2.0.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="406298b6236abf9e3bae3218df2fc89c25aee471b917eca7769ff5696fc8ec01", url="https://pypi.org/packages/49/de/0d69aedae7c5f6428314640b65947203ab80409c12b5d4e66fb5b7a4182e/azure_mgmt_keyvault-1.1.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="6eb995e7db41179960716f2ac5573ed5a6fffe7c1c40aae9391bb045fe6dfc56", url="https://pypi.org/packages/fa/a9/cb52f53824b15491ee0a9532c6003745edbb6643b8cd55e263942d8df73c/azure_mgmt_keyvault-1.0.0-py2.py3-none-any.whl")
    version("1.0.0-beta1", sha256="66fd1794896e6f5c81c951d5efeee9e09abb8fda151f8c18114d72633b8cf0bb", url="https://pypi.org/packages/21/8e/7a6b6eca4d5e206fa83461cc625e3e3df58a3e989f399db2678d49baf5cf/azure_mgmt_keyvault-1.0.0b1-py2.py3-none-any.whl")
    version("0.40.0", sha256="bd7fff997ce52fd06e0992ff5d4606450e4173e77d6feade7e8b145fe049dcee", url="https://pypi.org/packages/45/5a/f3182d7ed82173d9af0bd96d01de4002eca8fddbd3c1feb99d839c5f4657/azure_mgmt_keyvault-0.40.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@1.0.0:")
        depends_on("py-azure-common@1.1.5:", when="@0.31:1.0.0-beta1")
        depends_on("py-azure-mgmt-core@1.3.2:", when="@10.2:")
        depends_on("py-azure-mgmt-core@1.3.1:", when="@10.1")
        depends_on("py-azure-mgmt-core@1.3.0:", when="@10:10.0")
        depends_on("py-azure-mgmt-core@1.2:", when="@7.0.0:9")
        depends_on("py-azure-mgmt-nspkg@2:", when="@0.31:0,1.0.0:1")
        depends_on("py-isodate@0.6.1:", when="@10.2.1:")
        depends_on("py-msrest@0.7.1:", when="@10.2:10.2.0")
        depends_on("py-msrest@0.6.21:", when="@9:10.1")
        depends_on("py-msrest@0.5:", when="@1.1:8")
        depends_on("py-msrestazure@0.4.32:", when="@1.1:2")
        depends_on("py-msrestazure@0.4.27:", when="@1.0.0:1.0")
        depends_on("py-msrestazure@0.4.7:0.4", when="@0.31:1.0.0-beta1")

