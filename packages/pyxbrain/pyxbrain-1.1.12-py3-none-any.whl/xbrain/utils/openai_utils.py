from pydantic import Field
from xbrain.utils.config import Config
from pydantic import BaseModel
from openai import OpenAI
import openai

from xbrain.utils.input_util import get_input


system_prompt = """
{prompt_user}
"""


def chat(messages, tools=None, system_prompt="", response_format=None):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    formatted_prompt = system_prompt.format(
        prompt_user=system_prompt
    )
    messages = [{"role": "system", "content": formatted_prompt}] + messages
    response = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        temperature=0.1,
        **({"response_format": response_format} if response_format is not None else {}),
        **({"tools": [openai.pydantic_function_tool(tool) for tool in tools]} if tools is not None else {}),
    )
    message = response.choices[0].message
    return message


# 与用户进行多轮对话，直到没有问题为止
def multiple_rounds_chat(is_complete_description, content_description, question_description, system_prompt, messages=[], tools=None):
    class MultiChatModel(BaseModel):
        is_complete: bool = Field(description=is_complete_description)
        content: str = Field(description=content_description)
        question: str = Field(description=question_description)
    
    if messages:
        messages.append({"role": "user", "content": get_input(messages[0]["content"])})
    
    while True:
        res = chat(messages, tools, system_prompt, MultiChatModel)
        if res.parsed.is_complete:
            return res.parsed.content
        else:
            messages.append({"role": "assistant", "content": res.parsed.content})
            user_input = get_input(res.parsed.question)
            messages.append({"role": "user", "content": user_input})
    


