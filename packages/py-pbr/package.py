##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPbr(PythonPackage):
    version("6.0.0", sha256="4a7317d5e3b17a3dccb6a8cfe67dab65b20551404c52c8ed41279fa4f0cb4cda", url="https://pypi.org/packages/64/dd/171c9fb653591cf265bcc89c436eec75c9bde3dec921cc236fa71e5698df/pbr-6.0.0-py2.py3-none-any.whl")
    version("5.11.1", sha256="567f09558bae2b3ab53cb3c1e2e33e726ff3338e7bae3db5dc954b3a44eef12b", url="https://pypi.org/packages/01/06/4ab11bf70db5a60689fc521b636849c8593eb67a2c6bdf73a16c72d16a12/pbr-5.11.1-py2.py3-none-any.whl")
    version("5.11.0", sha256="db2317ff07c84c4c63648c9064a79fe9d9f5c7ce85a9099d4b6258b3db83225a", url="https://pypi.org/packages/e5/37/10e8a53f196cf0bcb93008daed42e2c47c7876430a7efd044ff4d647f30a/pbr-5.11.0-py2.py3-none-any.whl")
    version("5.10.0", sha256="da3e18aac0a3c003e9eea1a81bd23e5a3a75d745670dcf736317b7d966887fdf", url="https://pypi.org/packages/88/fb/c7958b2d571c7b15091b8574a727ad14328e8de590644198e57de9b5ee57/pbr-5.10.0-py2.py3-none-any.whl")
    version("5.9.0", sha256="e547125940bcc052856ded43be8e101f63828c2d94239ffbe2b327ba3d5ccf0a", url="https://pypi.org/packages/1b/ef/0621aa0e422dda72dc89b61972e5a28d5a947c22fdff83a5d69fdbc1949a/pbr-5.9.0-py2.py3-none-any.whl")
    version("5.8.1", sha256="27108648368782d07bbf1cb468ad2e2eeef29086affd14087a6d04b7de8af4ec", url="https://pypi.org/packages/5a/f0/28b2d5398ed905ce67045670e076c8dfa23ea54c19f2a8e3ac36e8153e1d/pbr-5.8.1-py2.py3-none-any.whl")
    version("5.8.0", sha256="176e8560eaf61e127817ef93d8a844803abb27a4d4637f0ff3bb783129be2e0a", url="https://pypi.org/packages/73/c3/d45171501210b0305f4c93fafe50950f0c2228e87034ceb51744bd03ff08/pbr-5.8.0-py2.py3-none-any.whl")
    version("5.7.0", sha256="60002958e459b195e8dbe61bf22bcf344eedf1b4e03a321a5414feb15566100c", url="https://pypi.org/packages/58/4e/98f141d6edcb41b4dd50bb2b70f072dcd4facb6f96685c2fca1f647d71f5/pbr-5.7.0-py2.py3-none-any.whl")
    version("5.6.0", sha256="c68c661ac5cc81058ac94247278eeda6d2e6aecb3e227b0387c30d277e7ef8d4", url="https://pypi.org/packages/18/e0/1d4702dd81121d04a477c272d47ee5b6bc970d1a0990b11befa275c55cf2/pbr-5.6.0-py2.py3-none-any.whl")
    version("5.5.1", sha256="b236cde0ac9a6aedd5e3c34517b423cd4fd97ef723849da6b0d2231142d89c00", url="https://pypi.org/packages/fb/48/69046506f6ac61c1eaa9a0d42d22d54673b69e176d30ca98e3f61513e980/pbr-5.5.1-py2.py3-none-any.whl")
    version("5.4.3", sha256="b32c8ccaac7b1a20c0ce00ce317642e6cf231cf038f9875e0280e28af5bf7ac9", url="https://pypi.org/packages/46/a4/d5c83831a3452713e4b4f126149bc4fbda170f7cb16a86a00ce57ce0e9ad/pbr-5.4.3-py2.py3-none-any.whl")
    version("5.2.1", sha256="0ce920b865091450bbcd452b35cf6d6eb8a6d9ce13ad2210d6e77557f85cf32b", url="https://pypi.org/packages/49/a2/e641de6c7e559e0a03a8d3c7b42199158b17a8cf2f96e11e7f725c2e730d/pbr-5.2.1-py2.py3-none-any.whl")
    version("3.1.1", sha256="60c25b7dfd054ef9bb0ae327af949dd4676aa09ac3a9471cdc871d8a9213f9ac", url="https://pypi.org/packages/0c/5d/b077dbf309993d52c1d71e6bf6fe443a8029ea215135ebbe0b1b10e7aefc/pbr-3.1.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="d9b69a26a5cb4e3898eb3c5cea54d2ab3332382167f04e30db5e1f54e1945e45", url="https://pypi.org/packages/e9/c0/8f7f54d7b9b8ceb73ac30d769fdd722431e95ad0d2cd689def382e8b9eec/pbr-2.0.0-py2.py3-none-any.whl")
    version("1.10.0", sha256="f5cf7265a80636ecff66806d13494cbf9d77a3758a65fd8b4d4d4bee81b0c375", url="https://pypi.org/packages/b8/a1/7abb01fd93d66fc71e24e5df9ca6d7d9acfb4b715937d2a38fd739f266e6/pbr-1.10.0-py2.py3-none-any.whl")
    version("1.8.1", sha256="46c8db75ae75a056bd1cc07fa21734fe2e603d11a07833ecc1eeb74c35c72e0c", url="https://pypi.org/packages/fc/37/94af8387babb09796d306b18cf94ee5c70388c875a16d8a88e471500452c/pbr-1.8.1-py2.py3-none-any.whl")
    version("0.11.1", sha256="192d775764cc87013ed4ce92382054a2317f1d2782197a0fe3cd1b00f0e40c02", url="https://pypi.org/packages/a8/87/23e26858c1a45ff7ed352261e34fb99b33a97bfac0a6e5ece8df7c983d02/pbr-0.11.1-py2.py3-none-any.whl")
    version("0.11.0", sha256="ba3f3c6313ccc8c22e73d6fbd94aff2a9e0a57e7cb9c5e9ac6e953a29d5c008b", url="https://pypi.org/packages/d4/26/8777b9e756b22295375946cb83ee588e8c10e6e2bed73e5f29c218c141c8/pbr-0.11.0-py2.py3-none-any.whl")
    version("0.10.8", sha256="ff5d4975ac02c072d4d338fda3bbd1fd1ea430a23e11bf5e1c53a579c2e5856b", url="https://pypi.org/packages/9c/b1/ca2d79e0d7a8745a3e4fbe396be26aa7ce6d02891af689474be93c25dcc1/pbr-0.10.8-py2.py3-none-any.whl")
    version("0.10.7", sha256="93cd0caba57c2c97ae4bf3e76cc80413a727be529cee38c4e196a6d690eb9109", url="https://pypi.org/packages/c1/ce/f8a51cbccd7e4bccb972464463a8bb139a35cf0c9d4998f4548292abc59d/pbr-0.10.7-py2.py3-none-any.whl")
    version("0.10.6", sha256="d5c4357467bf6cc6d1fbae3d726381ff4315664a11f0485150dc93b77fe5c150", url="https://pypi.org/packages/33/e0/b950dc6f07f174b70be856f1666236b60902c340e042d0a04dbd2529c086/pbr-0.10.6-py2.py3-none-any.whl")
    version("0.10.5", sha256="f563eb1ef0595d415b46becb8335893ae1d392ef5d5dc7571e27d836dae1372c", url="https://pypi.org/packages/bf/4d/6c52208dcbd56bb27921b631bcb689143bf4177700f06ee5c02281581788/pbr-0.10.5-py2.py3-none-any.whl")
    version("0.10.4", sha256="27b6aeae83f95e5cd52c0952b46c265333baf5622cff1743135f0d81382e0495", url="https://pypi.org/packages/55/93/92c38d86ad190cf3ab9903614869ef6649e660e5f01622a3b111ff0f8bf4/pbr-0.10.4-py2.py3-none-any.whl")
    version("0.10.3", sha256="87d67997a3d6570f6688aa4e938699439efae17abc452d4572442168043870f1", url="https://pypi.org/packages/d2/78/c6824d6fec5169cca21295093b42d1c609a54d21a18c953cf7f16dfaf1f5/pbr-0.10.3-py2.py3-none-any.whl")
    version("0.10.2", sha256="22c3f4a8c91dc2d2e99271d662b72cfeb90ec436ca0553ece620ae8576096a2b", url="https://pypi.org/packages/c2/39/653746d50ebd66a8784c5469e439e73b717f48fa463165d7c734d25a2de6/pbr-0.10.2-py2.py3-none-any.whl")
    version("0.10.1", sha256="64a051044009f18da4a5ed8faefe8eb9540cab8d3431b9b6d510d877c4b36a82", url="https://pypi.org/packages/db/20/4b2c63698053d5a03e2f1d5cf39735a890901a97fff513adfc7e7bd0729a/pbr-0.10.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pip", when="@0.10.1:0")

