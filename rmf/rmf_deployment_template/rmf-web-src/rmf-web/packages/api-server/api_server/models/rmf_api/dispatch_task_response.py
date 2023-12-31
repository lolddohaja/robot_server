# generated by datamodel-codegen:
#   filename:  dispatch_task_response.json

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field
from typing_extensions import Literal

from . import error, task_state


class TaskDispatchResponseItem1(BaseModel):
    success: Optional[Literal[False]] = None
    errors: Optional[List[error.Error]] = Field(
        None, description="Any error messages explaining why the request failed"
    )


class TaskDispatchResponseItem(BaseModel):
    success: Literal[True]
    state: task_state.TaskState


class TaskDispatchResponse(BaseModel):
    __root__: Union[TaskDispatchResponseItem, TaskDispatchResponseItem1] = Field(
        ...,
        description="Response to a task dispatch request",
        title="Task Dispatch Response",
    )
