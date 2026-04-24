import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Set page title and icon
st.set_page_config(page_title="For My Mithoo", page_icon="❤️", layout="wide")

# Function to encode local files to base64 (so they work online)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load Music and Photos
# Note: Ensure your mp3 is named 'our-song.mp3' and photos are in 'images/'
try:
    music_base64 = get_base64("our-song.mp3")
    music_html = f'<audio id="bg-music" loop><source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3"></audio>'
except:
    music_html = '<audio id="bg-music" loop></audio>'

# Generate Photo HTML tags
photo_tags = ""
if os.path.exists("images"):
    for i in range(1, 31):
        path = f"images/{i}.jpg"
        if os.path.exists(path):
            img_b64 = get_base64(path)
            photo_tags += f'<img src="data:image/jpg;base64,{img_b64}" alt="Memory">'

# The Full HTML/CSS/JS Interface
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@300;500&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary-pink: #ff4d6d; --soft-pink: #ffccd5; }}
        body {{ margin: 0; font-family: 'Quicksand', sans-serif; background: linear-gradient(135deg, #ffafbd, #ffc3a0); color: white; overflow-x: hidden; }}
        
        /* Floating Hearts */
        .heart-bg {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }}
        .heart {{ position: absolute; color: rgba(255, 77, 109, 0.6); animation: float 6s infinite linear; font-size: 20px; }}
        @keyframes float {{ 0% {{ transform: translateY(110vh); opacity: 1; }} 100% {{ transform: translateY(-10vh); opacity: 0; }} }}

        /* Password Screen */
        #pass-screen {{ position: fixed; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 100; background: rgba(0,0,0,0.3); backdrop-filter: blur(15px); }}
        .keypad {{ background: rgba(255,255,255,0.2); padding: 30px; border-radius: 20px; border: 1px solid white; text-align: center; }}
        .display {{ background: white; color: var(--primary-pink); padding: 10px; border-radius: 10px; margin-bottom: 20px; font-size: 24px; font-weight: bold; letter-spacing: 5px; }}
        .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
        button {{ width: 50px; height: 50px; border-radius: 50%; border: none; font-weight: bold; cursor: pointer; }}
        
        /* Main Content */
        #content {{ display: none; text-align: center; padding: 50px 20px; }}
        .heading {{ font-family: 'Dancing Script', cursive; font-size: 3.5rem; }}
        .photo-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 30px; }}
        .photo-grid img {{ width: 100%; border: 5px solid white; border-radius: 5px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }}
        .letter {{ background: white; color: #333; padding: 30px; border-radius: 10px; margin: 40px auto; max-width: 600px; text-align: left; line-height: 1.6; display: none; }}
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
        <p style="font-size: 1.5rem; margin-top: 40px;">Scroll down bubu... ⬇️</p>
        <button onclick="showLetter()" style="width: auto; height: auto; padding: 15px 30px; border-radius: 30px; background: #ff4d6d; color: white; margin-top: 20px;">Open My Letter ✉️</button>
        <div class="letter" id="let">
            I am sorry for not being a good boyfriend. <br><br>
            I love you so much bubu, I not taken you for granted bubu, bas ye hum door hai na, alag alag hogaya hamara sab, isiliye aisa hai, but I love you so much and I think about you everytime love, i JUST MISS YOU A LOTTTTT JALDI SE MERE PAAS AAAJAAOOOOOOOOOO
        </div>
    </div>

    <script>
        // Hearts
        setInterval(() => {{
            const h = document.createElement('div');
            h.className = 'heart'; h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            document.getElementById('hb').appendChild(h);
            setTimeout(() => h.remove(), 6000);
        }}, 300);

        // Keypad
        let pin = "";
        const keys = [1,2,3,4,5,6,7,8,9,'C',0,'✓'];
        keys.forEach(k => {{
            const b = document.createElement('button');
            b.innerText = k;
            b.onclick = () => {{
                if(k === 'C') pin = "";
                else if(k === '✓') {{
                    if(pin === "2424") {{
                        document.getElementById('bg-music').play();
                        document.getElementById('pass-screen').style.display = 'none';
                        document.getElementById('content').style.display = 'block';
                    }} else {{ alert("Wrong PIN!"); pin = ""; }}
                }} else if(pin.length < 4) {{ pin += k; }}
                document.getElementById('dis').innerText = "*".repeat(pin.length) || "****";
            }};
            document.getElementById('keys').appendChild(b);
        }});

        function showLetter() {{ document.getElementById('let').style.display = 'block'; window.scrollTo(0, document.body.scrollHeight); }}
    </script>
</body>
</html>
"""

components.html(html_code, height=2000, scrolling=True)
