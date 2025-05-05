# 🤖 HowTo Build the `!NotFunny` - The Meme Bot That No One Asked For

Welcome to the ultimate guide for building your own sarcastic Discord bot just like mine: **!NotFunny**.

---

# # Introduction
Welcome, traveler of the interwebz 👨‍💻👩‍💻

Are you tired of boring bots that just say "Hello World"?  
Do you crave **fresh**, **crispy**, **sometimes questionable** memes on demand?  
Do you want a bot that replies to "hi" or "hello" like it's its only purpose in life?

Well, congratulations... you’ve just discovered `!NotFunny` —  
The *most ironically named* meme bot that *might actually* make you laugh (I don't think so unless your humor is broken).

Powered by Python, sarcasm, and the occasional API hiccup,  
`!NotFunny` will chill in your server, crack open a cold meme, and drop it like it's 2012 again.  
And yes — it **only** responds to greetings and memes because boundaries are important (Lazy to implement more).

So buckle up, grab some snacks 🍿, and let’s build a bot that your friends won’t admit they love (they're jealous re).

**Disclaimer:** Bot is not responsible for meme addictions, keyboard smashing, or accidental LOLs.
---

## 📋 Prerequisites

Make sure you have:

- [Python 3.10+](https://www.python.org/downloads/) installed
- A [Discord](https://discord.com/download) account
- [Basic knowledge](https://docs.python.org/3/tutorial/index.html) of Python (helpful but not required)
- A Discord server to test the bot in, and a must have for you is "Manage Server" permissions. 
- Then you're good to start. :wink (i purposefully didn't finish the wink, i dont know, just like that)

---

# 🧠 Whoa.. Whoa.. Whoa.. Let's pause there Mr./Mrs. Frankenstein 🤖  
### Let's Understand How a Discord Bot *Actually* Works First  

We need fundamentals for everything, right?  
You wouldn’t build a nuclear toaster without reading the manual (ahh… hopefully).

So before we dive into crafting our meme-slinging masterpiece, let’s break it down:

You can skip this and scroll down to "Steps"

## 🤔 What *is* a Discord Bot?

A Discord bot is like a very obedient digital servant that lives in your server.  
It’s just a regular program (written in Python, in our case) that:

- Logs into Discord using a special **bot token** 🪪  
- Listens for messages in channels 👂 (an event listener)  
- Reacts to certain **commands** or **keywords** 💬  
- Sends messages, memes, or even chaos (your call) 💣

Think of it as a bridge between your code and your server.  
Instead of you typing in a message, your code types it for you! (Robot Slavery)

---

## 🔄 How Does It Work?

1. **The Code**: You write Python code by importing `discord.py`, `requests` & `json` library  
2. **The Bot Token**: Discord gives your bot a unique ID (like your password with your crush name), which you'll include in the code. Remember you're *not* supposed to share this to *anyone*, It's a high priority secret
3. **The Gateway**: Your bot connects to Discord’s servers upon running the program and listens for stuff happening  
4. **Message Handling**: If someone types `!funnyjoke`, your bot’s like:  
   *“Ayo, I got just the meme for you, here enjoy my guy.”*  
5. **API Magic**: The bot fetches a meme from an API and sends it in the channel; Now WHAT THE FUNNY is an API you may ask, well...
    API (Application Programming Interface) is just a fancy terminology to define how one program talks to another program. In our case, Discord's API allows us to read and send messages to its backend servers.
6. **Repeat**: Your bot does this all day like a loyal little script

---

## ⚙️ Behind the Scenes

- It runs continuously (until you tell it to stop or it crashes from bad code 💥)  
- You can run it locally, or host it on a server (like Replit, Render, or Railway)  
- It can be simple (like ours) or grow into a monster that plays music, moderates chats, and takes over your social life

---

So now that you've been blessed with this **forbidden knowledge**,  
let’s get back to building our meme-summoning sarcasm machine: `!NotFunny`.

*Just remember: with great bots comes great meme-sponsibility.*
 

---

# Steps: Now its time to start working my dear boys and girls (unless you're older than 30, then you're be uncle and aunty XD). 
## 🔧 Step 1: Set Up Your Bot on Discord

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**
3. Name your app: `NotFunny`
4. Go to **Bot** → **Add Bot** → Yes
5. Copy your bot **TOKEN** (keep it secret!)
6. Under **Privileged Gateway Intents**, enable:
   - `MESSAGE CONTENT INTENT`

---

## 🔗 Step 2: Invite the Bot to Your Server

1. Go to the **OAuth2 → URL Generator**
2. Select:
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Read Message History`
3. Copy the generated URL and paste it in your browser
4. Select your server → Authorize

---

## 🧪 Step 3: Set Up Your Project

1. Create a folder: `notfunny-bot`
2. Create and activate a virtual environment *(optional but recommended)*:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
