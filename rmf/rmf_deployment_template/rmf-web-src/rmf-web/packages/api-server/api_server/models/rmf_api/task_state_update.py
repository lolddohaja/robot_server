# generated by datamodel-codegen:
#   filename:  task_state_update.json

from __future__ import annotations

from pydantic import BaseModel, Field
from typing_extensions import Literal

from . import task_state


class TaskStateUpdate(BaseModel):
    type: Literal["task_state_update"] = Field(
        ..., description="Indicate that this is a task state update"
    )
    data: task_state.TaskState
