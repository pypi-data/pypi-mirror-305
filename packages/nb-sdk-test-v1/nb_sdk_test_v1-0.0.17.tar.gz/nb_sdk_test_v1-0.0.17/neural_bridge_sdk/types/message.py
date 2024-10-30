from enum import Enum
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel


class ExecutionResults(str, Enum):
  ERROR = "error"
  STREAM = "stream"
  DISPLAY_IMG_DATA = "display_img_data"
  DISPLAY_HTML_DATA = "display_html_data"
  CODE_RESULT = "code_result"


class CodeBlock(BaseModel):
  type: str = "code_block"
  code: str
  execution_result_type: Optional[ExecutionResults] = None
  execution_result: Optional[str] = None


class TextBlock(BaseModel):
  type: str = "text_block"
  text: str
  reset: Optional[bool] = False


class JsonBlock(BaseModel):
  type: str = "json_block"
  json_data: Dict[str, Any]  # Store JSON data as Dictionary


MessageContent = Union[CodeBlock, TextBlock, JsonBlock]


class Role(str, Enum):
  USER = "user"
  ASSISTANT = "assistant"
  SUMMARIZER = "summarizer"


class Message(BaseModel):
  content: MessageContent
  role: Role


class InvalidContentTypeError(Exception):
  """Exception raised when content is neither CodeBlock nor TextBlock."""

  pass
