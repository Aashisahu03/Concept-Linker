import asyncio
from google.adk.runners import InMemoryRunner
from handler import ConceptLinkerAgent


async def run_test():
    agent = ConceptLinkerAgent()
    runner = InMemoryRunner(agent=agent)

    events = await runner.run_debug("gravity | friendship")

    print("\n--- OUTPUT ---")
    for e in events:
        if hasattr(e, "content") and e.content and e.content.parts:
            # print only text parts
            part = e.content.parts[0]
            if hasattr(part, "text") and part.text:
                print(part.text)


if __name__ == "__main__":
    asyncio.run(run_test())
