# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPywinpty(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.13", sha256="c34e32351a3313ddd0d7da23d27f835c860d32fe4ac814d372a3ea9594f41dde", url="https://pypi.org/packages/33/d9/93956af389ab7d4ef2f558b1cc6c5cb48885d254ac882f212964c30a1e4f/pywinpty-2.0.13.tar.gz")
    version("2.0.12", sha256="8197de460ae8ebb7f5d1701dfa1b5df45b157bb832e92acba316305e18ca00dd", url="https://pypi.org/packages/7d/d3/f10b259284324bdad0bf38c1c8041344620b3f2ea603f2d59e63ca83ed5d/pywinpty-2.0.12.tar.gz")
    version("2.0.11", sha256="e244cffe29a894876e2cd251306efd0d8d64abd5ada0a46150a4a71c0b9ad5c5", url="https://pypi.org/packages/86/ab/4b8c722b772fd5edb5f50434a565ca892c8b4b0d24f13beec05fa3ac3900/pywinpty-2.0.11.tar.gz")
    version("2.0.10", sha256="cdbb5694cf8c7242c2ecfaca35c545d31fa5d5814c3d67a4e628f803f680ebea", url="https://pypi.org/packages/d3/89/2b9113eabacfe3bbebcdf95c24772e2267c7b6b9fed6e35bffba2080a4c1/pywinpty-2.0.10.tar.gz")
    version("2.0.9", sha256="01b6400dd79212f50a2f01af1c65b781290ff39610853db99bf03962eb9a615f", url="https://pypi.org/packages/22/77/59645ee028f410ef1d582fc2923d2cb61016ed38e6ae5022f405227ca2ad/pywinpty-2.0.9.tar.gz")
    version("2.0.8", sha256="a89b9021c63ef78b1e7d8e14f0fac4748c88a0c2e4f529c84f37f6e72b914280", url="https://pypi.org/packages/96/18/904410ebeff904b0039bb918e2529e8f72dd34048bf1a719abcffefc0151/pywinpty-2.0.8.tar.gz")
    version("2.0.7", sha256="f52b2e51c46dac40708ede1d42577f3ddb9d7cf8acaa36c8e27b3d3b975f4c95", url="https://pypi.org/packages/a0/e2/3760a999d2d3f35d37164793f8f961d25d29136356517173fdf108ae34fe/pywinpty-2.0.7.tar.gz")
    version("2.0.6", sha256="a91a77d23f29a58b44f62a9474a31ed67df1277cddb69665275f8d22429046ac", url="https://pypi.org/packages/2e/a6/50815a4aeff3946c5723bcf3363980f98461fa01b8fa125c41fbe852540a/pywinpty-2.0.6.tar.gz")
    version("2.0.5", sha256="e125d3f1804d8804952b13e33604ad2ca8b9b2cac92b27b521c005d1604794f8", url="https://pypi.org/packages/02/29/27d6ab0b1566db75cce1fde817cb2cf327066fc545c08ceb4e61a77a07de/pywinpty-2.0.5.tar.gz")
    version("2.0.4", sha256="a5002c74afc1ddcc85fca25de58ce9cef1a22957582981418c81aaee218675ad", url="https://pypi.org/packages/b2/44/c4b593af3c5e54bfb191f5fcb7232ec66d945a1ef632bbef4befacd50047/pywinpty-2.0.4.tar.gz")
    version("1.1.6", sha256="8808f07350c709119cc4464144d6e749637f98e15acc1e5d3c37db1953d2eebc", url="https://pypi.org/packages/3d/1d/b884c586cb4ff53da97f9c9e177dd73e74a5d848e2954492341f118413fc/pywinpty-1.1.6.tar.gz")
    version("1.1.5", sha256="92125f0f8e4e64bb5f3bf270a182c9206dc1765542c59bc07441908a9db17504", url="https://pypi.org/packages/01/c1/c6c7bf4851d78d71c1859e124626cf53d48638f3907ca80731579382a1b3/pywinpty-1.1.5.tar.gz")
    version("1.1.4", sha256="cc700c9d5a9fcebf677ac93a4943ca9a24db6e2f11a5f0e7e8e226184c5036f7", url="https://pypi.org/packages/1f/86/8c320359c04a85084f416bc01e265d09384655c5643953c0eaea2c5c7636/pywinpty-1.1.4.tar.gz")
    version("1.1.3", sha256="3a1d57b338390333812a5eed31c93c7d8ba82b131078063703e731946d90c9f2", url="https://pypi.org/packages/07/e0/a26c9ac4e16aefc0b66a203f0140373245b6298443fa35978a3c680c8726/pywinpty-1.1.3.tar.gz")
    version("1.1.2", sha256="f1718838e1c7c700e5f0b79d5d5e05243ff583313ff88e47bb94318ba303e565", url="https://pypi.org/packages/fb/dc/06ed1e684dfba3929a985f1845eb86f8480f0418293fc9402526e4b8bf10/pywinpty-1.1.2.tar.gz")
    version("1.1.1", sha256="4a3ffa2444daf15c5f65a76b5b2864447cc915564e41e2876816b9e4fe849070", url="https://pypi.org/packages/40/ed/694e4a642e3b8afac6d6e70538a3684e1049f2020a33002b58e1ac5cd4b3/pywinpty-1.1.1.tar.gz")
    version("1.1.0", sha256="f60ed4947fe0841e7d7cafae4885a0040d4994a4647dd21be4ed4266789885c9", url="https://pypi.org/packages/46/02/aeb98dc7ac48e3fc6ba13159be5c6fbd0d19e2d11edf996e96d031fa86ca/pywinpty-1.1.0.tar.gz")
    version("1.0.1", sha256="b3512d4a964a0abae1b77b6908917c62ea0ad7d8178696e4e973877fe9e820f9", url="https://pypi.org/packages/b0/2c/11676105f51a7718316cd74186630f4a4cb0efa3530ebf3cfbe0b72e35cb/pywinpty-1.0.1.tar.gz")
    version("1.0.0", sha256="76a8c1794eb9fe46081d78133960d72fd938fe1c86f78849173be6e52ce05bd9", url="https://pypi.org/packages/98/c1/e0881333c3ef6394f969842676a953ecbb83e41d9a83c2f240b043023665/pywinpty-1.0.0.tar.gz")
    version("0.5.7", sha256="2d7e9c881638a72ffdca3f5417dd1563b60f603e1b43e5895674c2a1b01f95a0", url="https://pypi.org/packages/5d/97/8e43c2152a638cdb83d45644eb125c752abe67249f94bb3e3e29b0709685/pywinpty-0.5.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

