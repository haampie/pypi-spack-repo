# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjc(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="976c8f8af49a91195307b3efbc2d63517be63aae2b4b3689dcff4f317669c23a", url="https://pypi.org/packages/b3/6e/e66efbbc291c5272d1241c7943da2fe55471a6c95687082124dab537433a/pyobjc-10.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-addressbook@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-applescriptkit@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-applicationservices@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-automator@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cfnetwork@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreaudio@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreaudiokit@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coredata@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremidi@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreservices@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coretext@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-discrecording@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-discrecordingui@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-diskarbitration@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-dvdplayback@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-exceptionhandling@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-installerplugins@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-iobluetooth@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-iobluetoothui@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-latentsemanticmapping@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-launchservices@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-osakit@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-preferencepanes@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-screensaver@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-searchkit@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-security@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-securityfoundation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-securityinterface@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-syncservices@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-systemconfiguration@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-webkit@10.2:", when="@10.2:")
    # END DEPENDENCIES


        # marker: platform_release >= "10.0"
        # depends_on("py-pyobjc-framework-applescriptobjc@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-corelocation@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-corewlan@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-imagecapturecore@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-iosurface@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-ituneslibrary@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-netfs@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-opendirectory@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-servicemanagement@10.2:", when="@10.2:")

        # marker: platform_release >= "11.0"
        # depends_on("py-pyobjc-framework-avfoundation@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-coremediaio@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-scenekit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-storekit@10.2:", when="@10.2:")

        # marker: platform_release >= "12.0"
        # depends_on("py-pyobjc-framework-accounts@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-audiovideobridging@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-eventkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-gamecenter@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-gamekit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-libdispatch@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-libxpc@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-social@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-videotoolbox@10.2:", when="@10.2:")

        # marker: platform_release >= "13.0"
        # depends_on("py-pyobjc-framework-avkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-gamecontroller@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-mapkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-mediaaccessibility@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-medialibrary@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-mediatoolbox@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-spritekit@10.2:", when="@10.2:")

        # marker: platform_release >= "14.0"
        # depends_on("py-pyobjc-framework-cloudkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-corebluetooth@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-cryptotokenkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-findersync@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-localauthentication@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-multipeerconnectivity@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-notificationcenter@10.2:", when="@10.2:")

        # marker: platform_release >= "15.0"
        # depends_on("py-pyobjc-framework-contacts@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-contactsui@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-gameplaykit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-metalkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-modelio@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-networkextension@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-photos@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-photosui@10.2:", when="@10.2:")

        # marker: platform_release >= "16.0"
        # depends_on("py-pyobjc-framework-intents@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-mediaplayer@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-safariservices@10.2:", when="@10.2:")

        # marker: platform_release >= "17.0"
        # depends_on("py-pyobjc-framework-colorsync@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-coreml@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-corespotlight@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-externalaccessory@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-metalperformanceshaders@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-vision@10.2:", when="@10.2:")

        # marker: platform_release >= "18.0"
        # depends_on("py-pyobjc-framework-adsupport@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-businesschat@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-naturallanguage@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-network@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-usernotifications@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-videosubscriberaccount@10.2:", when="@10.2:")

        # marker: platform_release >= "19.0"
        # depends_on("py-pyobjc-framework-authenticationservices@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-automaticassessmentconfiguration@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-corehaptics@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-coremotion@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-devicecheck@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-executionpolicy@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-fileprovider@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-fileproviderui@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-linkpresentation@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-oslog@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-pencilkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-pushkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-quicklookthumbnailing@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-soundanalysis@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-speech@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-systemextensions@10.2:", when="@10.2:")

        # marker: platform_release >= "20.0"
        # depends_on("py-pyobjc-framework-accessibility@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-adservices@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-apptrackingtransparency@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-callkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-classkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-kernelmanagement@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-metalperformanceshadersgraph@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-mlcompute@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-passkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-replaykit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-screentime@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-uniformtypeidentifiers@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-usernotificationsui@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-virtualization@10.2:", when="@10.2:")

        # marker: platform_release >= "21.0"
        # depends_on("py-pyobjc-framework-datadetection@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-intentsui@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-localauthenticationembeddedui@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-mailkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-metrickit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-phase@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-shazamkit@10.2:", when="@10.2:")

        # marker: platform_release >= "21.4"
        # depends_on("py-pyobjc-framework-screencapturekit@10.2:", when="@10.2:")

        # marker: platform_release >= "22.0"
        # depends_on("py-pyobjc-framework-avrouting@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-backgroundassets@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-extensionkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-healthkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-metalfx@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-safetykit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-sharedwithyou@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-sharedwithyoucore@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-threadnetwork@10.2:", when="@10.2:")

        # marker: platform_release >= "23.0"
        # depends_on("py-pyobjc-framework-cinematic@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-sensitivecontentanalysis@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-symbols@10.2:", when="@10.2:")

        # marker: platform_release >= "23.4"
        # depends_on("py-pyobjc-framework-browserenginekit", when="@10.2:")

        # marker: platform_release >= "9.0"
        # depends_on("py-pyobjc-framework-calendarstore@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-collaboration@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-dictionaryservices@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-fsevents@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-inputmethodkit@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-instantmessage@10.2:", when="@10.2:")
        # depends_on("py-pyobjc-framework-scriptingbridge@10.2:", when="@10.2:")

        # marker: platform_release >= "9.0" and platform_release < "18.0"
        # depends_on("py-pyobjc-framework-pubsub@10.2:", when="@10.2:")
