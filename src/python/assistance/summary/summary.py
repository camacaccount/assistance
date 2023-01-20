# Copyright (C) 2023 Assistance.Chat contributors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import openai

from .config import MODEL_KWARGS, PROMPT


async def summarise(query: str, text: str):
    prompt = PROMPT.format(query=query, text=text)

    completions = await openai.Completion.acreate(prompt=prompt, **MODEL_KWARGS)
    response: str = completions.choices[0].text

    return response
