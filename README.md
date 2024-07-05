<h1>Adder Program for Group Members</h1>
<h2>Automatic group to group adder</h2>
<h4>
  Note:
Make sure to manually enter your api_id, api_hash, and phone_number in the corresponding fields before running the program.
</h4>
<h3>

### How the Program Works:
### `get_id.py` This program is a Telegram client that lists all groups in your Telegram account and retrieves the participants of a selected group, saving their IDs and usernames to a txt file.
### `add_members.py` This program is a Telegram client that adds users from a text file to a Telegram group.

**Connecting to Telegram:**

- The program uses the Telethon library to create a Telegram client.
- It connects to a Telegram account using the `api_id`, `api_hash`, and `phone_number`.

**Retrieving and Displaying Groups:**

- The program fetches all dialogs (conversations) and filters out the groups.
- It displays a list of groups for the user to select from.

**Reading Users from a File:**

- The program reads the `members.txt` file and extracts the usernames listed in the file.

**Adding Users to the Group:**

- It adds each user to the selected group and prints the status of each addition or any errors that occur.

**Pause:**

- After adding the users, the program waits for a specified amount of time (in seconds) as determined by the user.

**Logging Out:**

- Finally, the program logs out of the Telegram account.

### Required Libraries:

To run this program, you need to install the Telethon library. You can install it using the following command:

```bash
pip install telethon
```
</h3>
<a href="https://t.me/freedomensan">My Telegram Channel</a>
