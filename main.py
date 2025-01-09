from fastapi.middleware.cors import CORSMiddleware #para permitir el acceso a la API desde cualquier origen

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os #para interactuar con el sistema operativo



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, WS, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gym FitLife</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f5f5f5;
                color: #333;
            }
            nav {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                text-align: center;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                font-weight: bold;
            }
            header {
                background-color: #4CAF50;
                color: white;
                text-align: center;
                padding: 20px;
            }
            header h1 {
                margin: 0;
                font-size: 2em;
            }
            .container {
                padding: 20px;
            }
            h2 {
                color: #4CAF50;
            }
            .plan {
                margin: 10px 0;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #fff;
            }
            footer {
                text-align: center;
                background-color: #333;
                color: white;
                padding: 10px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="#services">Servicios</a>
            <a href="#plans">Planes</a>
            <a href="#contact">Contacto</a>
        </nav>
        <header>
            <h1>Bienvenido a Gym FitLife</h1>
        </header>
        <div class="container">
            <section id="services">
                <h2>Servicios</h2>
                <ul>
                    <li>Entrenamiento personalizado</li>
                    <li>Clases grupales (Yoga, Zumba, Spinning)</li>
                    <li>Área de pesas y máquinas modernas</li>
                    <li>Asesoramiento nutricional</li>
                </ul>
            </section>
            <section id="plans">
                <h2>Planes</h2>
                <div class="plan">
                    <h3>Plan Básico</h3>
                    <p>Acceso al gimnasio de lunes a viernes.</p>
                    <p><strong>$20/mes</strong></p>
                </div>
                <div class="plan">
                    <h3>Plan Avanzado</h3>
                    <p>Acceso ilimitado + clases grupales.</p>
                    <p><strong>$35/mes</strong></p>
                </div>
                <div class="plan">
                    <h3>Plan Premium</h3>
                    <p>Todo incluido + asesoramiento personalizado.</p>
                    <p><strong>$50/mes</strong></p>
                </div>
            </section>
        </div>
        <footer>
            <p>&copy; 2024 Gym FitLife</p>
        </footer>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
