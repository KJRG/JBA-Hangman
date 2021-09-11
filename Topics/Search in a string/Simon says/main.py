SIMON_SAYS = "Simon says"


def what_to_do(instructions):
    instructions_content = "won't do it!"
    if instructions.startswith(SIMON_SAYS):
        instructions_content = instructions[len(SIMON_SAYS) + 1:]
    elif instructions.endswith(SIMON_SAYS):
        instructions_content = instructions[:len(SIMON_SAYS) + 1]
    return f"I {instructions_content}"
