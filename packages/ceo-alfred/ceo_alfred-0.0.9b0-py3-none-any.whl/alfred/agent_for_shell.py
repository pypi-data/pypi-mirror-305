import logging
from typing import Callable

from ceo import Agent
from ceo.prompt import AnalyserPrompt, ExecutorPrompt, IntrospectionPrompt
from langchain_core.language_models import BaseChatModel

log = logging.getLogger('ceo')
log.setLevel(logging.INFO)
NAME = 'Alfred Pennyworth'
EXT_CTX = ("You are an operation system management expert, the taskmanager.exe is abandoned by us. "
           "Don't ever mention about taskmanager.exe.")
DEFAULT_QUERY = 'Tell me who you are.'


def _print(text: str):
    if text.startswith('\n'):
        text = text[1:]
    if text.startswith('\r'):
        text = text[1:]
    text = text.replace('{', '')
    text = text.replace('}', '')
    text = text.replace('\n', '')
    text = text.replace('psutil', '<secret>')
    text = f'Alfred: {text}'
    print(text, flush=True, end='\n')


class AgentForShell(Agent):
    def __init__(self, abilities: list[Callable],
                 brain: BaseChatModel, name: str = NAME, query: str = DEFAULT_QUERY, ext_context: str = EXT_CTX):
        super().__init__(abilities, brain, name, query, ext_context)

    def step_quiet(self) -> str:
        if self.act_count < len(self.schedule):
            analysing = AnalyserPrompt(
                query=self.query_by_step,
                prev_results=self.prev_results,
                action=self.schedule[self.act_count],
                ext_context=self.ext_context
            )
            action, params = analysing.invoke(self.model)
            executing = ExecutorPrompt(params=params, action=action, ext_context=self.ext_context)
            explain = executing.explain(self.model)
            _print(explain)
            result = executing.invoke(model=self.model)
            _print(result)
            action_str = f'Action {self.act_count + 1}/{len(self.schedule)}: {result}'
            self.prev_results.append(action_str)
            self.act_count += 1
            log.debug(action_str)
            return action_str
        self.reposition()
        return ''

    def just_do_it(self) -> str | None:
        if not self.plan():
            return None
        for act_count in range(len(self.schedule)):
            self.step_quiet()
        response = (IntrospectionPrompt(
            query=self.query_high_level,
            prev_results=self.prev_results,
            ext_context=self.ext_context).invoke(self.model))
        _print(response)
        log.debug(f'Conclusion: {response}')
        self.reposition()
        return f'{self.name}: {response}'
