# generated by datamodel-codegen:
#   filename:  fleet_state_update.json

from __future__ import annotations

from pydantic import BaseModel, Field
from typing_extensions import Literal

from . import fleet_state


class FleetStateUpdate(BaseModel):
    type: Literal["fleet_state_update"] = Field(
        ..., description="Indicate that this is a fleet state update"
    )
    data: fleet_state.FleetState
