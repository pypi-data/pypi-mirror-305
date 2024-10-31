from pydantic import BaseModel

from Application.DTO.Request.custom_prompt_view_model import CustomPromptViewModel


class UpdateRequestToLLM(BaseModel):

        username: str
        password: str
        project: str
        custom_prompt: CustomPromptViewModel
        source: str
