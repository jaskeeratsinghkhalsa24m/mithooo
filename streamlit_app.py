import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Set page title and icon
st.set_page_config(page_title="For My Mithoo", page_icon="❤️", layout="wide")

# Function to encode local files to base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ensure we are looking in the correct directory
current_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(current_dir, "images")
music_path = os.path.join(current_dir, "our-song.mp3")

# Load Music
music_html = ""
if os.path.exists(music_path):
    try:
        music_base64 = get_base64(music_path)
        music_html = f'<audio id="bg-music" loop><source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3"></audio>'
    except Exception as e:
        music_html = f""

# Load Photos (Checks for 1-30 with multiple extensions)
photo_tags = ""
extensions = [".jpg", ".jpeg", ".png", ".JPG", ".PNG"]

if os.path.exists(images_path):
    for i in range(1, 31):
        found = False
        for ext in extensions:
            p = os.path.join(images_path, f"{i}{ext}")
            if os.path.exists(p):
                try:
                    img_b64 = get_base64(p)
                    # Use a standard polaroid-style frame for the photos
                    photo_tags += f'''
                    <div style="background: white; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); margin-bottom: 20px; transform: rotate({(i%2*4)-2}deg);">
                        <img src="data:image/jpeg;base64,{img_b64}" style="width:100%; display:block;">
                    </div>'''
                    found = True
                    break
                except:
                    continue
        if not found:
            photo_tags += f""

# The Romantic Interface
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@300;500&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary-pink: #ff4d6d; --soft-pink: #ffccd5; }}
        body {{ 
            margin: 0; 
            font-family: 'Quicksand', sans-serif; 
            background: linear-gradient(135deg, #ffafbd, #ffc3a0); 
            color: white; 
            overflow-x: hidden; 
            min-height: 100vh;
        }}
        
        .heart-bg {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }}
        .heart {{ position: absolute; color: rgba(255, 77, 109, 0.6); animation: float 6s infinite linear; font-size: 20px; }}
        @keyframes float {{ 0% {{ transform: translateY(110vh); opacity: 1; }} 100% {{ transform: translateY(-10vh); opacity: 0; }} }}

        #pass-screen {{ 
            position: fixed; inset: 0; display: flex; flex-direction: column; 
            align-items: center; justify-content: center; z-index: 100; 
            background: rgba(0,0,0,0.4); backdrop-filter: blur(15px); 
        }}
        .keypad {{ background: rgba(255,255,255,0.25); padding: 30px; border-radius: 20px; border: 1px solid white; text-align: center; }}
        .display {{ background: white; color: var(--primary-pink); padding: 15px; border-radius: 10px; margin-bottom: 20px; font-size: 28px; font-weight: bold; letter-spacing: 8px; min-width: 150px; }}
        .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }}
        button.num-key {{ width: 60px; height: 60px; border-radius: 50%; border: none; font-weight: bold; cursor: pointer; font-size: 20px; background: white; color: #333; }}
        button.num-key:active {{ background: var(--soft-pink); }}
        
        #content {{ display: none; text-align: center; padding: 50px 20px; position: relative; z-index: 10; }}
        .heading {{ font-family: 'Dancing Script', cursive; font-size: 4rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.2); }}
        .photo-grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
            gap: 25px; 
            margin: 40px auto; 
            max-width: 1100px;
        }}
        .letter {{ 
            background: #fffdf9; color: #333; padding: 40px; 
            border-radius: 10px; margin: 50px auto; max-width: 650px; 
            text-align: left; line-height: 1.8; display: none; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-top: 8px solid var(--primary-pink);
            font-size: 1.2rem;
        }}
        .open-btn {{ 
            padding: 20px 40px; font-size: 1.3rem; background: var(--primary-pink); 
            color: white; border: none; border-radius: 50px; cursor: pointer; 
            box-shadow: 0 5px 15px rgba(0,0,0,0.2); font-weight: bold;
        }}
    </style>
</head>
<body>
    {music_html}
    <div class="heart-bg" id="hb"></div>

    <div id="pass-screen">
        <div class="keypad">
            <div class="display" id="dis">****</div>
            <div class="grid" id="keys"></div>
            <p style="margin-top: 15px;">Hint: 2424</p>
        </div>
    </div>

    <div id="content">
        <h1 class="heading">I AM SORRY MITHOO ❤️</h1>
        <div class="photo-grid">{photo_tags}</div>
        <p style="font-size: 1.8rem; margin: 40px 0;">Scroll down bubu... ⬇️</p>
        <button class="open-btn" onclick="showLetter()">Open My Letter ✉️</button>
        <div class="letter" id="let">
            I am sorry for not being a good boyfriend. <br><br>
            I love you so much bubu, I not taken you for granted bubu, bas ye hum door hai na, alag alag hogaya hamara sab, isiliye aisa hai, but I love you so much and I think about you everytime love, i JUST MISS YOU A LOTTTTT JALDI SE MERE PAAS AAAJAAOOOOOOOOOO
        </div>
    </div>

    <script>
        // Floating Hearts
        setInterval(() => {{
            const h = document.createElement('div');
            h.className = 'heart'; h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            document.getElementById('hb').appendChild(h);
            setTimeout(() => h.remove(), 6000);
        }}, 300);

        // Keypad Logic
        let pin = "";
        const keys = [1,2,3,4,5,6,7,8,9,'C',0,'✓'];
        keys.forEach(k => {{
            const b = document.createElement('button');
            b.className = 'num-key';
            b.innerText = k;
            b.onclick = () => {{
                if(k === 'C') pin = "";
                else if(k === '✓') {{
                    if(pin === "2424") {{
                        const m = document.getElementById('bg-music');
                        if(m) m.play();
                        document.getElementById('pass-screen').style.display = 'none';
                        document.getElementById('content').style.display = 'block';
                    }} else {{ alert("Wrong PIN!"); pin = ""; }}
                }} else if(pin.length < 4) {{ pin += k; }}
                document.getElementById('dis').innerText = "*".repeat(pin.length) || "****";
            }};
            document.getElementById('keys').appendChild(b);
        }});

        function showLetter() {{ 
            document.getElementById('let').style.display = 'block'; 
            window.scrollTo({{ top: document.body.scrollHeight, behavior: 'smooth' }}); 
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=3000, scrolling=True)
