# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySympy(PythonPackage):
    # BEGIN VERSIONS
    version("1.12", sha256="c3588cd4295d0c0f603d0f2ae780587e64e2efeedb3521e46b9bb1d08d184fa5", url="https://pypi.org/packages/d2/05/e6600db80270777c4a64238a98d442f0fd07cc8915be2a1c16da7f2b9e74/sympy-1.12-py3-none-any.whl")
    version("1.12-rc1", sha256="5faae0c0f5bb83ea2e07a7f72c9881eb451c5da7ccf6f71bd01891c129ae80d7", url="https://pypi.org/packages/48/c8/01feab160a64edcc0741c0c912010728bf4368be4e69c427ac5273e30a70/sympy-1.12rc1-py3-none-any.whl")
    version("1.11.1", sha256="938f984ee2b1e8eae8a07b884c8b7a1146010040fccddc6539c54f401c8f6fcf", url="https://pypi.org/packages/2d/49/a2d03101e2d28ad528968144831d506344418ef1cc04839acdbe185889c2/sympy-1.11.1-py3-none-any.whl")
    version("1.11", sha256="b53069f5f30e4a4690b57cdb8e3d0d9065fff42627239db718214f804e442481", url="https://pypi.org/packages/62/a5/54c15ac18abaf2aad2b017110f5271aeb5cb05f19876b66fb5c907fe1116/sympy-1.11-py3-none-any.whl")
    version("1.11-rc1", sha256="afb88547c8752b403c971c6f268c0418862e8f7aa85ba9ae3f79a34d3e8d80f9", url="https://pypi.org/packages/c7/2c/673478fbf79915fe8e55092cd649a3268b17910f41e9c5880406a5b49fdc/sympy-1.11rc1-py3-none-any.whl")
    version("1.10.1", sha256="df75d738930f6fe9ebe7034e59d56698f29e85f443f743e51e47df0caccc2130", url="https://pypi.org/packages/d0/04/66be21ceb305c66a4b326b0ae44cc4f027a43bc08cac204b48fb45bb3653/sympy-1.10.1-py3-none-any.whl")
    version("1.10", sha256="2009368e862cd29f1b568dc6572786371a2faa1cd8eb4d313e11a90195d6ee36", url="https://pypi.org/packages/cb/14/a012b78f7e3e287d16f63ae91e8c543ff8416a54f74154dc316c83708c74/sympy-1.10-py3-none-any.whl")
    version("1.10-rc3", sha256="9ade6535b7ed6f6a4a87634fd61ecaa1039320e4ee7b0317a0d6db2227b3ceaf", url="https://pypi.org/packages/3c/98/e7a50420b2f47941b8aaebb78a8b09c4ef7fb70bb22128dd41388f414be4/sympy-1.10rc3-py3-none-any.whl")
    version("1.10-rc2", sha256="055d8e5717b21773dd7067810f5efce1a0856d351b47aa08c821c0812607d385", url="https://pypi.org/packages/b9/16/554fa8a97a93752db51e034daae4608e44f84890ffce2c00f2b9d85213bf/sympy-1.10rc2-py3-none-any.whl")
    version("1.10-rc1", sha256="ac5b4122f25cbf22a676a1ef81ca814d6055a77d37bedb38b313d66fca0b4048", url="https://pypi.org/packages/49/10/56b4d919e7bb046389af666cda138ae9bef62dfdfd4fc22cff606d00130c/sympy-1.10rc1-py3-none-any.whl")
    version("1.9", sha256="8bc5de4608b7aa4e7ffd1b25452ae87ccc5f6ca667c661aafb854a1ade337d0c", url="https://pypi.org/packages/78/43/33c5a5e7fbafbf51520f4e09cb0634a1ca1d4cd5469c57967e43183d7a42/sympy-1.9-py3-none-any.whl")
    version("1.8", sha256="3b0b3776e357f789951bb14776c6a841f931680f20d5f8fe55977885657c9b7a", url="https://pypi.org/packages/aa/26/956fece0fc67a6c299557d22158503206d8f14b2e0acc2daf7f06c5f4721/sympy-1.8-py3-none-any.whl")
    version("1.7.1", sha256="c986df98babfb9f5ddea49ba7b69398f6d1cfada5ae0dc0431691cddaff851f6", url="https://pypi.org/packages/ff/69/b16fc81b939d3efdd0b552f2e3e54f7fa1423d0c320cced2e69e675dde26/sympy-1.7.1-py3-none-any.whl")
    version("1.7", sha256="09aa4b3075e505108cb84785ba358e58a53d9596c8c71f07b613958b9150c481", url="https://pypi.org/packages/2f/88/0769eecd7520210e2555d984793e9aa121fdc7b5fd22e9602282726a7818/sympy-1.7-py3-none-any.whl")
    version("1.6.2", sha256="0f6c5724a999eca02f4b453260b0c7151d6fa076313f441274db98bbf97ba8cd", url="https://pypi.org/packages/e0/1f/8cbbf698e853019ac3dc5d60ca8f6be4ace4542b2f05f7b62949617fc98e/sympy-1.6.2-py3-none-any.whl")
    version("1.6.1", sha256="7f50d922bf055560429777447ac827620fd86d39d1de4ea057422e7552c65f3b", url="https://pypi.org/packages/1e/ed/4b0576282597e87e7cf3be33fa4f738d5974471f9b59a55b3730c3877530/sympy-1.6.1-py3-none-any.whl")
    version("1.6", sha256="7af1e11e9fcb72362c47a481dc010e518cfcb60a594d1ee8bd268f86ea7d6cbf", url="https://pypi.org/packages/a4/ea/590e1f2c73a1b8f878a1398b0edbf261d660439a9f851accb39db73d8e2f/sympy-1.6-py3-none-any.whl")
    version("1.5.1", sha256="4880d3a351558063bd89febda302f220dc4b88de393bba81fa6539a3966f03fa", url="https://pypi.org/packages/ce/5b/acc12e3c0d0be685601fc2b2d20ed18dc0bf461380e763afc9d0a548deb0/sympy-1.5.1-py2.py3-none-any.whl")
    version("1.5", sha256="8ae4a95378304ed4081921767fe46f0adf5921bf471c9f5df425abf2c655d751", url="https://pypi.org/packages/4d/a7/25d5d6b3295537ab90bdbcd21e464633fb4a0684dd9a065da404487625bb/sympy-1.5-py2.py3-none-any.whl")
    version("1.4", sha256="f9b00ec76151c98470e84f1da2d7d03633180b71fb318428ddccce1c867d3eaa", url="https://pypi.org/packages/21/21/f4105795ca7f35c541d82c5b06be684dd2f5cb4f508fb487cd7aea4de776/sympy-1.4-py2.py3-none-any.whl")
    version("1.3", sha256="e1319b556207a3758a0efebae14e5e52c648fc1db8975953b05fff12b6871b54", url="https://pypi.org/packages/dd/f6/ed485ff22efdd7b371d0dbbf6d77ad61c3b3b7e0815a83c89cbb38ce35de/sympy-1.3.tar.gz")
    version("1.1.1", sha256="ac5b57691bc43919dcc21167660a57cc51797c28a4301a6144eff07b751216a4", url="https://pypi.org/packages/91/26/4e477dbd1f9260eb743d9f221af3044648a8fb2fcf3f2f23daee4dc831a4/sympy-1.1.1.tar.gz")
    version("1.0", sha256="3eacd210d839e4db911d216a9258a3ac6f936992f66db211e22767983297ffae", url="https://pypi.org/packages/f3/ae/585ca7545c7e8d3a8130cc3d0cf53cfa489c137f8257e743fd3e18d7c401/sympy-1.0.tar.gz")
    version("0.7.6", sha256="dfa3927e9befdfa7da7a18783ccbc2fe489ce4c46aa335a879e49e48fc03d7a7", url="https://pypi.org/packages/09/0d/fcd9536a3640a6399edac53cda5b4efc71bae953161623f59607305efbfc/sympy-0.7.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-mpmath@0.19:", when="@1.4:1.5-beta1,1.5:")
    # END DEPENDENCIES

