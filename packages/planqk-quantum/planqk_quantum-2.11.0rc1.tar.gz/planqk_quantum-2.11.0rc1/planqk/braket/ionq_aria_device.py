import json

from braket.device_schema.ionq import IonqDeviceCapabilities
from planqk.braket.device_factory import DeviceFactory
from planqk.braket.gate_based_device import PlanqkAwsGateBasedDevice


@DeviceFactory.register_device("aws.ionq.aria")
@DeviceFactory.register_device("aws.ionq.aria-2")
class PlanqkAwsIonqAriaDevice(PlanqkAwsGateBasedDevice):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def properties(self) -> IonqDeviceCapabilities:
        """IonqDeviceCapabilities: Return the device properties"""
        config = self._get_backend_config()
        return IonqDeviceCapabilities.parse_raw(json.dumps(config))

    @property
    def name(self) -> str:
        return "Ionq"

    @property
    def provider_name(self) -> str:
        return "Aria"
