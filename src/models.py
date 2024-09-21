import os

from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from openai import OpenAI
from openai.pagination import SyncCursorPage
from openai.types.beta import Thread
from dotenv import load_dotenv

from src import tools

from src.config import assistant_detail

load_dotenv()

fakeit_assistant = OpenAIAssistantRunnable(
    assistant_id=assistant_detail['id_fakeit'],
    as_agent=True,
)

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


async def assistant_completion(message, assistant_id: str, thread: Thread) -> SyncCursorPage:
    # Add message to thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message,
    )

    # Run the specified thread with the specified assistant
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

    if run.status == 'requires_action':
        if run.required_action.type == 'submit_tool_outputs':
            print("---Action required---")
            print(run.required_action.submit_tool_outputs.tool_calls[0].function.name)
            print(run.required_action.submit_tool_outputs.tool_calls[0].function.arguments)
            function_name = run.required_action.submit_tool_outputs.tool_calls[0].function.name
            arguments = run.required_action.submit_tool_outputs.tool_calls[0].function.arguments
            result = getattr(tools, function_name)(arguments)
            tool_call_id = run.required_action.submit_tool_outputs.tool_calls[0].id

            client.beta.threads.runs.submit_tool_outputs_and_poll(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=[
                    {
                        "tool_call_id": tool_call_id,
                        "output": result
                    }
                ]
            )

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages.data)
    return messages


if __name__ == "__main__":
    response = fakeit_assistant.invoke({'content': 'Where is Paris'})

    print(response)
    print(type(response))

