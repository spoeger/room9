from flask import Flask

app = Flask(__name__)

# HTML Template without Images
def html_template(title, story, choices):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                background-color: #f4f1de;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
            }}
            h1 {{
                color: #3d405b;
            }}
            p {{
                font-size: 18px;
            }}
            a {{
                display: block;
                margin: 10px;
                padding: 10px;
                background-color: #81b29a;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-size: 20px;
            }}
            a:hover {{
                background-color: #e07a5f;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <p>{story}</p>
        {choices}
    </body>
    </html>
    """

# 🏡 Home Page
@app.route("/")
def home():
    return html_template(
        "🌲 Welcome to the Magical Forest, Room 9! 🌲",
        "You are standing at the entrance of a magical forest. What do you do?",
        """
        <a href='/left'>🚶 Follow the path to the left</a>
        <a href='/right'>🚶 Follow the path to the right</a>
        <a href='/squirrel'>🐿️ Talk to the squirrel</a>
        """
    )

# 🦊 Fox’s Riddle Challenge
@app.route("/left")
def left():
    return html_template(
        "🦊 The Fox’s Riddle",
        "The fox smiles: 'Solve this riddle: I speak without a mouth and hear without ears. What am I?'",
        """
        <a href='/golden_bridge'>🧠 Answer: An Echo</a>
        <a href='/tricky_maze'>🤔 Answer: A Shadow</a>
        """
    )

# 🌉 Golden Bridge (Correct Answer)
@app.route("/golden_bridge")
def golden_bridge():
    return html_template(
        "🌉 The Golden Bridge",
        "You solved the riddle! A golden bridge appears. As you cross, two paths open ahead.",
        """
        <a href='/talking_rabbit'>🎩 Meet a Talking Rabbit</a>
        <a href='/hidden_castle'>🏯 Explore the Hidden Castle</a>
        """
    )

# 🎩 Talking Rabbit (Final)
@app.route("/talking_rabbit")
def talking_rabbit():
    return html_template(
        "🎩 The Talking Rabbit’s Gift",
        "The rabbit gives you a potion that grants you the ability to read ancient magical texts. Your adventure is just beginning!",
        "<a href='/'>🔙 Play Again</a>"
    )

# 🏯 Hidden Castle (Final)
@app.route("/hidden_castle")
def hidden_castle():
    return html_template(
        "🏯 The Sleeping Knight",
        "The knight awakens, sees your bravery, and rewards you with a magical shield. Your journey ends here… for now!",
        "<a href='/'>🔙 Play Again</a>"
    )

# 🌀 Tricky Maze (Wrong Answer)
@app.route("/tricky_maze")
def tricky_maze():
    return html_template(
        "🌀 Lost in the Maze",
        "Oh no! The fox laughs. 'Not quite right! You must now find your way out of the tricky maze!'",
        "<a href='/'>🔙 Try Again</a>"
    )

# 🪄 The Cave Path (Magic & Wisdom)
@app.route("/right")
def right():
    return html_template(
        "🪄 The Glowing Cave",
        "Inside the cave, a wise owl holds a glowing key. What do you do?",
        """
        <a href='/owl'>🦉 Talk to the Owl</a>
        <a href='/hidden_library'>📚 Enter the Secret Library</a>
        """
    )

# 🦉 Talking to the Owl
@app.route("/owl")
def owl():
    return html_template(
        "🦉 The Wise Owl Speaks",
        "The owl nods and says, 'Knowledge is the greatest treasure. Choose your path wisely.'",
        """
        <a href='/hidden_library'>📚 Explore the Secret Library</a>
        <a href='/giant'>🌋 Wake the Sleeping Giant</a>
        <a href='/'>🔙 Return Home</a>
        """
    )

# 📚 Secret Library (Final)
@app.route("/hidden_library")
def hidden_library():
    return html_template(
        "📚 The Hidden Kingdom",
        "You enter a secret kingdom of magic, where you can learn ancient spells. A whole new world awaits!",
        "<a href='/'>🔙 Play Again</a>"
    )

# 🌋 Wake the Sleeping Giant (Final)
@app.route("/giant")
def giant():
    return html_template(
        "🌋 The Guardian of the Land",
        "The giant awakens and declares you the new protector of the land. Your legend will live forever!",
        "<a href='/'>🔙 Play Again</a>"
    )

# 🐿️ Squirrel’s Path (Adventure & Treasure)
@app.route("/squirrel")
def squirrel():
    return html_template(
        "🐿️ The Squirrel’s Advice",
        "The squirrel whispers: 'Follow the stars or light a fire for warmth.'",
        """
        <a href='/stars'>✨ Follow the stars</a>
        <a href='/dragon'>🔥 Build a campfire</a>
        """
    )

# ☁️ Floating Island (Final)
@app.route("/stars")
def stars():
    return html_template(
        "☁️ The Lost Treasure",
        "You find an abandoned pirate ship filled with gold! Your fortune is made.",
        "<a href='/'>🔙 Play Again</a>"
    )

# 🔥 Mystical Dragon (Final)
@app.route("/dragon")
def dragon():
    return html_template(
        "🐉 The Mystical Dragon",
        "The dragon grants you one magical power. Choose wisely!",
        """
        <a href='/fire_power'>🔥 Power of Fire</a>
        <a href='/flight_power'>🦅 Power of Flight</a>
        <a href='/invisibility_power'>👻 Power of Invisibility</a>
        """
    )

# 🏆 Final Power Choices
@app.route("/fire_power")
def fire_power():
    return html_template("🔥 Power of Fire", "You can breathe fire like a dragon!", "<a href='/'>🔙 Play Again</a>")

@app.route("/flight_power")
def flight_power():
    return html_template("🦅 Power of Flight", "You can soar through the skies!", "<a href='/'>🔙 Play Again</a>")

@app.route("/invisibility_power")
def invisibility_power():
    return html_template("👻 Power of Invisibility", "You vanish into thin air at will!", "<a href='/'>🔙 Play Again</a>")

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True, port=5001)
