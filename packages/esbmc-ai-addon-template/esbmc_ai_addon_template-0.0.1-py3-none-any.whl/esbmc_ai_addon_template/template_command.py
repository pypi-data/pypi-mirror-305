from typing import override, Optional, Any
from esbmc_ai.commands import ChatCommand, CommandResult


class TemplateCommand(ChatCommand):
    def __init__(self) -> None:
        super().__init__(
            "template_1",
            "This is a command from esbmc_ai_addon_template",
            "Yiannis Charalambous",
        )

    @override
    def execute(self, **kwargs: Optional[Any]) -> Optional[CommandResult]:
        _ = kwargs
        print("Hello world!")
