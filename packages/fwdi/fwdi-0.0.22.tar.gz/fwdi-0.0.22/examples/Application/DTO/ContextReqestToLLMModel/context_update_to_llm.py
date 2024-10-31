from pydantic import BaseModel

from Application.DTO.Request.custom_prompt_view_model import CustomPromptViewModel


class UpdateRequestToLLM(BaseModel):

    custom_prompt: CustomPromptViewModel
    source: str
