##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzuremlCore(PythonPackage):
    version("1.23.0", sha256="0965d0741e39cdb95cff5880dbf1a55fdd87cd9fc316884f965668e6cc36e628", url="https://pypi.org/packages/b8/4b/203468b7dc8ac633fc65a45c136efed2dca6ee29311db02b2ff1cee260d6/azureml_core-1.23.0-py3-none-any.whl")
    version("1.11.0.post2", sha256="f87111ea0311f77023ae15f7bccf1facf6b1c344be05c97358c73d3efa65d3b8", url="https://pypi.org/packages/c6/d4/1eadc80ad1b2dc4ca0c8f1e3b885d529cd3d90beea3006006fdb5977c383/azureml_core-1.11.0.post2-py3-none-any.whl")
    version("1.11.0.post1", sha256="2c4dc9038bb42306217bedd025ca0d2e5aee0ccd6e55403dff9f85f77ff17e2f", url="https://pypi.org/packages/1d/db/c665c5d6124b1b848d295f83d028f054763d6584c3e25e3f37b319a1755c/azureml_core-1.11.0.post1-py3-none-any.whl")
    version("1.11.0", sha256="df8a01b04bb156852480de0bdd78434ed84f386e1891752bdf887faeaa2ca417", url="https://pypi.org/packages/31/6e/851737ab431fca870d5f7927761163875ca5834842b55b0d496a8b93bfb9/azureml_core-1.11.0-py3-none-any.whl")
    version("1.8.0.post1", sha256="dd44d313b68d8e534f8e61e8484c519b9b88b32dc70d1f9d90c1d25f834e7f53", url="https://pypi.org/packages/d7/f8/70c0c428b6fb5d40aa21f6232f52a3bee33ae9402fc3bac88952b8c83989/azureml_core-1.8.0.post1-py3-none-any.whl")
    version("1.8.0", sha256="a0f2b0977f18fb7dcb88c314594a4a85c636a36be3d582be1cae25655fea6105", url="https://pypi.org/packages/22/38/6c763c4194b751550fd57fdfebcd3ec1431c0d634f17e004923ea7a4e90c/azureml_core-1.8.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@:3.8", when="@1.2:1.34")
        depends_on("py-adal@1.2:", when="@1:1.0.0,1.0.10:1.31")
        depends_on("py-azure-common@1.1.12:", when="@:1.26")
        depends_on("py-azure-graphrbac@0.40:")
        depends_on("py-azure-mgmt-authorization@0.40:0", when="@1.16:1.40")
        depends_on("py-azure-mgmt-authorization@0.40:", when="@:1.15")
        depends_on("py-azure-mgmt-containerregistry@2:", when="@:1.37")
        depends_on("py-azure-mgmt-keyvault@0.40:2", when="@1.16:1.29")
        depends_on("py-azure-mgmt-keyvault@0.40:", when="@:1.14")
        depends_on("py-azure-mgmt-network@10", when="@1.5:1.9")
        depends_on("py-azure-mgmt-resource@1.2.1:13", when="@1.16:1.36")
        depends_on("py-azure-mgmt-resource@1.2.1:10.2", when="@1.9.0.post:1.9,1.10.0.post2:1.10,1.11.0.post2:1.11,1.12.0.post2:1.12,1.13.0.post:1.13,1.14.0.post:1.15")
        depends_on("py-azure-mgmt-resource@1.2.1:", when="@:1.0.62.0,1.0.65:1.0.76.0,1.0.79:1.0.85.5,1.1:1.1.5.6,1.2:1.2.0.post1,1.4.0.post:1.9.0.0,1.10:1.10.0.post1,1.11:1.11.0.post1,1.12:1.12.0.post1,1.13:1.13.0.0,1.14:1.14.0.0")
        depends_on("py-azure-mgmt-storage@1.5:11", when="@1.16:1.36")
        depends_on("py-azure-mgmt-storage@1.5:", when="@:1.14")
        depends_on("py-backports-tempfile")
        depends_on("py-contextlib2", when="@:1.26")
        depends_on("py-cryptography@:1.8,2.3:3.2.0", when="@1.23:1.24.0.post1")
        depends_on("py-cryptography@:1.8,2.3:", when="@0.1.65:1.0.17.0,1.0.18:1.22,1.52:1.53")
        depends_on("py-docker", when="@:1.26")
        depends_on("py-jmespath", when="@1:1.0.0,1.0.10:1.26")
        depends_on("py-jsonpickle", when="@:1.26")
        depends_on("py-msrest@0.5.1:", when="@:1.26")
        depends_on("py-msrestazure@0.4.33:", when="@:1.31")
        depends_on("py-ndg-httpsclient", when="@:1.31")
        depends_on("py-pathspec", when="@:1.26")
        depends_on("py-pyjwt", when="@0.1.68:1.13.0.post1,1.14:1.14.0.post1,1.15:1.15.0.0,1.16:1.16.0.post1,1.17:1.17.0.0,1.22:")
        depends_on("py-pyopenssl@:20", when="@1.21:1.36")
        depends_on("py-pyopenssl", when="@1:1.0.0,1.0.17:1.15")
        depends_on("py-python-dateutil@2.7.3:", when="@:1.26")
        depends_on("py-pytz")
        depends_on("py-requests@2.19.1:", when="@:1.36")
        depends_on("py-ruamel-yaml@0.15.35:", when="@1.11.0.post:1.11,1.12.0.post:1.25.0.0,1.26:1.26.0.0")
        depends_on("py-ruamel-yaml@0.16.9:", when="@1.5.0.post4:1.11.0.0,1.12:1.12.0.0")
        depends_on("py-secretstorage", when="@1:1.0.0,1.0.17:1.26")
        depends_on("py-urllib3@1.23:", when="@:0.1.68,1:1.0.0,1.0.17:1.31")

