# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUproot(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.3.2", sha256="be07a6e852bc63636a7835106a032f191ec698d304ebc7dcb291ee407fb68b2d", url="https://pypi.org/packages/69/08/6dbc179914c7e3438eec018b3cbc6e3dddb2164beef61b9d0b6b876c15f1/uproot-5.3.2-py3-none-any.whl")
    version("5.3.1", sha256="db416b9290f67454cf9d5c99a5b008df4979f2aa1cbb05843c61ba23349fe658", url="https://pypi.org/packages/3b/1a/13102f7461b148382274d4de6017d8c202fc89ef4e187111a86df362997b/uproot-5.3.1-py3-none-any.whl")
    version("5.3.0", sha256="ad89c3a8a51262e803ce8ad352bed0dfd2a0627f764efbe0e3ab2c553dcd7ce7", url="https://pypi.org/packages/87/d0/99811fca5cac80a6839c1e0144eb6dbc33a23cf9e05735781d26bf3383de/uproot-5.3.0-py3-none-any.whl")
    version("5.2.2", sha256="df67149509f89ee0ac38e33238d5f36f342a14e3bcf9d46fe6ec1248bf4825eb", url="https://pypi.org/packages/35/cc/d639e5e939aec01282508fd8dea00347bb1d21f8ae1e810e9d9f45ffb93b/uproot-5.2.2-py3-none-any.whl")
    version("5.2.1", sha256="f09d9fb7c7cb20d3efe2c21046c0cf65db3f1650bec71ea07b85451fd7c2f42e", url="https://pypi.org/packages/cb/6f/04a1d88e7b0770e18057eac17bed91796a8c7e3c2a5d50de8b65601f8020/uproot-5.2.1-py3-none-any.whl")
    version("5.2.0", sha256="3b6739558b38add54b67b317fb39bda52bb1fe57b5adedb602e234242bccdada", url="https://pypi.org/packages/0f/af/a907cca0197ae700eed89e984c3da1e83eb3d8aeb48b02c6a234a9355320/uproot-5.2.0-py3-none-any.whl")
    version("5.1.2", sha256="99d0896ee83f2bed0e7112e8abccf22e7b749c63cf8785ac65a81b7e4d913d68", url="https://pypi.org/packages/ad/c8/1418a0621fbf39d6fef02a8375abb2225e46151d1b0cb278dd076add014c/uproot-5.1.2-py3-none-any.whl")
    version("5.1.1", sha256="6f6e57288c6349d60161bebf9c54ed28668b8d6efd85bfa758da0ff671f9e7b1", url="https://pypi.org/packages/db/7c/c8765183bc551e27f9d602afb372e4cbfea45bc069e9d8cabd051601bf20/uproot-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="e9419ebba73e3b298c6ec2bf579004be8042d4ec5f38dfd3716c61710a342f97", url="https://pypi.org/packages/bd/a6/845eb553ea64393625ac3ae35cc36f99efda24cce72b8c12e3fae2186b03/uproot-5.1.0-py3-none-any.whl")
    version("5.0.13", sha256="055b4b1b827074fffa718194f23759c15573d2de3ea0f0f342b60b27baa9f113", url="https://pypi.org/packages/fb/de/bbfb82eaaacdaf5ed15c766a282304da445d792fe714fa8453b4327962be/uproot-5.0.13-py3-none-any.whl")
    version("5.0.5", sha256="900aad0fd71d4730d5e5d98bbd926d1afabd229756ec63c8959dec57a7a78e88", url="https://pypi.org/packages/ba/ba/9910833d8ece6c5d52613b4bdeece5e2c0df65d384e803a91acd83486a17/uproot-5.0.5-py3-none-any.whl")
    version("5.0.4", sha256="5a4a526fbec5d5bb3c439dcee0876bc689d42a36627a4a89105924afc3b3ec24", url="https://pypi.org/packages/cc/be/000ad141863f38a931fb73d34018a1d9c00884a5dbc263dccd3835bc0ec6/uproot-5.0.4-py3-none-any.whl")
    version("5.0.3", sha256="b826e62ddacc9717045fc95f1ff9b690c683368ece7ee74deba670300c0712bb", url="https://pypi.org/packages/9d/f2/57d054b926de2bafbe702090d4a17da6cd3924f1d8103b120f291fc2556c/uproot-5.0.3-py3-none-any.whl")
    version("5.0.2", sha256="5c74fc126ec6aa76488466e345e0e51efb51239c66e32f31fbdf534e21bad030", url="https://pypi.org/packages/50/ce/343326e18b2c809fc4553ba707312fba394305fd3e1e69bcedd8a30653f5/uproot-5.0.2-py3-none-any.whl")
    version("5.0.1", sha256="ceefab14d57942cee11dd43b02503291097f725fca2677d8da4cfb2383cc5a89", url="https://pypi.org/packages/dd/ba/59d44c1d4b41707b5fd1658945ca34bd845c40a8ba4bb1dd6d6dc6484417/uproot-5.0.1-py3-none-any.whl")
    version("5.0.0", sha256="722a341b84e0d84a105425d147cc91256c7c80747564a42f24ce9778f18adad7", url="https://pypi.org/packages/c0/75/1182d0cb43e48d437359a3584546a995537e772d5df8dab159674f96d3da/uproot-5.0.0-py3-none-any.whl")
    version("4.3.7", sha256="7b55df2b5b8c0db9d4d4e4bdb7161e29215a0fbd39087971b657514d0c67d4c2", url="https://pypi.org/packages/fa/2f/c4b3dbc0c3b6cdce29e66f5bea5d920c064d699c1d1dd2ecb27fcb8b5d47/uproot-4.3.7-py3-none-any.whl")
    version("4.3.6", sha256="780049013204481eb89d7db61169a3bf306d0fd7c8f22c79aa895e24ca68a3b8", url="https://pypi.org/packages/81/f9/ba105299f43f9544574f7bc4ccb1f09bc87d252e71103290097f11175788/uproot-4.3.6-py3-none-any.whl")
    version("4.3.5", sha256="940300d6b700f719ae90bfebc00a8deada3cfe43010cd2258ef6ab35e637319d", url="https://pypi.org/packages/be/3e/50da9b92af3efd7026da13406ae7ee859cd0e04bae680763e81b277e8079/uproot-4.3.5-py3-none-any.whl")
    version("4.3.4", sha256="87ebc97e86854e2adcc12fa29a274e5b4e6ce7c3f1fc2784f7aeccceb57a30a3", url="https://pypi.org/packages/12/30/7193f4e029c3be48ec70cdbba8edd8ea911d2a0a329024be05d33c3f4bfd/uproot-4.3.4-py2.py3-none-any.whl")
    version("4.3.3", sha256="7502807920d8c3e4c8d1c1ffe540c90152398ba45e0f3e508875b32ae9892332", url="https://pypi.org/packages/0a/12/5186335f38074dde8a1157834118c54809d45fef23a81e79afa3e2f7607b/uproot-4.3.3-py2.py3-none-any.whl")
    version("4.3.2", sha256="9c6abda4c2d8b4f14de10d91c19692bc5830ebe70ca257811adc052746782dca", url="https://pypi.org/packages/73/6f/ee5cf3b4b3859c4106f5bbde6eb64452800917c564af3c3d34efbca6d7ee/uproot-4.3.2-py2.py3-none-any.whl")
    version("4.3.1", sha256="23bef36caa0dcad5d1273c5359a11323a01bdc710adb953371291cc7fc73b62b", url="https://pypi.org/packages/d5/09/38f19efe9a465f2ae7317c62ca039aeecf91278f280c65c10c9cec808333/uproot-4.3.1-py2.py3-none-any.whl")
    version("4.3.0", sha256="d7f82480e812805444ffd0f3ec44934d3b10a547ea5c1c489153634d905f1343", url="https://pypi.org/packages/b5/73/a2cbb91cccb77ea7f346224f54425bd5abcd4929fc971ac02ea8300a101c/uproot-4.3.0-py2.py3-none-any.whl")
    version("4.2.4", sha256="3da12232e5247292826fb4de6cc0464f83fb931311977591ec26d8b58025031d", url="https://pypi.org/packages/34/44/428527157bcee4bbde363505a60d19d9af2f46da31d0e9e960f5118ce000/uproot-4.2.4-py2.py3-none-any.whl")
    version("4.2.3", sha256="2f7ad4057ae11319c44111c0feaa90b51d1ac132cf17f0bd7d82b78525d3b4ac", url="https://pypi.org/packages/3e/48/7c459ffc8996ff83cd6442657356e345456df46edbf63b93a4359931384b/uproot-4.2.3-py2.py3-none-any.whl")
    version("4.2.2", sha256="39df5c4e501ba924c7ba12a9bf9ef91e332a593a422f0dbdde1c774ee5920ef8", url="https://pypi.org/packages/2d/0a/f191041e74fc05783fca8d3d4fd6d2a2af32132e10653e2a86ed7404e539/uproot-4.2.2-py2.py3-none-any.whl")
    version("4.1.8", sha256="cced42c62cf080728df8ac07cadedd845f6af9ae885fb06398d331cc945bd2ff", url="https://pypi.org/packages/da/ec/62916a8b4001a56d11bc888e54ed21b1fcc193d61cef84ecf5bf4d98e109/uproot-4.1.8-py2.py3-none-any.whl")
    version("4.0.11", sha256="c0b6111b2034211eba2d8ecce5502ed35bfd395b45eabed20ec6c20d21437c41", url="https://pypi.org/packages/b8/0b/27399201b0b5c049f339d0263de96079b18b7ef82a1afdb436406a8472aa/uproot-4.0.11-py2.py3-none-any.whl")
    version("4.0.10", sha256="01694bb3e31ac66029467a75b857c9c96c2f71314d50d876fe199f980815e823", url="https://pypi.org/packages/64/29/509d02ac708979f6982c199d65faefb76dc6a500a65eef8703633b0dd51c/uproot-4.0.10-py2.py3-none-any.whl")
    version("4.0.9", sha256="8e7df52f2edfdb373e440bc28b564c79776f1fe1d819b2753df3a01f8c00533d", url="https://pypi.org/packages/9c/1c/10b9a9ff56c2d48fd3e050ccceffefb763dffd8eb3efb9beb9082dced8f7/uproot-4.0.9-py2.py3-none-any.whl")
    version("4.0.8", sha256="ff590a7a142441c244532944c5c501890862899e83eb0f1d41f2c47c59c84d73", url="https://pypi.org/packages/a5/99/bf1b3995f9cafad30c8df34a99ab286f522cf762a2eb2152ac47609be04e/uproot-4.0.8-py2.py3-none-any.whl")
    version("4.0.7", sha256="7fbe065eb75f271819542df691499518ecc56caaa8e0166876d3d13be5bf08b3", url="https://pypi.org/packages/73/85/06dda0d02fa68f726d49eacce836eb501c1dfde33fe1162ee80358f4ca6b/uproot-4.0.7-py2.py3-none-any.whl")
    version("4.0.6", sha256="03988d9d7eee951182eb483884f68715a1c6d5c37b0f5918c020dea99f109203", url="https://pypi.org/packages/ae/01/efb4100d671aec20b3f04c289dfe19d0930e534de538ee8f748e72f783d6/uproot-4.0.6-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("lz4", default=False)
    variant("xrootd", default=False)
    variant("zstd", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-awkward@2.4.6:", when="@5.1.0-rc4:")
        depends_on("py-awkward@2.0.0:", when="@5.0.0:5.1.0-rc1")
        depends_on("py-cramjam@2.5:", when="@5.3.1:")
        depends_on("py-cramjam@2.8.1:2.8.1.0,2.8.2:", when="@5.3:5.3.0")
        depends_on("py-fsspec", when="@5.2:")
        depends_on("py-fsspec-xrootd", when="@5.3.2-rc1:+xrootd")
        depends_on("py-lz4", when="@3:3.2")
        depends_on("py-numpy", when="@2.9.9:2,4:")
        depends_on("py-packaging", when="@5.0.0-rc2:")
        depends_on("py-setuptools", when="@4.0.8:5.0.0-rc1")
        depends_on("py-typing-extensions@4.1:", when="@5.1: ^python@:3.10")
    # END DEPENDENCIES

