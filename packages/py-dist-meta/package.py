# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDistMeta(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.0", sha256="a01eba9a9a0737e8293d3a7f6750fb7395fc47e96bec59a918912535347360ad", url="https://pypi.org/packages/5c/59/50227daa0c8543094b363bf1c0ea58c8a4877b5d901eb81b4d3f0271dfeb/dist_meta-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="a9ecd103ba88e74f5e1e20f7826a19042a95ed5c21166860cca5eb0998d87fd7", url="https://pypi.org/packages/39/a2/33a03a1277daba1e809eca80cc820302775b349a6e5b8cf41aa61c73d0bb/dist_meta-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="e86c54b8b7157f1478632121aab38dff0f2783abf515ef68c0487d58b245d7f7", url="https://pypi.org/packages/c2/c5/b339bf71a88c457b4de01bb3607b9dc504e8980e6dd5935d5842b522a708/dist_meta-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="28f51bcc6a4c203eef0400eb67562633866229debd1c4bee124e8b02c37194e4", url="https://pypi.org/packages/a3/32/c8a799af5f2985ceefdd86f55da669f5e82cc71932694768fc512932067b/dist_meta-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="d39cef556968af80b85bab00996ce6d67eae8a37232b90dcb7557e3e88e729c4", url="https://pypi.org/packages/6c/04/68fcccb5f09f95d72f06528a3ac8dd94640df0936e986b53ea65c93ea06d/dist_meta-0.4.0-py3-none-any.whl")
    version("0.3.4", sha256="29ec99bd4b4326b226ddd59e0262cb6b4cc2f6f560334bcaf3e4131bb3dc1c3b", url="https://pypi.org/packages/75/1f/51dd1977381cbb6070953d7450b007fe54f0a54b23fccc3e0c7e5cc92213/dist_meta-0.3.4-py3-none-any.whl")
    version("0.3.3", sha256="ee3195af3e5ba2ca69a67c7d7ebbe5250d74eff6848c55379f36295dbac76be4", url="https://pypi.org/packages/0f/95/76bc6746ecec9457eb36fe19033915a449604b44c2b21c31cacc10731622/dist_meta-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="28ba6c9e22a6559f13767d6da16231869cd36596ec138c867b8cb9051690e1b3", url="https://pypi.org/packages/4c/93/02fa51e812f787a21b719ea32e36fd297343431a74730de3ebfed6ddd886/dist_meta-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="c22db809a4b5f64f6d17cd48e311186520889a3942a24b1ed371525c1d56190a", url="https://pypi.org/packages/05/82/c8e64de17aec21e11113ce26fc1deb3d6eabcf700708cb3b9ec5af4a74e0/dist_meta-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="2823105527a1c36f876bab76b108d8f6982ec1a4fcf25beb211e5b6360f5dc95", url="https://pypi.org/packages/6e/4b/b6fcec980d48994d6dac7b98d01667b74b5212a48530a92a6f59b46ca5d4/dist_meta-0.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-domdf-python-tools@3.1:")
        depends_on("py-handy-archives")
        depends_on("py-packaging@20.9:")
    # END DEPENDENCIES

