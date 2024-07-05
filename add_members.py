from telethon import TelegramClient, sync
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import PeerChannel
from time import sleep

# Replace these values with your actual Telegram API credentials
api_id = ''  # Your API ID
api_hash = ''  # Your API Hash
phone_number = ''  # Your phone number

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Log in to Telegram
    await client.start(phone=phone_number)

    # Get dialogs (conversations)
    dialogs = await client.get_dialogs()

    # Filter only group chats
    groups = [d for d in dialogs if d.is_group]

    # Print the list of group chats
    print("Groups:")
    for i, group in enumerate(groups, start=1):
        print(f"{i}. {group.name}")

    # Ask the user to select a group
    choice = int(input("Select a group by number: ")) - 1
    selected_group = groups[choice]

    #Ask time Sleep
    timesq = int(input('How long should the time sleep be: '))
    # Read the users from the text file
    users_to_add = []
    with open('members.txt', 'r') as file:
        for line in file:
            parts = line.split(', ')
            username = parts[1].split(': ')[1].strip()
            if username != 'None':
                users_to_add.append('@' + username)

    # Add each user to the selected group
    for user in users_to_add:
        try:
            await client(InviteToChannelRequest(PeerChannel(selected_group.id), [user]))
            print(f"User {user} added to group {selected_group.name}")
        except Exception as e:
            print(f"Failed to add user {user}: {e}")
    sleep(timesq)
    # Log out
    await client.log_out()

with client:
    client.loop.run_until_complete(main())