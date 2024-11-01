import openai
# from dotenv import load_dotenv
from ceo import get_openai_model

from alfred.agent_for_shell import AgentForShell
from process_manager.action import (
    find_all_processes,
    find_process_by_name,
    find_top_k_processes_with_the_highest_cpu_usage,
    find_top_k_processes_with_the_highest_memory_usage,
    kill_a_process_by_pid,
    show_specifications_of_current_computer,
    calculator
)

abilities = [
    find_all_processes,
    find_process_by_name,
    find_top_k_processes_with_the_highest_cpu_usage,
    find_top_k_processes_with_the_highest_memory_usage,
    kill_a_process_by_pid,
    show_specifications_of_current_computer,
    calculator
]

process_manager = None

try:
    # load_dotenv()
    brain = get_openai_model()
    process_manager = AgentForShell(abilities=abilities, brain=brain)
except openai.OpenAIError:
    print('ERR: you must set "OPENAI_API_KEY" environment variable before you make demands on Alfred.')
    exit(1)
