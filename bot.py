# Import required modules
import discord          # Discord library to create the bot
import requests         # To fetch memes from the API
import json             # To parse JSON response from the meme API

# Function to get a random meme
# Make a GET request to the meme API
# Parse the JSON response
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
     # Return the meme image URL
    return json_data['url']

# Custom bot client class inheriting from discord.Client
class MyClient(discord.Client):

    # This function runs once when the bot is ready
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user)) # Prints bot's username and tag in the terminal, NOT in the discord channel

    # This function handles incoming messages
    async def on_message(self, message):
        # Prevent the bot from replying to itself
        if message.author == self.user:
            return # Returns nothing
        
        # Convert the incoming message to lowercase for easier matching
        msg = message.content.lower()

        # List of basic greeting keywords the bot will respond to
        greetings = [
    'hi', 'hello', 'hey', 'yo', 'sup', 'heya', 'hiya',
    'good morning', 'good afternoon', 'good evening', 'greetings',
    'wassup', 'whatsup', 'howdy', 'hola', 'salut', 'namaste', 'shalom', 'bonjour', 'konnichiwa',
    'o7', 'hiiii', 'helloooo', 'hewwo', 'hai', 'sup bro', 'yo yo', '👋','anna namaste'] 

        # If the message is a greeting, respond with a friendly reply
        if msg in greetings:
            await message.channel.send("Wassup, It's me yo dear boy Jaya, hope you're have a good day! \nAnyways, type '`!funnyjoke`' to receive a crispy, juicy, fresh ah meme :wink:   \n||my dad Deva, only allowed me to respond to basic greeting messages and !funnyjoke command|| ")

        # If the message starts with "$meme", send a meme from the API
        if msg.startswith('!funnyjoke'):
            await message.channel.send(get_meme())

# Set up message intent (required to read message content in newer API versions)
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot client with the specified intents
client = MyClient(intents=intents) 

# Run the bot using your bot token (replace 'token' with your actual token)
# 🔐 DO NOT share this token with anyone
client.run('token') # Replace with your own token. 


