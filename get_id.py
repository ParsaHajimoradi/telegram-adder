import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, Chat, Channel

# Replace these values with your actual Telegram API credentials
api_id = ''  # Your API ID
api_hash = ''  # Your API Hash
phone_number = ''  # Your phone number

# Create a Telegram client
client = TelegramClient(phone_number, api_id, api_hash)

async def list_groups_and_get_participants(client):
    await client.start()
    
    # Get all dialogs (chats and channels)
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))

    chats = []
    for chat in result.chats:
        if isinstance(chat, (Chat, Channel)) and getattr(chat, 'megagroup', False):
            chats.append(chat)

    print("List of groups:")
    for i, chat in enumerate(chats):
        print(f"{i + 1}. {chat.title}")

    # Select the group to work with
    group_index = int(input("Enter the number of the group: ")) - 1
    if group_index < 0 or group_index >= len(chats):
        print("Invalid group number.")
        return

    group = chats[group_index]

    # Retrieve participants of the selected group
    offset = 0
    limit = 100
    all_participants = []

    while True:
        participants = await client(GetParticipantsRequest(
            group, ChannelParticipantsSearch(''), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)

    # Append participant IDs and usernames to a file
    with open('members.txt', 'a') as file:
        for participant in all_participants:
            if participant.id is not None or participant.username is not None:
                file.write(f"ID: {participant.id}, Username: {participant.username}\n")

    print("All members with IDs or usernames have been saved.")
    await client.disconnect()

with client:
    client.loop.run_until_complete(list_groups_and_get_participants(client))