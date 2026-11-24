import re

from flask import Flask
from flask import render_template_string
from flask import request

app = Flask(__name__)

CONTACT_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#10111d">
    <title>Contact</title>
    <style>
        * { box-sizing: border-box; }

        body {
            min-height: 100vh;
            margin: 0;
            padding: clamp(1.5rem, 6vw, 5rem);
            color: #f5f3ff;
            background:
                radial-gradient(ellipse at 15% 15%, #48317a 0, transparent 38%),
                radial-gradient(ellipse at 85% 85%, #1c5961 0, transparent 38%),
                #10111d;
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
        }

        main {
            width: min(100%, 38rem);
            margin: 0 auto;
            padding: clamp(1.5rem, 6vw, 3.5rem);
            border: 1px solid #ffffff24;
            border-radius: 2rem;
            background: linear-gradient(140deg, #ffffff12, #ffffff05);
            box-shadow: 0 2rem 6rem #05060d80, inset 0 1px #ffffff18;
            backdrop-filter: blur(18px);
        }

        h1 {
            margin: 0 0 1.5rem;
            font-size: clamp(2rem, 6vw, 3.5rem);
            letter-spacing: -0.06em;
        }

        label { display: block; margin-top: 1rem; font-weight: 600; }

        input, textarea {
            display: block;
            width: 100%;
            margin-top: 0.4rem;
            padding: 0.8rem 1rem;
            border: 1px solid #ffffff30;
            border-radius: 0.75rem;
            color: #f5f3ff;
            background: #10111d99;
            font: inherit;
        }

        textarea { min-height: 9rem; resize: vertical; }

        button {
            margin-top: 1.5rem;
            padding: 0.85rem 1.25rem;
            border: 0;
            border-radius: 0.75rem;
            color: #10111d;
            background: linear-gradient(105deg, #f8ddff, #8de8e5);
            font: inherit;
            font-weight: 700;
            cursor: pointer;
        }

        .error { color: #ffb9c3; }
        .success { color: #a7f3d0; }
    </style>
</head>
<body>
    <main>
        <h1>Contact</h1>
        {% if success %}
        <p class="success" role="status">Thanks for reaching out, {{ name }}. Your message has been received.</p>
        {% else %}
        {% if errors %}
        <ul class="error" role="alert">
            {% for error in errors %}<li>{{ error }}</li>{% endfor %}
        </ul>
        {% endif %}
        <form method="post" action="/contact">
            <label for="name">Name</label>
            <input id="name" name="name" type="text" value="{{ name }}" required>
            <label for="email">Email</label>
            <input id="email" name="email" type="email" value="{{ email }}" required>
            <label for="message">Message</label>
            <textarea id="message" name="message" required>{{ message }}</textarea>
            <button type="submit">Send message</button>
        </form>
        {% endif %}
    </main>
</body>
</html>"""


def is_valid_email(email):
    if len(email) > 254:
        return False

    local, separator, _ = email.partition("@")
    if not separator or len(local) > 64:
        return False

    pattern = (
        r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
        r"(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
        r"@(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
        r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])"
    )
    return re.fullmatch(pattern, email) is not None


@app.get("/")
def home():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#10111d">
    <title>Hello from Suzanne</title>
    <style>
        * { box-sizing: border-box; }

        body {
            display: grid;
            min-height: 100vh;
            min-height: 100svh;
            place-items: center;
            margin: 0;
            padding: 1.5rem;
            color: #f5f3ff;
            background:
                radial-gradient(ellipse at 15% 15%, #48317a 0, transparent 38%),
                radial-gradient(ellipse at 85% 85%, #1c5961 0, transparent 38%),
                #10111d;
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
        }

        main {
            width: min(100%, 52rem);
            padding: clamp(2.5rem, 9vw, 6.5rem) clamp(1.5rem, 8vw, 5rem);
            border: 1px solid #ffffff24;
            border-radius: 2rem;
            background: linear-gradient(140deg, #ffffff12, #ffffff05);
            box-shadow: 0 2rem 6rem #05060d80, inset 0 1px #ffffff18;
            text-align: center;
            backdrop-filter: blur(18px);
        }

        p {
            margin: 0 0 1rem;
            color: #c2b9e8;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.24em;
            text-transform: uppercase;
        }

        h1 {
            margin: 0;
            font-size: clamp(2.5rem, 10vw, 6.5rem);
            font-weight: 800;
            letter-spacing: -0.07em;
            line-height: 1;
            background: linear-gradient(105deg, #f8ddff, #c2b5ff 52%, #8de8e5);
            background-clip: text;
            color: transparent;
        }

        @media (forced-colors: active) {
            h1 { color: CanvasText; }
        }
    </style>
</head>
<body>
    <main>
        <p>A little hello</p>
        <h1>Hello from Suzanne</h1>
    </main>
</body>
</html>"""


@app.route("/contact", methods=["GET", "POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    errors = []

    if request.method == "POST":
        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        elif not is_valid_email(email):
            errors.append("Enter a valid email address.")
        if not message:
            errors.append("Message is required.")

    return render_template_string(
        CONTACT_TEMPLATE,
        name=name,
        email=email,
        message=message,
        errors=errors,
        success=request.method == "POST" and not errors,
    )


@app.get("/about")
def about():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#10111d">
    <title>What would you build? | About</title>
    <style>
        * { box-sizing: border-box; }

        body {
            min-height: 100vh;
            margin: 0;
            padding: clamp(1.5rem, 6vw, 5rem);
            color: #f5f3ff;
            background:
                radial-gradient(ellipse at 15% 15%, #48317a 0, transparent 38%),
                radial-gradient(ellipse at 85% 85%, #1c5961 0, transparent 38%),
                #10111d;
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
            line-height: 1.75;
        }

        main {
            width: min(100%, 52rem);
            margin: 0 auto;
            padding: clamp(1.5rem, 6vw, 4rem);
            border: 1px solid #ffffff24;
            border-radius: 2rem;
            background: linear-gradient(140deg, #ffffff12, #ffffff05);
            box-shadow: 0 2rem 6rem #05060d80, inset 0 1px #ffffff18;
            backdrop-filter: blur(18px);
        }

        h1 {
            margin: 0 0 1.5rem;
            font-size: clamp(2rem, 6vw, 4rem);
            font-weight: 800;
            letter-spacing: -0.06em;
            line-height: 1.1;
            background: linear-gradient(105deg, #f8ddff, #c2b5ff 52%, #8de8e5);
            background-clip: text;
            color: transparent;
        }

        p { color: #dedbed; }

        @media (forced-colors: active) {
            h1 { color: CanvasText; }
        }
    </style>
</head>
<body>
    <main>
        <h1>What would you build if it took an evening instead of a quarter?</h1>
        <p>I would build a delivery driver web application designed to simplify the daily operations of businesses that employ delivery drivers. The application would consist of two main features: a driver scheduling system and a delivery assistant.</p>
        <p>The scheduling system would allow drivers to submit their availability and preferred locations, while managers could assign shifts, manage scheduling conflicts and approve requests for shift cover.</p>
        <p>The delivery assistant would allow drivers to scan delivery dockets, automatically extract addresses, Eircodes and contact details, and launch their preferred navigation application. It would also track completed deliveries, paid and unpaid orders, delivery fees and overall earnings.</p>
        <p>The application would incorporate role-based access control, providing administrators, managers and drivers with separate dashboards and appropriate permissions.</p>
        <p>Using AI-assisted development and low-code tools, I could rapidly transform this idea into a functional minimum viable product, reducing administrative overhead, improving operational efficiency and solving genuine problems experienced by delivery drivers.</p>
    </main>
</body>
</html>"""


if __name__ == "__main__":
    app.run()
