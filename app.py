from flask import Flask

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run()
