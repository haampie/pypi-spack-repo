##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyH5py(PythonPackage):
    version("3.10.0", sha256="d93adc48ceeb33347eb24a634fb787efc7ae4644e6ea4ba733d099605045c049", url="https://pypi.org/packages/37/fc/0b1825077a1c4c79a13984c59997e4b36702962df0bca420698f77b70b10/h5py-3.10.0.tar.gz")
    version("3.9.0", sha256="e604db6521c1e367c6bd7fad239c847f53cc46646f2d2651372d05ae5e95f817", url="https://pypi.org/packages/57/ea/e59bf321fdbfed5ada0b856b3ed1d319733adaebe55aeb132673b5aa8501/h5py-3.9.0.tar.gz")
    version("3.8.0", sha256="6fead82f0c4000cf38d53f9c030780d81bfa0220218aee13b90b7701c937d95f", url="https://pypi.org/packages/69/f4/3172bb63d3c57e24aec42bb93fcf1da4102752701ab5ad10b3ded00d0c5b/h5py-3.8.0.tar.gz")
    version("3.7.0", sha256="3fcf37884383c5da64846ab510190720027dca0768def34dd8dcb659dbe5cbf3", url="https://pypi.org/packages/c5/40/7cf58e6230f0e76699f011c6d293dd47755997709a303a4e644823f3a753/h5py-3.7.0.tar.gz")
    version("3.6.0", sha256="8752d2814a92aba4e2b2a5922d2782d0029102d99caaf3c201a566bc0b40db29", url="https://pypi.org/packages/0a/39/62ec4c1cc96408f6cf27c1d10a26409b98eb6aa2dda7d9c48d204c09b970/h5py-3.6.0.tar.gz")
    version("3.5.0", sha256="77c7be4001ac7d3ed80477de5b6942501d782de1bbe4886597bdfec2a7ab821f", url="https://pypi.org/packages/56/c7/9410b3802f456c702f6e0ccebf82e628f42a30921f61a232e26e424d95d4/h5py-3.5.0.tar.gz")
    version("3.4.0", sha256="ee1c683d91ab010d5e85cb61e8f9e7ee0d8eab545bf3dd50a9618f1d0e8f615e", url="https://pypi.org/packages/7b/c5/d71a944e0637a0db5a0f779c6b757253149fec439a5cafd5fc87e277658b/h5py-3.4.0.tar.gz")
    version("3.3.0", sha256="e0dac887d779929778b3cfd13309a939359cc9e74756fc09af7c527a82797186", url="https://pypi.org/packages/61/0f/e7e57c4b87d027d74acf75e0fc49aff8aca87d6ff7b2e655c183a714044d/h5py-3.3.0.tar.gz")
    version("3.2.1", sha256="89474be911bfcdb34cbf0d98b8ec48b578c27a89fdb1ae4ee7513f1ef8d9249e", url="https://pypi.org/packages/ea/00/d0606cc0d6107a98f75b98367dc42917a67e3a7ec881636835f8e6987e6b/h5py-3.2.1.tar.gz")
    version("3.2.0", sha256="4271c1a4b7d87aa76fe96d016368beb05a6c389d64882d58036964ce7d2d03c1", url="https://pypi.org/packages/b4/1d/3753ec0549ea9f85306a91b714bff2a241c1a73003c141816711db313e2c/h5py-3.2.0.tar.gz")
    version("3.1.0", sha256="1e2516f190652beedcb8c7acfa1c6fa92d99b42331cbef5e5c7ec2d65b0fc3c2", url="https://pypi.org/packages/a7/81/20d5d994c91ed8347efda90d32c396ea28254fd8eb9e071e28ee5700ffd5/h5py-3.1.0.tar.gz")
    version("3.0.0", sha256="7d3803be1b530c68c2955faba726dc0f591079b68941a0c0269b5384a42ab519", url="https://pypi.org/packages/15/fb/86d26128a5ea42d20f402109e76a63e59845d73171887a08a43a28b847dc/h5py-3.0.0.tar.gz")
    version("2.10.0", sha256="84412798925dc870ffd7107f045d7659e60f5d46d1c70c700375248bf6bf512d", url="https://pypi.org/packages/5f/97/a58afbcf40e8abecededd9512978b4e4915374e5b80049af082f49cebe9a/h5py-2.10.0.tar.gz")
    version("2.9.0", sha256="9d41ca62daf36d6b6515ab8765e4c8c4388ee18e2a665701fef2b41563821002", url="https://pypi.org/packages/43/27/a6e7dcb8ae20a4dbf3725321058923fec262b6f7835179d78ccc8d98deec/h5py-2.9.0.tar.gz")
    version("2.8.0", sha256="e626c65a8587921ebc7fb8d31a49addfdd0b9a9aa96315ea484c09803337b955", url="https://pypi.org/packages/74/5d/6f11a5fffc3d8884bb8d6c06abbee0b3d7c8c81bde9819979208ba823a47/h5py-2.8.0.tar.gz")
    version("2.7.1", sha256="180a688311e826ff6ae6d3bda9b5c292b90b28787525ddfcb10a29d5ddcae2cc", url="https://pypi.org/packages/41/7a/6048de44c62fc5e618178ef9888850c3773a9e4be249e5e673ebce0402ff/h5py-2.7.1.tar.gz")
    version("2.7.0", sha256="79254312df2e6154c4928f5e3b22f7a2847b6e5ffb05ddc33e37b16e76d36310", url="https://pypi.org/packages/11/6b/32cee6f59e7a03ab7c60bb250caff63e2d20c33ebca47cf8c28f6a2d085c/h5py-2.7.0.tar.gz")
    version("2.6.0", sha256="b2afc35430d5e4c3435c996e4f4ea2aba1ea5610e2d2f46c9cae9f785e33c435", url="https://pypi.org/packages/22/82/64dada5382a60471f85f16eb7d01cc1a9620aea855cd665609adf6fdbb0d/h5py-2.6.0.tar.gz")
    version("2.5.0", sha256="9833df8a679e108b561670b245bcf9f3a827b10ccb3a5fa1341523852cfac2f6", url="https://pypi.org/packages/6c/03/e3c8c484687466ffcc83e575b997ae6fcdedead573b9522297f53da6e68b/h5py-2.5.0.tar.gz")
    version("2.4.0", sha256="faaeadf4b8ca14c054b7568842e0d12690de7d5d68af4ecce5d7b8fc104d8e60", url="https://pypi.org/packages/84/ad/77e92b47445d5ec5c7e5e8a61196457b47acebc3d7eca166056e7e1291da/h5py-2.4.0.tar.gz")


