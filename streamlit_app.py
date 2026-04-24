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

# File path handling
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

# Load Photos with improved "No-White-Space" styling
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
                    # This styling crops the photo to fill the frame perfectly
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
        :root {{ --primary-pink: #ff4d6d; --soft-pink: #ffccd5; }}
        body {{ 
            margin: 0; padding: 0;
            font-family: 'Quicksand', sans-serif; 
            background: linear-gradient(135deg, #ffafbd, #ffc3a0); 
            color: white; overflow-x: hidden;
        }}
        
        .heart-bg {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }}
        .heart {{ position: absolute; color: rgba(255, 77, 109, 0.6); animation: float 6s infinite linear; font-size: 20px; }}
        @keyframes float {{ 0% {{ transform: translateY(110vh); opacity: 1; }} 100% {{ transform: translateY(-10vh); opacity: 0; }} }}

        /* Password Screen */
        #pass-screen {{ 
            position: fixed; inset: 0; display: flex; flex-direction: column; 
            align-items: center; justify-content: center; z-index: 100; 
            background: rgba(0,0,0,0.5); backdrop-filter: blur(15px); 
        }}
        .keypad {{ background: rgba(255,255,255,0.2); padding: 30px; border-radius: 20px; border: 1px solid white; text-align: center; }}
        .display {{ background: white; color: var(--primary-pink); padding: 15px; border-radius: 10px; margin-bottom: 20px; font-size: 28px; font-weight: bold; letter-spacing: 8px; }}
        .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
        button {{ width: 60px; height: 60px; border-radius: 50%; border: none; font-weight: bold; cursor: pointer; background: white; font-size: 18px; }}

        /* Photo Gallery Styling */
        #content {{ display: none; text-align: center; padding: 50px 10px; z-index: 10; position: relative; }}
        .heading {{ font-family: 'Dancing Script', cursive; font-size: 3.5rem; margin-bottom: 40px; }}
        
        .photo-grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
            gap: 30px; 
            max-width: 1200px; 
            margin: 0 auto; 
            padding: 20px;
        }}

        .photo-frame {{
            background: white;
            padding: 12px 12px 40px 12px; /* Traditional Polaroid look */
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            transition: 0.3s;
        }}

        .img-wrapper {{
            width: 100%;
            height: 300px; /* Forces a uniform height */
            overflow: hidden;
            background: #eee;
        }}

        .img-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover; /* THIS REMOVES THE WHITE SPACE BY FILLING THE AREA */
            display: block;
        }}

        .photo-frame:hover {{ transform: scale(1.05) rotate(0deg) !important; z-index: 20; }}

        /* Letter Styling */
        .letter-container {{ margin: 60px auto; max-width: 600px; }}
        .letter-box {{ 
            background: #fffdf9; color: #333; padding: 40px; 
            border-radius: 5px; text-align: left; line-height: 1.8; 
            display: none; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            font-size: 1.2rem; border-top: 8px solid var(--primary-pink);
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
            <p>Hint: 2424</p>
        </div>
    </div>

    <div id="content">
        <h1 class="heading">I AM SORRY MITHOO ❤️</h1>
        <div class="photo-grid">{photo_tags}</div>
        
        <div class="letter-container">
            <p style="font-size: 1.5rem;">Scroll down for my heart... ⬇️</p>
            <button onclick="showLetter()" style="padding: 15px 40px; border-radius: 30px; border: none; background: #ff4d6d; color: white; font-weight: bold; font-size: 1.2rem; cursor: pointer;">Open My Letter ✉️</button>
            <div class="letter-box" id="let">
                I am sorry for not being a good boyfriend. <br><br>
                I love you so much bubu, I not taken you for granted bubu, bas ye hum door hai na, alag alag hogaya hamara sab, isiliye aisa hai, but I love you so much and I think about you everytime love, i JUST MISS YOU A LOTTTTT JALDI SE MERE PAAS AAAJAAOOOOOOOOOO
            </div>
        </div>
    </div>

    <script>
        // Hearts logic
        setInterval(() => {{
            const h = document.createElement('div');
            h.className = 'heart'; h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            document.getElementById('hb').appendChild(h);
            setTimeout(() => h.remove(), 6000);
        }}, 300);

        // Keypad logic
        let pin = "";
        const keys = [1,2,3,4,5,6,7,8,9,'C',0,'✓'];
        keys.forEach(k => {{
            const b = document.createElement('button');
            b.innerText = k;
            b.onclick = () => {{
                if(k === 'C') pin = "";
                else if(k === '✓') {{
                    if(pin === "2424") {{
                        const m = document.getElementById('bg-music');
                        if(m) m.play();
                        document.getElementById('pass-screen').style.display = 'none';
                        document.getElementById('content').style.display = 'block';
                    }} else {{ alert("Incorrect PIN, Mithoo!"); pin = ""; }}
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

components.html(html_code, height=3500, scrolling=True)
