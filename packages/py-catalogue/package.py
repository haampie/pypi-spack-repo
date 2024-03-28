# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCatalogue(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.10", sha256="58c2de0020aa90f4a2da7dfad161bf7b3b054c86a5f09fcedc0b2b740c109a9f", url="https://pypi.org/packages/9e/96/d32b941a501ab566a16358d68b6eb4e4acc373fab3c3c4d7d9e649f7b4bb/catalogue-2.0.10-py3-none-any.whl")
    version("2.0.9", sha256="5817ce97de17ace366a15eadd4987ac022b28f262006147549cdb3467265dc4d", url="https://pypi.org/packages/45/8f/5b73efc14e0373d9bb0de6ce1ab04a8f77420dc473f1f3ef270caf085cff/catalogue-2.0.9-py3-none-any.whl")
    version("2.0.8", sha256="2d786e229d8d202b4f8a2a059858e45a2331201d831e39746732daa704b99f69", url="https://pypi.org/packages/dc/28/a2b0cc4bfa7916ef9caf08475be5810fc564411c5a801f225a1f40a458c5/catalogue-2.0.8-py3-none-any.whl")
    version("2.0.7", sha256="cab4feda641fe05da1e6a1a9d123b0869d5ca324dcd93d4a5c384408ab62e7fb", url="https://pypi.org/packages/6e/0f/bc9518492efc23f6a36ce6d0c41bebc93e70c198ef40885f24394b6a6c61/catalogue-2.0.7-py3-none-any.whl")
    version("2.0.6", sha256="34ebb5cd2b98f7fa7421fa0eead3b84e577243532509b3fa8cd04abcc9f61d3c", url="https://pypi.org/packages/1f/8b/273bf7d3863570302401991839e1b2c68ae544cc5b02367f58089db872cb/catalogue-2.0.6-py3-none-any.whl")
    version("2.0.5", sha256="fdc6ce61590d5002c9aa4c7eb15e9a17a64adc51654151a197c658619e5b6857", url="https://pypi.org/packages/2b/11/1c6f5ad206d18a9ca4e1b8b4acb8b84d2b3cab5b119b2c5e1d2245bc85a3/catalogue-2.0.5-py3-none-any.whl")
    version("2.0.4", sha256="62572ad1a641face0eb1436921ee4e03169162879bdc25ab8d535219b5f65b48", url="https://pypi.org/packages/9c/10/dbc1203a4b1367c7b02fddf08cb2981d9aa3e688d398f587cea0ab9e3bec/catalogue-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="ea9626fe3dffe2c17c2e8dad9edf689acb08b980babfa96f698687305cc0a194", url="https://pypi.org/packages/82/a5/b5021c74c04cac35a27d34cbf3146d86eb8e173b4491888bc4908c4c8b3b/catalogue-2.0.3-py3-none-any.whl")
    version("2.0.0", sha256="218103923efff9120e4082712015464ef2a594bca18e0a2111c8c038332da502", url="https://pypi.org/packages/e3/8e/9391f722c58dc202cb7980a3a1f0e2499cc91e1fbda2c17632dad1b6e299/catalogue-2.0.0-py3-none-any.whl")
    version("1.0.2", sha256="c9a07ab312f625498a1ea712cd711e1952333c9459c4c674ffc3f05591258334", url="https://pypi.org/packages/fb/8d/7cce983c23fe1bf5f072545853b3c22e2b76e500f2476d968c01757a70c4/catalogue-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="2a7e179511ff4d20713f830cb3da18ade9cd1f2763cd77183bc255ce82015128", url="https://pypi.org/packages/4b/26/dc4a865390e322bdadd33ff5525b628975b7d2b5a652ff220479f0896c64/catalogue-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="584d78e7f4c3c6e2fd498eb56dfc8ef1f4ff738480237de2ccd26cbe2cf47172", url="https://pypi.org/packages/6c/f9/9a5658e2f56932e41eb264941f9a2cb7f3ce41a80cb36b2af6ab78e2f8af/catalogue-1.0.0-py2.py3-none-any.whl")
    version("0.2.1", sha256="25b51f74187ed04f4c327b8c1c3c74d542f30d81ed4bbbd1a4c60893e2b6e916", url="https://pypi.org/packages/d0/9f/6e3588d65274ff2aa157b4781b3d467ae46e581568d93ab03d395e4a1bac/catalogue-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="998329046e952f2e07d606b96e7b2505b40aca1962345398385863781449a69d", url="https://pypi.org/packages/4b/4c/0e0fa8b1e193c1e09a6b72807ff4ca17c78f68f0c0f4459bc8043c66d649/catalogue-0.2.0-py2.py3-none-any.whl")
    version("0.0.8", sha256="98a71a99cc65eb26914fd8a3cc3027354337b870c80e9d3dc32e2c95a34e7df0", url="https://pypi.org/packages/4f/d5/46ff975f0d7d055cf95557b944fd5d29d9dfb37a4341038e070f212b24fe/catalogue-0.0.8-py2.py3-none-any.whl")
    version("0.0.7", sha256="a84b6f86ede2a427561f58f6a26d509149a8ac9763cf5d1703e99c776e7ed72d", url="https://pypi.org/packages/b5/89/69a392cf6901e41319a13293cb21a7020225cb29bb04c55366817fe000ac/catalogue-0.0.7-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

