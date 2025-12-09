# handler.py
from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.genai.types import Content, Part   # <-- CORRECT LOCATION


class ConceptLinkerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="concept_linker")

    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:

        # Extract user input
        msg = ""
        if ctx.user_content and ctx.user_content.parts:
            part = ctx.user_content.parts[0]
            if hasattr(part, "text") and part.text:
                msg = part.text

        # Logic
        if "|" not in msg:
            reply = "Please enter: concept1 | concept2"
        else:
            c1, c2 = [x.strip() for x in msg.split("|", 1)]
            reply = f"Write a creative scene connecting '{c1}' and '{c2}'."

        # Build content with GenAI types
        content = Content(
            role="model",
            parts=[Part(text=reply)],
        )

        # Yield an event back to runner
        yield Event(author=self.name, content=content)
