"""Models for ArkitektNext. Thiese include extensiosn for the Fakts Manifest and the User model."""

from hashlib import sha256
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class Requirement(BaseModel):
    key: str
    service: str
    """ The service is the service that will be used to fill the key, it will be used to find the correct instance. It needs to fullfill
    the reverse domain naming scheme"""
    optional: bool = False
    """ The optional flag indicates if the requirement is optional or not. Users should be able to use the client even if the requirement is not met. """
    description: Optional[str] = None
    """ The description is a human readable description of the requirement. Will be show to the user when asking for the requirement."""


def build_default_requirements() -> List[Requirement]:
    return [
        Requirement(
            key="lok",
            service="live.arkitekt_next.lok",
            description="An instance of ArkitektNext Lok to authenticate the user",
        ),
        Requirement(
            key="rekuest",
            service="live.arkitekt_next.rekuest",
            description="An instance of ArkitektNext Rekuest to assign to nodes",
        ),
        Requirement(
            key="kabinet",
            service="live.arkitekt_next.kabinet",
            description="An instance of ArkitektNext Kabinet to retrieve nodes from",
        ),
        Requirement(
            key="mikro",
            service="live.arkitekt_next.mikro",
            description="An instance of ArkitektNext Mikro to make requests to the user's data",
            optional=True,
        ),
        Requirement(
            key="fluss",
            service="live.arkitekt_next.fluss",
            description="An instance of ArkitektNext Fluss to make requests to the user's data",
            optional=False,
        ),
        Requirement(
            key="port",
            service="live.arkitekt_next.port",
            description="An instance of ArkitektNext Fluss to make requests to the user's data",
            optional=True,
        ),
        Requirement(
            key="datalayer",
            service="live.arkitekt_next.datalayer",
            description="An instance of ArkitektNext Datalayer to make requests to the user's data",
            optional=False,
        ),
    ]


class Manifest(BaseModel):
    """A manifest for an app that can be installed in ArkitektNext

    Manifests are used to describe apps that can be installed in ArkitektNext.
    They provide information about the app, such as the
    its globally unique identifier, the version, the scopes it needs, etc.

    This Manifest is send to the Fakts server on initial app configuration,
    and is used to register the app with the Fakts server, which in turn
    will prompt the user to grant the app access to establish itself as
    an ArkitektNext app (and therefore as an OAuth2 client) (see more in the
    Fakts documentation).

    """

    version: str
    """ The version of the app TODO: Should this be a semver? """
    identifier: str
    """ The globally unique identifier of the app: TODO: Should we check for a reverse domain name? """
    scopes: List[str]
    """ Scopes that this app should request from the user """
    logo: Optional[str]
    """ A URL to the logo of the app TODO: We should enforce this to be a http URL as local paths won't work """
    requirements: Optional[List[Requirement]] = Field(
        default_factory=build_default_requirements
    )
    """ Requirements that this app has TODO: What are the requirements? """

    class Config:
        extra = "forbid"

    def hash(self):
        """Hash the manifest"""
        return sha256(self.model_dump_json().encode()).hexdigest()
    

    @field_validator("identifier")
    def check_identifier(cls, v):
        assert "/" not in v, "The identifier should not contain a /"
        assert len(v) > 0, "The identifier should not be empty"
        assert len(v) < 256, "The identifier should not be longer than 256 characters"
        return v


class User(BaseModel):
    """A user of ArkitektNext

    This model represents a user on ArkitektNext. As herre_next is acgnostic to the
    user model, we need to provide a model that can be used to represent
    the ArkitektNext user. This model is used by the
    :class:`herre_next.fakts.fakts_endpoint_fetcher.FaktsUserFetcher` to
    fetch the user from the associated ArkitektNext Lok instance. This model
    is closely mimicking the OIDC user model, and is therefore compatible
    to represent OIDC users.

    """

    id: str = Field(alias="sub")
    """ The user's id (in lok, this is the user's sub(ject) ID)"""

    username: str = Field(alias="preferred_username")
    """ The user's preferred username """
    email: str = Field(alias="email")
    """ The user's preferred username """
