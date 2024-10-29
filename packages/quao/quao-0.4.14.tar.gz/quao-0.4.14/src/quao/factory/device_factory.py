"""
    QuaO Project device_factory.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from ..enum.provider_tag import ProviderTag
from ..enum.sdk import Sdk
from ..model.device.aws_braket_device import AwsBraketDevice
from ..model.device.ibm_cloud_device import IbmCloudDevice
from ..model.device.ibm_quantum_device import IbmQuantumDevice
from ..model.device.quao_braket_device import QuaoBraketDevice
from ..model.device.quao_qiskit_device import QuaoQiskitDevice
from ..model.device.quao_tytan_device import QuaoTytanDevice
from ..model.device.quao_dwave_device import QuaoDwaveDevice
from ..model.device.quao_cuda_quantum_device import QuaoCudaQuantumDevice
from ..model.device.dwave_system_device import DwaveSystemDevice
from ..model.device.dwave_hybrid_device import DwaveHybridDevice
from ..model.provider.provider import Provider
from ..model.provider.dwave_system_provider import system_devices, hybrid_devices


class DeviceFactory:
    @staticmethod
    def create_device(
        provider: Provider, device_specification: str, authentication: dict, sdk: Sdk
    ):
        """
        @param sdk:
        @param provider:
        @param device_specification:
        @param authentication:
        @return:
        """

        provider_type = ProviderTag.resolve(provider.get_provider_type().value)

        if ProviderTag.QUAO_QUANTUM_SIMULATOR.__eq__(provider_type):
            if Sdk.QISKIT.__eq__(sdk):
                return QuaoQiskitDevice(provider, device_specification)

            if Sdk.BRAKET.__eq__(sdk):
                return QuaoBraketDevice(provider, device_specification)

            if Sdk.TYTAN.__eq__(sdk):
                return QuaoTytanDevice(provider, device_specification)

            if Sdk.D_WAVE_OCEAN.__eq__(sdk):
                return QuaoDwaveDevice(provider, device_specification)

            if Sdk.CUDA_QUANTUM.__eq__(sdk):
                return QuaoCudaQuantumDevice(provider, device_specification)

        if ProviderTag.IBM_QUANTUM.__eq__(provider_type):
            return IbmQuantumDevice(provider, device_specification)

        if ProviderTag.IBM_CLOUD.__eq__(provider_type):
            return IbmCloudDevice(provider, device_specification)

        if ProviderTag.AWS_BRAKET.__eq__(provider_type):
            return AwsBraketDevice(
                provider,
                device_specification,
                authentication.get("bucketName"),
                authentication.get("prefix"),
            )

        if ProviderTag.D_WAVE.__eq__(provider_type):
            if device_specification in system_devices:
                return DwaveSystemDevice(provider, device_specification)

            if device_specification in hybrid_devices:
                return DwaveHybridDevice(provider, device_specification)

        raise Exception("Unsupported device!")
