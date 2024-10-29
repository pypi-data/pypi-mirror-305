from pydantic import Field
from rath.links.file import FileExtraction
from rath.links.dictinglink import DictingLink
from rath.links.auth import AuthTokenLink
from rath.links.split import SplitLink
from fakts_next import Fakts
from herre_next import Herre
from arkitekt_next.service_registry import Params
from arkitekt_next.base_models import Requirement

from mikro_next.mikro_next import MikroNext
from mikro_next.rath import MikroNextLinkComposition, MikroNextRath
from rath.links.split import SplitLink
from fakts_next.contrib.rath.aiohttp import FaktsAIOHttpLink
from fakts_next.contrib.rath.graphql_ws import FaktsGraphQLWSLink
from herre_next.contrib.rath.auth_link import HerreAuthLink
from mikro_next.contrib.fakts.datalayer import FaktsDataLayer
from mikro_next.links.upload import UploadLink
from mikro_next.datalayer import DataLayer
from graphql import OperationType
from herre_next import Herre
from fakts_next import Fakts

from arkitekt_next.base_models import Manifest


def init_services(service_builder_registry):

    try:
        from rekuest_next.links.context import ContextLink
        from rath.links.compose import TypedComposedLink

        class ArkitektMikroNextLinkComposition(TypedComposedLink):
            fileextraction: FileExtraction = Field(default_factory=FileExtraction)
            """ A link that extracts files from the request and follows the graphql multipart request spec"""
            dicting: DictingLink = Field(default_factory=DictingLink)
            """ A link that converts basemodels to dicts"""
            upload: UploadLink
            """ A link that uploads supported data types like numpy arrays and parquet files to the datalayer"""
            auth: AuthTokenLink
            """ A link that adds the auth token to the request"""
            """ A link that splits the request into a http and a websocket request"""
            assignation: ContextLink = Field(default_factory=ContextLink)
            split: SplitLink

    except ImportError:
        ArkitektMikroNextLinkComposition = MikroNextLinkComposition

    class ArkitektMikroNextRath(MikroNextRath):
        link: ArkitektMikroNextLinkComposition

    class ArkitektNextMikroNext(MikroNext):
        rath: ArkitektMikroNextRath
        datalayer: DataLayer

    def builder_mikro(fakts: Fakts, herre: Herre, params: Params, manifest: Manifest):
        datalayer = FaktsDataLayer(fakts_group="datalayer", fakts=fakts)

        return ArkitektNextMikroNext(
            rath=ArkitektMikroNextRath(
                link=ArkitektMikroNextLinkComposition(
                    auth=HerreAuthLink(herre=herre),
                    upload=UploadLink(
                        datalayer=datalayer,
                    ),
                    split=SplitLink(
                        left=FaktsAIOHttpLink(
                            fakts_group="mikro", fakts=fakts, endpoint_url="FAKE_URL"
                        ),
                        right=FaktsGraphQLWSLink(
                            fakts_group="mikro", fakts=fakts, ws_endpoint_url="FAKE_URL"
                        ),
                        split=lambda o: o.node.operation != OperationType.SUBSCRIPTION,
                    ),
                )
            ),
            datalayer=datalayer,
        )

    def fake_builder(fakts, herre, params, manifest):
        return FaktsDataLayer(fakts_group="datalayer", fakts=fakts)

    service_builder_registry.register(
        "mikro",
        builder_mikro,
        Requirement(
            key="mikro",
            service="live.arkitekt.mikro",
            description="An instance of ArkitektNext Mikro to make requests to the user's data",
            optional=True,
        ),
    )
    service_builder_registry.register(
        "datalayer",
        fake_builder,
        Requirement(
            key="datalayer",
            service="live.arkitekt.s3",
            description="An instance of ArkitektNext Datalayer to make requests to the user's data",
            optional=True,
        ),
    )
