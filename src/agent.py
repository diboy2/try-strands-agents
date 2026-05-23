from strands import Agent, tool
from strands_tools import calculator, current_time

@tool
def letter_counter(word: str) -> int:
    return len(word)