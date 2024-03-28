# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEmcee(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.4", sha256="13d216a96b4f60661839d5f6ec482eda9e86b499502cda2bf6d8cc839ccf3e59", url="https://pypi.org/packages/1c/2c/426cf760d1f1161b2c57272c7efc495bef353b0d1d609d91708ddfb831a2/emcee-3.1.4-py2.py3-none-any.whl")
    version("3.1.4-rc1", sha256="f321371834a7a74c51ebc20bed2b7c02d263d2cfc4fdef1f29d5047ec7bff9bb", url="https://pypi.org/packages/09/eb/ff8751a9fccf59718369e6260f2a96377a83d2a7f05b4db7323ddc4a3ce9/emcee-3.1.4rc1-py2.py3-none-any.whl")
    version("3.1.3", sha256="508a4d78933bd4f25c595acb44d3d0f810be69cb0e9b12012a5ed9bd35657987", url="https://pypi.org/packages/98/5f/e899376b4979559d74b082f20a78b159972fec9a4425d33d4eb797cfab55/emcee-3.1.3-py2.py3-none-any.whl")
    version("3.1.3-rc1", sha256="13d70651500d8fc7426ce5418fc5854626a06748b14059384254509c57576214", url="https://pypi.org/packages/a2/3c/78fd9c0a29dd4dacac988f63bfc34aa847666331ea28fe2094334881318c/emcee-3.1.3rc1-py2.py3-none-any.whl")
    version("3.1.2", sha256="88a816b09932048c58d3ff8a8ce8d8171ef0926314a887ebb45748979a8aa518", url="https://pypi.org/packages/85/7a/0b3ef15421b16d72b41d97a8d1ab271d07795161ee8971b747324c1d5032/emcee-3.1.2-py2.py3-none-any.whl")
    version("3.1.1", sha256="e01d68a84725f6c0734c3c31394e88a7252b12fddb44efe981e10956a7028a93", url="https://pypi.org/packages/ca/41/62ddfd3847bbf9247dcf163de1ff79d56eaa1ac33bfb382f925ab22ba638/emcee-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="b3195637280cc13efcbaaff8bbb0cac1eb43fc868cf85ccde8fc171e1b6da8ca", url="https://pypi.org/packages/71/9d/36b2a068f0d2b4426613af16a9efdaff7b4bbc79c3e6a25f377f60f295b1/emcee-3.1.0-py2.py3-none-any.whl")
    version("3.0.2", sha256="bffaa2e1830d90f4e2ae42ca8db9bef67b73eefe90bdedacf58c9a1977966184", url="https://pypi.org/packages/97/f4/00151f5f843088337c6a53edd6cbb2df340f1044d23080c662f95219cc3f/emcee-3.0.2-py2.py3-none-any.whl")
    version("3.0.1", sha256="96af059c717790341a68bad8c7b935dfe1c38beba6efabd8960af0591e31f068", url="https://pypi.org/packages/5c/e1/8ddb3d5059851cb84fee58fd94b916b045e2177c27ab43d35aa43bd5b5da/emcee-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="db451e4a95c15f7828d4ad0af1b0809b54cf067bacc8b827112b9ab40ce6bc31", url="https://pypi.org/packages/00/08/0d86d0af356d50ff00d741c34a90a971e7ae0a0aeb2bd050bcacfdc34229/emcee-3.0.0-py2.py3-none-any.whl")
    version("2.2.1", sha256="b83551e342b37311897906b3b8acf32979f4c5542e0a25786ada862d26241172", url="https://pypi.org/packages/3f/d3/7635106605dedccd08705beac53be4c43a8da1caad6be667adbf93ed0965/emcee-2.2.1.tar.gz")
    version("2.1.0", sha256="5ce1039a3d78fb9e7d53fcd768517585c5998193743bfcfaac407927d375ca63", url="https://pypi.org/packages/de/00/2358f12c98fa74ab58d78e6a4a4f9a8152fadf6ade2d809d98d771dcc31b/emcee-2.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@3.0-rc2:")
    # END DEPENDENCIES

