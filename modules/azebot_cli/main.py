#imports
import asyncio

from communication_handler import CommunicationHandler
from session_handler import SessionHandler
import sys

greeting = "$!>"


async def main(handler: CommunicationHandler):
    session_token = await SessionHandler.create_session()

    while True:
        sys.stdout.write(greeting)
        sys.stdout.flush()

        user_input = await asyncio.to_thread(sys.stdin.readline)
        if not user_input:
            break

        user_prompt = user_input.strip()
        if not user_prompt:
            continue

        sys.stdout.write(user_prompt)
        sys.stdout.write("Processing\n")

        request = {
            "source": "azebot_cli",
            "session": session_token,
            "user_prompt": user_prompt,
        }

        response = await handler.add_request(request)

        sys.stdout.write(str(response) + "\n")
        sys.stdout.flush()
