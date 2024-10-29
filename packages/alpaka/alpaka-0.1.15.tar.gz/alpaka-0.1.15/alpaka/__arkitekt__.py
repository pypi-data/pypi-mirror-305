from alpaka.alpaka import Alpaka
from herre_next import Herre
from fakts_next import Fakts
from typing import Optional

from arkitekt_next.base_models import Manifest

from arkitekt_next.service_registry import (
    Params,
)
from arkitekt_next.base_models import Requirement


class ArkitektAlpaka(Alpaka):
    endpoint_url: str = "fake_url"
    fakts: Fakts
    herre: Herre

    async def aconnect(self, *args, **kwargs):
        endpoint_url = await self.fakts.get("alpaka.endpoint_url")
        self.endpoint_url = endpoint_url
        await super().aconnect(*args, **kwargs)

    class Config:
        arbitrary_types_allowed = True


def init_services(service_builder_registry):
    def build_arkitekt_next_alpaka(
        fakts: Fakts, herre: Herre, params: Params, manifest: Manifest
    ):
        return ArkitektAlpaka(
            fakts=fakts,
            herre=herre,
        )

    service_builder_registry.register(
        "alpaka",
        build_arkitekt_next_alpaka,
        Requirement(
            key="alpaka",
            service="io.ollama.ollama",
            description="An instance of Ollama to chat with",
        ),
    )
