##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbclient(PythonPackage):
    version("0.10.0", sha256="f13e3529332a1f1f81d82a53210322476a168bb7090a0289c795fe9cc11c9d3f", url="https://pypi.org/packages/66/e8/00517a23d3eeaed0513e718fbc94aab26eaa1758f5690fc8578839791c79/nbclient-0.10.0-py3-none-any.whl")
    version("0.9.1", sha256="2c50a866e8dd6c5f655de47d2e252c82d2ebe978574e760ac229f5950593a434", url="https://pypi.org/packages/ad/41/c3bdff990ded5607321af31e284223eb5fa702e375332fd805f2a9163522/nbclient-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="a3a1ddfb34d4a9d17fc744d655962714a866639acd30130e9be84191cd97cd15", url="https://pypi.org/packages/6b/3a/607149974149f847125c38a62b9ea2b8267eb74823bbf8d8c54ae0212a00/nbclient-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="25e861299e5303a0477568557c4045eccc7a34c17fc08e7959558707b9ebe548", url="https://pypi.org/packages/ac/5a/d670ca51e6c3d98574b9647599821590efcd811d71f58e9c89fc59a17685/nbclient-0.8.0-py3-none-any.whl")
    version("0.7.4", sha256="c817c0768c5ff0d60e468e017613e6eae27b6fa31e43f905addd2d24df60c125", url="https://pypi.org/packages/f3/97/d35da363d1df4a68f1b3d44335f80235487d7ca77d1f606b0c3523118f34/nbclient-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="8fa96f7e36693d5e83408f5e840f113c14a45c279befe609904dbe05dad646d1", url="https://pypi.org/packages/b6/d0/d7a60eb2791e76efe8f88c02431e53e08fa4577d4da7c1599703c685ae61/nbclient-0.7.3-py3-none-any.whl")
    version("0.7.2", sha256="d97ac6257de2794f5397609df754fcbca1a603e94e924eb9b99787c031ae2e7c", url="https://pypi.org/packages/15/49/ea7a0c7e649c54883d76f5119a3e0be592d82a7df1a9b87124fa6663d9c7/nbclient-0.7.2-py3-none-any.whl")
    version("0.7.0", sha256="434c91385cf3e53084185334d675a0d33c615108b391e260915d1aa8e86661b8", url="https://pypi.org/packages/ed/aa/d00b9bdd4623a5e4500baee7f4a37b851dcbb2fa6d90f621d367d1d93420/nbclient-0.7.0-py3-none-any.whl")
    version("0.6.8", sha256="7cce8b415888539180535953f80ea2385cdbb444944cdeb73ffac1556fdbc228", url="https://pypi.org/packages/e6/1d/de31c4139603b3f43147dca571de7d1928bd23d5c674865342bd457ec419/nbclient-0.6.8-py3-none-any.whl")
    version("0.6.7", sha256="d4e32459e7e96783285d1daac92dc2c60ee7b8a82b7cf7d2e55be9d89d7ac463", url="https://pypi.org/packages/ba/bf/e89f683a24dd76ea2eac195035014529f3db6295f5e2a04ede01f27d0d1b/nbclient-0.6.7-py3-none-any.whl")
    version("0.6.6", sha256="09bae4ea2df79fa6bc50aeb8278d8b79d2036792824337fa6eee834afae17312", url="https://pypi.org/packages/68/88/a3f13adcf5708cf0d5f9c4c95e12d1527f6498d87b30d463b588bb466c15/nbclient-0.6.6-py3-none-any.whl")
    version("0.5.13", sha256="47ac905af59379913c1f8f541098d2550153cf8dc58553cbe18c702b181518b0", url="https://pypi.org/packages/db/f7/436bb1add1814911efec4a4a5a358c7559e9b1fd19f4ef89a2a71d707c2b/nbclient-0.5.13-py3-none-any.whl")
    version("0.5.12", sha256="ff2d908024aaabb8864e5392c3517c76e17994b1f9330dda9b5284da9275c499", url="https://pypi.org/packages/e6/e2/dece3c3efa0f8d7ac39b136e288509e6384418105f5d95b448111ab4b83e/nbclient-0.5.12-py3-none-any.whl")
    version("0.5.11", sha256="03e857bea3012377289daa1e1c1651f4fc0295bcd109ccd36a337efcdbebaed7", url="https://pypi.org/packages/ab/e4/0b475cfb00aba0c17cf45ceee2b299f8218076fb32879c75e9bfc93af2e2/nbclient-0.5.11-py3-none-any.whl")
    version("0.5.10", sha256="5b582e21c8b464e6676a9d60acc6871d7fbc3b080f74bef265a9f90411b31f6f", url="https://pypi.org/packages/9a/b0/1cbebe1a3d71bf283c2eaba5c37e9b7e1bee82fb0682fcb8d6bcaecdbcfa/nbclient-0.5.10-py3-none-any.whl")
    version("0.5.9", sha256="8a307be4129cce5f70eb83a57c3edbe45656623c31de54e38bb6fdfbadc428b3", url="https://pypi.org/packages/27/70/69c3561f43ea305da4b360820e67b57244c5308faf1fa890bc444e7cf842/nbclient-0.5.9-py3-none-any.whl")
    version("0.5.8", sha256="e85d4d6280d0a0237c1a6ec7a5e0757cf40a1fcb8c47253516b3a1f87f4ceae8", url="https://pypi.org/packages/4f/81/e7a7e6b3bbbc0d94472b41e0db1308da0504c2c686ab34b3acd3472c0a9a/nbclient-0.5.8-py3-none-any.whl")
    version("0.5.6", sha256="b1ac5a63e3d9fa5eb4b733e136c4416026e2c3ca8bacce3eeac44d7b01905221", url="https://pypi.org/packages/5d/d5/3ec9154da68dd7ec243c051b778bec6bd74a4a66b5bcdd6e0ec8d2f70c1e/nbclient-0.5.6-py3-none-any.whl")
    version("0.5.5", sha256="542b1dfd492bc2524fff52064461149208ac3d53fa6353ce21da2219910b0cfc", url="https://pypi.org/packages/61/f0/693c0d157d2d2af3be700f31225206ac7573790cd0ac8d64cc4e68c66e31/nbclient-0.5.5-py3-none-any.whl")
    version("0.5.4", sha256="95a300c6fbe73721736cf13972a46d8d666f78794b832866ed7197a504269e11", url="https://pypi.org/packages/a7/ed/b764fa931614cb7ed9bebbc42532daecef405d6bef660eeda882f6c23b98/nbclient-0.5.4-py3-none-any.whl")
    version("0.5.3", sha256="e79437364a2376892b3f46bedbf9b444e5396cfb1bc366a472c37b48e9551500", url="https://pypi.org/packages/22/a6/f3a01a5c1a0e72d1d064f33d4cd9c3a782010f48f48f47f256d0b438994a/nbclient-0.5.3-py3-none-any.whl")
    version("0.5.0", sha256="8a6e27ff581cee50895f44c41936ce02369674e85e2ad58643d8d4a6c36771b0", url="https://pypi.org/packages/c3/c0/b8802a7cd2bb7a81a64a580eb65047d2931fd9fea8c038ff3ada2a6bd0ae/nbclient-0.5.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-async-generator", when="@0.2:0.5.3")
        depends_on("py-jupyter-client@6.1.12:", when="@0.7.2:")
        depends_on("py-jupyter-client@6.1.5:", when="@0.4.1:0.7.0")
        depends_on("py-jupyter-core@4.12:4,5.1:", when="@0.7.2:")
        depends_on("py-nbformat@5.1:", when="@0.7.2:")
        depends_on("py-nbformat@5:", when="@:0.7.0")
        depends_on("py-nest-asyncio", when="@0.2:0.7.0")
        depends_on("py-traitlets@5.4:", when="@0.8:")
        depends_on("py-traitlets@5.3:5.3.0.0,5.4:", when="@0.7.2:0.7")
        depends_on("py-traitlets@5.2.2:", when="@0.6.4:0.7.0")
        depends_on("py-traitlets@5.0.0:", when="@0.5.12:0.6.3")
        depends_on("py-traitlets@4.2:", when="@:0.5.11")

