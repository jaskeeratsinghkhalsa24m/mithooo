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

# File path handling for Streamlit Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(current_dir, "images")
music_path = os.path.join(current_dir, "our-song.mp3")

# Load Music
music_html = ""
if os.path.exists(music_path):
    try:
        music_base64 = get_base64(music_path)
        music_html = f'<audio id="bg-music" loop><source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3"></audio>'
    except:
        pass

# Load Photos with "No-White-Space" styling
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
                    photo_tags += f'''
                    <div class="photo-frame" style="transform: rotate({(i%2*6)-3}deg);">
                        <div class="img-wrapper">
                            <img src="data:image/jpeg;base64,{img_b64}">
                        </div>
                    </div>'''
                    found = True
                    break
                except:
                    continue

# The Romantic Interface
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@300;500&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary-pink: #ff4d6d; --dark-pink: #c9184a; --paper-color: #fffdf9; }}
        body {{ 
            margin: 0; padding: 0;
            font-family: 'Quicksand', sans-serif; 
            background: linear-gradient(135deg, #ffafbd, #ffc3a0); 
            color: white; overflow-x: hidden;
        }}
        
        /* Floating Hearts */
        .heart-bg {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }}
        .heart {{ position: absolute; color: rgba(255, 77, 109, 0.6); animation: float 6s infinite linear; font-size: 20px; }}
        @keyframes float {{ 0% {{ transform: translateY(110vh); opacity: 1; }} 100% {{ transform: translateY(-10vh); opacity: 0; }} }}

        /* Password Screen */
        #pass-screen {{ 
            position: fixed; inset: 0; display: flex; flex-direction: column; 
            align-items: center; justify-content: center; z-index: 100; 
            background: rgba(0,0,0,0.5); backdrop-filter: blur(15px); 
        }}
        .main-title {{
            font-family: 'Dancing Script', cursive;
            font-size: 4.5rem;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
            animation: fadeIn 2s ease;
        }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(-20px); }} to {{ opacity: 1; transform: translateY(0); }} }}

        .keypad {{ 
            background: rgba(255,255,255,0.25); 
            padding: 35px; 
            border-radius: 30px; 
            border: 1px solid rgba(255,255,255,0.4); 
            text-align: center;
            box-shadow: 0 0 50px rgba(255, 77, 109, 0.3);
        }}
        .display {{ background: white; color: var(--primary-pink); padding: 15px; border-radius: 10px; margin-bottom: 20px; font-size: 28px; font-weight: bold; letter-spacing: 8px; }}
        .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }}
        button.key-btn {{ width: 65px; height: 65px; border-radius: 50%; border: none; font-weight: bold; cursor: pointer; background: white; font-size: 20px; transition: 0.2s; }}
        button.key-btn:active {{ transform: scale(0.9); background: #ffccd5; }}

        /* Photo Gallery Content */
        #content {{ display: none; text-align: center; padding: 50px 10px; z-index: 10; position: relative; }}
        .heading {{ font-family: 'Dancing Script', cursive; font-size: 4rem; margin-bottom: 40px; }}
        .photo-grid {{ 
            display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
            gap: 30px; max-width: 1200px; margin: 0 auto; padding: 20px;
        }}
        .photo-frame {{ background: white; padding: 12px 12px 40px 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); }}
        .img-wrapper {{ width: 100%; height: 320px; overflow: hidden; background: #eee; }}
        .img-wrapper img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}

        /* Envelope Logic */
        .envelope-wrapper {{
            position: relative; height: 350px; width: 500px; background-color: var(--dark-pink);
            margin: 100px auto; display: flex; justify-content: center; cursor: pointer;
        }}
        .envelope-wrapper:before {{
            content: ""; position: absolute; z-index: 2;
            border-top: 175px solid transparent; border-right: 250px solid var(--primary-pink);
            border-bottom: 175px solid var(--primary-pink); border-left: 250px solid var(--primary-pink);
        }}
        .flap {{
            position: absolute; top: 0; width: 0; height: 0;
            border-top: 180px solid var(--dark-pink); border-left: 250px solid transparent; border-right: 250px solid transparent;
            transform-origin: top; transition: transform 0.4s 0.4s, z-index 0.4s 0.4s; z-index: 5;
        }}
        .letter-content {{
            position: absolute; bottom: 0; width: 85%; height: 90%; background: var(--paper-color);
            text-align: left; padding: 40px; color: #333; font-size: 1.2rem; line-height: 1.8;
            transition: transform 0.4s, z-index 0.4s; z-index: 1; overflow-y: auto;
        }}
        .envelope-wrapper.open .flap {{ transform: rotateX(180deg); z-index: 0; }}
        .envelope-wrapper.open .letter-content {{ transform: translateY(-220px); height: auto; min-height: 350px; z-index: 6; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }}
        .heart-seal {{
            position: absolute; top: 140px; left: 220px; width: 60px; height: 60px;
            background: #ff4d6d; z-index: 6; border-radius: 50%; display: flex;
            align-items: center; justify-content: center; font-size: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }}
        .open .heart-seal {{ opacity: 0; }}
    </style>
</head>
<body>
    {music_html}
    <div class="heart-bg" id="hb"></div>

    <div id="pass-screen">
        <h1 class="main-title">For my Mithooo</h1>
        <div class="keypad">
            <div class="display" id="dis">****</div>
            <div class="grid" id="keys"></div>
            <p style="color: white; margin-top: 20px; font-weight: 500;">Hint: its the code you told me</p>
        </div>
    </div>

    <div id="content">
        <h1 class="heading">I AM SORRY MITHOO ❤️</h1>
        <div class="photo-grid">{{photo_tags}}</div>
        
        <p style="font-size: 2rem; margin-top: 100px;">Click the heart to open my letter ⬇️</p>

        <div class="envelope-wrapper" id="envelope" onclick="toggleLetter()">
            <div class="flap"></div>
            <div class="heart-seal">❤️</div>
            <div class="letter-content">
                <strong>My Dearest Bubu,</strong><br><br>
                I am sorry for not being a good boyfriend. <br><br>
                I love you so much bubu, I not taken you for granted bubu, bas ye hum door hai na, alag alag hogaya hamara sab, isiliye aisa hai, but I love you so much and I think about you everytime love, i JUST MISS YOU A LOTTTTT JALDI SE MERE PAAS AAAJAAOOOOOOOOOO
            </div>
        </div>
        <div style="height: 300px;"></div>
    </div>

    <script>
        setInterval(() => {{
            const h = document.createElement('div');
            h.className = 'heart'; h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            document.getElementById('hb').appendChild(h);
            setTimeout(() => h.remove(), 6000);
        }}, 300);

        let pin = "";
        const keys = [1,2,3,4,5,6,7,8,9,'C',0,'✓'];
        keys.forEach(k => {{
            const b = document.createElement('button');
            b.className = 'key-btn';
            b.innerText = k;
            b.onclick = () => {{
                if(k === 'C') pin = "";
                else if(k === '✓') {{
                    if(pin === "2424") {{
                        const m = document.getElementById('bg-music');
                        if(m) m.play().catch(e => console.log("Music click needed"));
                        document.getElementById('pass-screen').style.display = 'none';
                        document.getElementById('content').style.display = 'block';
                    }} else {{ alert("Wrong PIN, Mithoo!"); pin = ""; }}
                }} else if(pin.length < 4) {{ pin += k; }}
                document.getElementById('dis').innerText = "*".repeat(pin.length) || "****";
            }};
            document.getElementById('keys').appendChild(b);
        }});

        function toggleLetter() {{
            document.getElementById('envelope').classList.toggle('open');
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=4500, scrolling=True)
