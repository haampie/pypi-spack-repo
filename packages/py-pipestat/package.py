##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPipestat(PythonPackage):
    version("0.8.3-alpha1", sha256="f678656cb920d7c59b6da491eba5d7b2ffeecf3378bbf75b07f11c0ce8d5afac", url="https://pypi.org/packages/e5/cf/205010e1c4cc64eefabbf327f65496a08176d14add1a36817745bf3efad3/pipestat-0.8.3a1-py3-none-any.whl")
    version("0.8.2", sha256="079a392a17314a7aa26aa92f3df64c09a5aa5b58352ef559149b14701852ae7d", url="https://pypi.org/packages/4d/05/625124ed97b885294d5b2ae0cc55a9c175c35c8a24077e026479c6f6fca9/pipestat-0.8.2-py3-none-any.whl")
    version("0.8.2-alpha1", sha256="0eb38fe24f1a0031316124c4157f1996c9dfca4c431b64321d35df9ab81dca9f", url="https://pypi.org/packages/49/0c/7f64daeb627c66feefb70aacad014bb5341bdd5995b8ab3615d905cdcf33/pipestat-0.8.2a1-py3-none-any.whl")
    version("0.8.1", sha256="8da054887b2c1ba756979ef0e005c7aa12c2dad51c2849b936ed9fc552a0ace4", url="https://pypi.org/packages/12/a8/c72e37201a27214eaa2fa930a0ff228d0a2e01fa333702db06f18a4a4683/pipestat-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="7eefabdda82bbbfa1f5582848b0072683f1b0d165fbacce3dfff0ed1d61d3f59", url="https://pypi.org/packages/68/a6/f7700e3185839e531f8c6b4cf993b31ca82707663ad848fbab0be1683824/pipestat-0.8.0-py3-none-any.whl")
    version("0.8.0-alpha1", sha256="80093eb195f657e5de06a3c2ec3bcd5cba16f6df9fe0d8ac05ffe6791918afb2", url="https://pypi.org/packages/17/2c/2b23fb3c32eb0d14691f744519a1f79d11921f19f61d66add9b34cdbfcb7/pipestat-0.8.0a1-py3-none-any.whl")
    version("0.7.1-alpha1", sha256="7e05121a28bfd4e88a27be514e0fa62bb07b398dfec8332284b7375a39fcb157", url="https://pypi.org/packages/59/c5/0fe582fa71da735480217a9ce6066422c2c2b58842c0f3a968141216941a/pipestat-0.7.1a1-py3-none-any.whl")
    version("0.7.0", sha256="62798d2e51e3bd0014bb84a9839d6395f3b1c7d6ad404bc25d21659372975823", url="https://pypi.org/packages/ed/0e/49aa7f3111af864d262d49f68c0995bf599732b7c959c9333aac219cd2a8/pipestat-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="c0732b7ef4925d40fa0fad13deb14d00899b45db5534a9aeed37224d6ff3974a", url="https://pypi.org/packages/61/b2/a325d31714c74bb7080cf07eaa4dc76cd5c4cca3fe50069a84bed4e5b72d/pipestat-0.6.0-py3-none-any.whl")
    version("0.6.0-alpha11", sha256="30d192336bce0bad6b7b12fe2dcb29cf57146d0ddc76fb3f866c1ce0219bfc3a", url="https://pypi.org/packages/e7/27/4551f92a686f9b49f7515f9ef47ae960845ee6c2f01b9ea96a65732bed23/pipestat-0.6.0a11-py3-none-any.whl")
    version("0.5.2", sha256="34645fb789344a15e4a8cc065c012831c86d5761860db6a49cb41ee9fa1f71b1", url="https://pypi.org/packages/37/1e/5be8c02916223e7710ca0eabefd877ea3d463ce2bcd33eee27cfac0a2e91/pipestat-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="6f3e373340b3f3eb8ec91d04f200c96b95e6e447f8b914980eb92756293835ca", url="https://pypi.org/packages/30/cc/fe966706151f43c775323e8ab389f7a19d581ac5b91640516d010b1e4b9a/pipestat-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="5ed5abce53c61d58fba89d246a032d116439585110180d8be4b3bb18d430ad02", url="https://pypi.org/packages/4c/ec/2062a05ab1903ff2626d18e25742f9c19249f2a53a9c15adeb61832fb591/pipestat-0.5.0-py3-none-any.whl")
    version("0.4.1", sha256="91239689a59244196906ef2d68023161c4421c79fcdb0bf20e80c6a7039f8217", url="https://pypi.org/packages/48/05/773587d75d5d15c9ce429f2ff46987d4eb9b90ef2ba982e1d61c17e42e63/pipestat-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="45d31092ac30be522fcf7a792a8170268e060273598a575e178218e9ad7299c6", url="https://pypi.org/packages/14/f7/fe41097949eb5c1a7ac9e6b06bd3594b104d54d3add5f57540dde2e2023e/pipestat-0.4.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-eido", when="@0.4.1:")
        depends_on("py-fastapi", when="@0.6:0.6.0-alpha2")
        depends_on("py-jinja2", when="@0.5.2:0.5,0.6.0-alpha2:")
        depends_on("py-jsonschema", when="@0.0.2:")
        depends_on("py-logmuse@0.2.5:", when="@0.0.2:")
        depends_on("py-oyaml", when="@0.0.2:")
        depends_on("py-pandas", when="@0.4.1:")
        depends_on("py-psycopg2-binary", when="@0.0.2:0.6.0-alpha2")
        depends_on("py-pydantic", when="@0.4.1:0.6.0-alpha2")
        depends_on("py-pydantic@2:", when="@0.4:0.4.0")
        depends_on("py-pyyaml", when="@0.4:0.8.0-alpha1")
        depends_on("py-sqlmodel@0.0.8:", when="@0.4:0.6.0-alpha2")
        depends_on("py-ubiquerg@0.6.1:", when="@0.0.2:")
        depends_on("py-uvicorn", when="@0.6:0.6.0-alpha2")
        depends_on("py-yacman@0.9.3:", when="@0.8.2-alpha1:")
        depends_on("py-yacman@0.9.2:", when="@0.6.0-alpha8:0.8.1")
        depends_on("py-yacman@0.9.1:", when="@0.4.1:0.6.0-alpha7")
        depends_on("py-yacman@0.9:", when="@0.4:0.4.0")

