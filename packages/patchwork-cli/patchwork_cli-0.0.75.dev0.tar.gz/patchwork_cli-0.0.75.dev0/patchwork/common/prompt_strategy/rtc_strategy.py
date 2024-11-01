from patchwork.common.client.llm.protocol import LlmClient


class RtcStrategy(LlmClient):
    def __init__(self, client: LlmClient):
        pass

    def get_prompt(self):
        return self.prompt

    def get_prompt_type(self):
        return "RTC"
