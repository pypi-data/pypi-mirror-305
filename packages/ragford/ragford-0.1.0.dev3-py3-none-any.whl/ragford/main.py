import os
import io
import time
import json
import logging
import inspect
import asyncio

import hikari
import lightbulb
from dotenv import load_dotenv

import swarmauri_core
import swarmauri
from swarmauri.llms.concrete.GroqModel import GroqModel
from swarmauri.vector_stores.concrete.TfidfVectorStore import TfidfVectorStore
from swarmauri.documents.concrete.Document import Document
from swarmauri.agents.concrete.RagAgent import RagAgent
from swarmauri.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation
from swarmauri.messages.concrete.SystemMessage import SystemMessage

# Load environment variables from development.env
load_dotenv()

# Configuration Constants from environment variables
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
SYSTEM_CONTEXT_INSTRUCTION = os.getenv('SYSTEM_CONTEXT_INSTRUCTION', 'You are a python developer...')
TEMPERATURE_VALUE = float(os.getenv('TEMPERATURE_VALUE', 0.9))
MAX_TOKEN_VALUE = int(os.getenv('MAX_TOKEN_VALUE', 1500))
MAX_CONVERSATION_SIZE = int(os.getenv('MAX_TOKEN_VALUE', 5))
TOP_K_VALUE = int(os.getenv('TOP_K_VALUE', 20))
CACHE_EXPIRATION = int(os.getenv('CACHE_EXPIRATION', 3600))

# Initialize the Bot
bot = lightbulb.BotApp(token=DISCORD_BOT_TOKEN)
cache = {}

# Initialize Language Model, Global Conversation, and Vector Store
llm = GroqModel(api_key=GROQ_API_KEY, name='llama-3.1-8b-instant')
global_conversation = MaxSystemContextConversation(system_context=SystemMessage(content=SYSTEM_CONTEXT_INSTRUCTION), max_size=MAX_CONVERSATION_SIZE)
vector_store = TfidfVectorStore()
global_agent = RagAgent(llm=llm, conversation=global_conversation, system_context=SystemMessage(content=SYSTEM_CONTEXT_INSTRUCTION), vector_store=vector_store)

llm_kwargs = {"temperature": TEMPERATURE_VALUE, "max_tokens": MAX_TOKEN_VALUE}
thread_agents = {}  # Dictionary to store agents for each thread

# Utility to Load Documents from a Folder
def load_documents_from_folder(folder_path, include_extensions=None, exclude_extensions=None,
                               include_folders=None, exclude_folders=None):
    documents = []
    include_all_files = not include_extensions and not exclude_extensions
    include_all_folders = not include_folders and not exclude_folders

    for root, dirs, files in os.walk(folder_path):
        current_folder_name = os.path.basename(root)
        if not include_all_folders:
            if include_folders and current_folder_name not in include_folders:
                logging.info(f"Skipping folder: {current_folder_name}")
                continue
            if exclude_folders and current_folder_name in exclude_folders:
                logging.info(f"Skipping folder: {current_folder_name}")
                continue

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_extension = file_name.split(".")[-1]
            if include_all_files or (include_extensions and file_extension in include_extensions) or \
               (exclude_extensions and file_extension not in exclude_extensions):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        document = Document(content=content, metadata={"filepath": file_path})
                        documents.append(document)
                except (json.JSONDecodeError, Exception) as e:
                    logging.warning(f"Skipping file: {file_name} ({e})")
    return documents

# Load and Add Documents to Vector Store
folder_path = os.path.dirname(inspect.getfile(swarmauri))
documents = load_documents_from_folder(folder_path, exclude_folders=["__pycache__"])
vector_store.add_documents(documents)
print(f"{len(vector_store.documents)} documents added to the vector store.")

# Load and Add More Documents to Vector Store
folder_path = os.path.dirname(inspect.getfile(swarmauri_core))
documents = load_documents_from_folder(folder_path, exclude_folders=["__pycache__"])
vector_store.add_documents(documents)
print(f"{len(vector_store.documents)} documents added to the vector store.")


# Retry Decorator
def retry_on_empty(retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                result = func(*args, **kwargs)
                if result:
                    print('got a result')
                    return result
                print('Retrying due to empty result...')
            return result
        return wrapper
    return decorator

# Caching and Conversing with the Agent
@retry_on_empty(retries=2)
def converse(prompt, agent):
    return agent.exec(input_data=prompt, top_k=TOP_K_VALUE, llm_kwargs=llm_kwargs)

def converse_with_cache(prompt, agent):
    if prompt in cache:
        result, timestamp = cache[prompt]
        if time.time() - timestamp < CACHE_EXPIRATION:
            return result
    result = converse(prompt, agent)
    if result:
        cache[prompt] = (result, time.time())
    return result

# Helper to create a unique agent for each thread or channel
def get_or_create_agent(channel_id):
    if channel_id not in thread_agents:
        conversation = MaxSystemContextConversation(
            system_context=SystemMessage(content=SYSTEM_CONTEXT_INSTRUCTION),
            max_size=MAX_CONVERSATION_SIZE
        )
        agent = RagAgent(
            llm=llm,
            conversation=conversation,
            system_context=SystemMessage(content=SYSTEM_CONTEXT_INSTRUCTION),
            vector_store=vector_store
        )
        thread_agents[channel_id] = agent
    return thread_agents[channel_id]

# Slash Command to Create a New Thread and Start a Conversation
@bot.command
@lightbulb.option("topic", "The topic for the new thread.", type=str)
@lightbulb.command("create_thread", "Create a new thread and start a conversation.")
@lightbulb.implements(lightbulb.SlashCommand)
async def create_thread_command(ctx: lightbulb.Context):
    topic = ctx.options.topic
    channel_id = ctx.channel_id

    # Send initial response
    intro_message = f"A new thread on '{topic}' has been created! Feel free to ask questions here."
    await ctx.respond(intro_message)

    # Wait briefly to allow the message to send, then retrieve it
    await asyncio.sleep(1)  # Short delay to ensure message is posted

    # Fetch the last message in the channel to get its ID
    messages = await bot.rest.fetch_messages(channel_id)
    message_id = messages[0].id  # Get the ID of the most recent message (sent by ctx.respond)

    # Create a new thread in reply to this message
    thread = await bot.rest.create_message_thread(channel_id, message_id, topic)
    thread_id = thread.id

    # Initialize a new agent for this thread
    agent = get_or_create_agent(thread_id)

# Slash Command for Interaction within Threads
@bot.command
@lightbulb.option("prompt", "The prompt to converse with the agent.", type=str)
@lightbulb.command("converse", "Interact with the bot using the AI agent.")
@lightbulb.implements(lightbulb.SlashCommand)
async def converse_command(ctx: lightbulb.Context):
    prompt = ctx.options.prompt
    thread_id = ctx.channel_id

    # Get or create agent for the specific thread
    agent = get_or_create_agent(thread_id)
    await ctx.respond("Processing your request...", flags=hikari.MessageFlag.EPHEMERAL)

    # Converse with agent and get response
    result = converse_with_cache(prompt.strip(), agent)

    # Send response based on length
    if len(result) == 0:
        await ctx.respond("I couldn't generate a response. Please try again.")
    elif len(result) > 2000:
        file_content = io.BytesIO(result.encode('utf-8'))
        await ctx.respond("The response is too lengthy. Sending as an attachment...", attachment=hikari.Bytes(file_content, "response.md"))
    else:
        await ctx.respond(result)

@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print("Bot is online and started!")

@bot.listen(hikari.StoppedEvent)
async def bot_stop(event):
    print('\nBot stopping successfully.\n')

if __name__ == "__main__":
    bot.run()
