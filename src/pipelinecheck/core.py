from collections.abc import Iterable, Mapping

def validate(steps: Iterable[Mapping[str, object]]) -> list[str]:
    """Validate that pipeline steps have names and commands."""
    errors=[]
    for i, step in enumerate(steps):
        if not str(step.get("name", "")).strip(): errors.append(f"step[{i}]: missing name")
        if not str(step.get("command", "")).strip(): errors.append(f"step[{i}]: missing command")
    return errors
