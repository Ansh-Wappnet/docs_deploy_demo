import os

def generate_landing_page():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --text-muted: #94a3b8;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow: hidden;
        }
        .container {
            text-align: center;
            padding: 2rem;
            max-width: 800px;
            z-index: 10;
        }
        h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p {
            color: var(--text-muted);
            font-size: 1.25rem;
            margin-bottom: 3rem;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }
        .card {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 1.5rem;
            text-decoration: none;
            color: inherit;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(255, 255, 255, 0.05);
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .card:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            background-color: #1e293b;
        }
        .card h2 {
            font-size: 1.5rem;
            margin: 0 0 0.75rem 0;
        }
        .card p {
            font-size: 1rem;
            margin: 0;
            color: var(--text-muted);
        }
        .icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
        }
        .bg-glow {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100vw;
            height: 100vh;
            background: radial-gradient(circle at 50% 50%, rgba(99, 102, 241, 0.15) 0%, rgba(0, 0, 0, 0) 50%);
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="bg-glow"></div>
    <div class="container">
        <h1>Documentation Portal</h1>
        <p>Select a portal to explore the documentation.</p>
        <div class="grid">
            <a href="user/" class="card">
                <div class="icon">👤</div>
                <h2>User Docs</h2>
                <p>Guides for end-users and customers.</p>
            </a>
            <a href="super-admin/" class="card">
                <div class="icon">🛡️</div>
                <h2>Super Admin Docs</h2>
                <p>Administration and system configuration.</p>
            </a>
        </div>
    </div>
</body>
</html>
"""
    os.makedirs(".site", exist_ok=True)
    with open(".site/index.html", "w") as f:
        f.write(html_content)
    print("Landing page generated at .site/index.html")

if __name__ == "__main__":
    generate_landing_page()
