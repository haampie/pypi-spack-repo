# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQpsolvers(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.3.1", sha256="a208aee3a699c0dc7fa41e0e9cd911895fc50ec767dd4361a26611703aa265c8", url="https://pypi.org/packages/9f/97/1723a0db426b132dc5be8bd460c5d61ad23bdadf663ba1c843440f9a0040/qpsolvers-4.3.1-py3-none-any.whl")
    version("4.3.0", sha256="e601f1814f4a02eb1ff593150c4449f7a24e41a4d3161ff6d0d451465be5bacc", url="https://pypi.org/packages/30/bc/9a2cd3e5a2ffd39a00b65266ed9df1308a01a70445d8b789f582e1e0c656/qpsolvers-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="ed2a274471e0eb718baa450e007f9537791c34feb21392941a0de400dc0801c5", url="https://pypi.org/packages/ff/da/47c16e6ae389f2000f7b89997456a839354c118b8dc46b891edc5215fa42/qpsolvers-4.2.0-py3-none-any.whl")
    version("4.1.1", sha256="54c85c44b739961dfde04706f3476d97a93273579116e56475e5dfec8762714b", url="https://pypi.org/packages/e5/db/2288a8eddda0927e9b24e40b02bcc0377c871eea69fa4d58834f5c9ab261/qpsolvers-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="265c09fa907d58346400af82fdd13af50f5841f90c410f4b710c7025a24a5080", url="https://pypi.org/packages/6f/2e/a03ce84a77dda58e1a4a92e414367b8c1bef0e1c30948b1d3d7adae2819c/qpsolvers-4.1.0-py3-none-any.whl")
    version("4.0.1", sha256="2439af8a5a15ef7b5208e4080bdf3d1df7ad9f9fe528766ea57c7d294591c298", url="https://pypi.org/packages/d3/5b/d26a8a0c2322ed2620287332ed88dba294636279723370416dc2fc31ed24/qpsolvers-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="cd8a5a1759ffe906198ccd8e5cdd83665cfe066edb401377d412cc508294c7f5", url="https://pypi.org/packages/e0/1b/5cf3888d13873a8d6e85fc3676c2e972e2a6a9fc059fecdaf12b02c9552f/qpsolvers-4.0.0-py3-none-any.whl")
    version("3.5.0", sha256="3929d04fc5d548b2db91f37c4b7b814af9722de1831382d47b51c8b58432f458", url="https://pypi.org/packages/dd/c3/227b9583c5ee26f4221755cafd4ba0cac2c2435a2d6145cd047846c1f489/qpsolvers-3.5.0-py3-none-any.whl")
    version("3.4.0", sha256="2788f1cba7b64bdf7cc32fe616946784962f187bd285229ffb6b7a15b8863f28", url="https://pypi.org/packages/4c/bd/c0c34384e04e7fd2b437d3552dbd5d2365bbc109b1c060f8cb97b176478e/qpsolvers-3.4.0-py3-none-any.whl")
    version("3.3.1", sha256="ce161a81e15fbcffa56bcf8e2c1ef0da1f797f050adab63f386ce4c14712f864", url="https://pypi.org/packages/39/46/e7f9d8fbf4d70a842b456e6d8c70e41183e4a7ce928b7eeff17ba49a4b9c/qpsolvers-3.3.1-py3-none-any.whl")
    version("3.2.0", sha256="ba1651a45ce23c49786bcf8327d83943092a124f84024da3dfdc44735c25aae9", url="https://pypi.org/packages/b6/c5/2afcb9c856385f7a1c8d804ff7a52f45bc44b20a5e936f01005213fe24fc/qpsolvers-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="2b17ca23eb87124aa6f3844fcdb3affbc55b78ac7f89dcb0d2e706df899783c1", url="https://pypi.org/packages/cd/d1/b877f55bc00f2ea99c3862ecb07c1c0ef5ccc7b0cbfb49636d3505911d88/qpsolvers-3.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cvxopt@1.2.6:", when="@3:3.0")
        depends_on("py-daqp@0.5.1:", when="@3.3.1:4.2")
        depends_on("py-ecos@2.0.8:", when="@3:4.2")
        depends_on("py-numpy@1.15.4:", when="@2.6:")
        depends_on("py-osqp@0.6.2:", when="@3:4.2")
        depends_on("py-quadprog@0.1.11:", when="@3:3.0")
        depends_on("py-scipy@1.2.0:", when="@1.7.2:")
        depends_on("py-scs@3.2:", when="@3:4.2")
    # END DEPENDENCIES

