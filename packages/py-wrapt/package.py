##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWrapt(PythonPackage):
    version("1.16.0", sha256="5f370f952971e7d17c7d1ead40e49f32345a7f7a5373571ef44d800d06b1899d", url="https://pypi.org/packages/95/4c/063a912e20bcef7124e0df97282a8af3ff3e4b603ce84c481d6d7346be0a/wrapt-1.16.0.tar.gz")
    version("1.16.0-rc2", sha256="fbf2264e29f4834eda24438377ba42d7e9571c81e9ff4dd54976a14e3c05dc8e", url="https://pypi.org/packages/cb/97/40c7e8bea26f5a65bc3fef52b304ba62ba1e8260b22832caca03a9dd88c9/wrapt-1.16.0rc2.tar.gz")
    version("1.16.0-rc1", sha256="228533d82158a4d25de8b3703195d5c69bae5860010c75bd01f6ab393561ea22", url="https://pypi.org/packages/40/f8/837a2e44e40b27219eb42245a5c705195393cbb167073d4f8fe0a105f297/wrapt-1.16.0rc1.tar.gz")
    version("1.15.0", sha256="d06730c6aed78cee4126234cf2d071e01b44b915e725a6cb439a879ec9754a3a", url="https://pypi.org/packages/f8/7d/73e4e3cdb2c780e13f9d87dc10488d7566d8fd77f8d68f0e416bfbd144c7/wrapt-1.15.0.tar.gz")
    version("1.15.0-rc1", sha256="42a271aac91a2c74ea6a6b869219cff14404e9362de05c4b83f65dfed7e9b12c", url="https://pypi.org/packages/67/ad/7116586277639eaf1b3504a2739bb3f322146100e2972b92fd314ac46613/wrapt-1.15.0rc1.tar.gz")
    version("1.14.1", sha256="380a85cf89e0e69b7cfbe2ea9f765f004ff419f34194018a6827ac0e3edfed4d", url="https://pypi.org/packages/11/eb/e06e77394d6cf09977d92bff310cb0392930c08a338f99af6066a5a98f92/wrapt-1.14.1.tar.gz")
    version("1.14.0", sha256="8323a43bd9c91f62bb7d4be74cc9ff10090e7ef820e27bfe8815c57e68261311", url="https://pypi.org/packages/c7/b4/3a937c7f8ee4751b38274c8542e02f42ebf3e080f1344c4a2aff6416630e/wrapt-1.14.0.tar.gz")
    version("1.13.3", sha256="1fea9cd438686e6682271d36f3481a9f3636195578bab9ca3382e2f5f01fc185", url="https://pypi.org/packages/eb/f6/d81ccf43ac2a3c80ddb6647653ac8b53ce2d65796029369923be06b815b8/wrapt-1.13.3.tar.gz")
    version("1.13.3-rc2", sha256="9acca689aa840564a1369a3834714a3e336052738c59ff8b942961ab804f4433", url="https://pypi.org/packages/22/71/71c361f462e534187abe3a2a43efb75df17d5e0115f12855f5f8794566d9/wrapt-1.13.3rc2.tar.gz")
    version("1.13.2", sha256="dca56cc5963a5fd7c2aa8607017753f534ee514e09103a6c55d2db70b50e7447", url="https://pypi.org/packages/57/f0/b9c4beb5be22485ff0f09427dcc4e483dbf3a34fd5afb4f93cd6c68b2fac/wrapt-1.13.2.tar.gz")
    version("1.13.1", sha256="909a80ce028821c7ad01bdcaa588126825931d177cdccd00b3545818d4a195ce", url="https://pypi.org/packages/e2/30/dae34ff8afa579098e5796452c414efa4b2738afda40318fdb26e1a8edc1/wrapt-1.13.1.tar.gz")
    version("1.13.0", sha256="4652939e6e19a2c9f197b571d8c066747a1ec20f48b4151f3fd22f4ea058d414", url="https://pypi.org/packages/6d/91/7c6f9475c5a1dbafe2d1cf725a56b1b3438bbc38dd9397cd9cfaa0f3302e/wrapt-1.13.0.tar.gz")
    version("1.12.1", sha256="b62ffa81fb85f4332a4f609cab4ac40709470da05643a082ec1eb88e6d9b97d7", url="https://pypi.org/packages/82/f7/e43cefbe88c5fd371f4cf0cf5eb3feccd07515af9fd6cf7dbf1d1793a797/wrapt-1.12.1.tar.gz")
    version("1.12.0", sha256="0ec40d9fd4ec9f9e3ff9bdd12dbd3535f4085949f4db93025089d7a673ea94e8", url="https://pypi.org/packages/ee/bc/7993faa8084b5a5dbabb07a197ae1b7590da4752dc80455d878573553e2f/wrapt-1.12.0.tar.gz")
    version("1.11.2", sha256="565a021fd19419476b9362b05eeaa094178de64f8361e44468f9e9d7843901e1", url="https://pypi.org/packages/23/84/323c2415280bc4fc880ac5050dddfb3c8062c2552b34c2e512eb4aa68f79/wrapt-1.11.2.tar.gz")
    version("1.11.1", sha256="4aea003270831cceb8a90ff27c4031da6ead7ec1886023b80ce0dfe0adf61533", url="https://pypi.org/packages/67/b2/0f71ca90b0ade7fad27e3d20327c996c6252a2ffe88f50a95bba7434eda9/wrapt-1.11.1.tar.gz")
    version("1.11.0", sha256="e03f19f64d81d0a3099518ca26b04550026f131eced2e76ced7b85c6b8d32128", url="https://pypi.org/packages/78/4d/c3f9bd791683bd61b7799e465872bf5f4495fe3abb6c4f119419b9f606eb/wrapt-1.11.0.tar.gz")
    version("1.10.10", sha256="42160c91b77f1bc64a955890038e02f2f72986c01d462d53cb6cb039b995cdd9", url="https://pypi.org/packages/a3/bb/525e9de0a220060394f4aa34fdf6200853581803d92714ae41fc3556e7d7/wrapt-1.10.10.tar.gz")


