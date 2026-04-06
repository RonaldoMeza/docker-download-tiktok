from flask import Flask, request, send_file, render_template_string
import subprocess
import uuid
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Descargar TikTok</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #0f172a;
            color: white;
            padding: 50px;
        }
        input {
            width: 60%;
            padding: 10px;
            border-radius: 5px;
            border: none;
        }
        button {
            padding: 10px 20px;
            background: #22c55e;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #16a34a;
        }
    </style>
</head>
<body>
    <h1>⬇️ Descargar video de TikTok</h1>
    <form method="post" action="/download">
        <input type="text" name="url" placeholder="Pega URL de TikTok" required>
        <br><br>
        <button type="submit">Descargar</button>
    </form>
    <p style="color:red;">{{ error }}</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, error="")

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')

    if not url:
        return render_template_string(HTML, error="❌ URL inválida")

    filename = f"video_{uuid.uuid4()}.mp4"

    try:
        # Ejecutar yt-dlp correctamente
        result = subprocess.run(
            ["yt-dlp", "-o", filename, url],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return render_template_string(HTML, error="❌ Error descargando video")

        if not os.path.exists(filename):
            return render_template_string(HTML, error="❌ No se generó el archivo")

        return send_file(filename, as_attachment=True)

    except Exception as e:
        return render_template_string(HTML, error=f"❌ Error: {str(e)}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
