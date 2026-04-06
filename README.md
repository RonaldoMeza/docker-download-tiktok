# 🎬 TikTok Video Downloader - Docker

Aplicación web desarrollada con Flask que permite descargar videos de TikTok utilizando contenedores Docker.

---

## 🚀 Tecnologías utilizadas

* Python 3.11
* Flask
* yt-dlp
* Docker

---

## 📦 Clonar repositorio

```bash
git clone https://github.com/RonaldoMeza/docker-download-tiktok.git
cd docker-download-tiktok
```

---

## 🐳 Construir imagen Docker

```bash
docker build -t tiktok-app:v1 .
```

---

## ▶️ Ejecutar contenedor

```bash
docker run -d -p 5000:5000 --name tiktok-container tiktok-app:v1
```

---

## 🌐 Acceder a la aplicación

Abrir en navegador:

```
http://localhost:5000
```

O en servidor EC2:

```
http://IP-PUBLICA:5000
```

---

## 📥 Uso

1. Pegar URL de TikTok
2. Click en "Descargar"
3. Se descarga automáticamente el video

---

## 🧠 Dockerfiles incluidos

* Dockerfile (básico)
* Dockerfile.optimizado
* Dockerfile.multistage

---

## ⚠️ Notas

* Algunos videos pueden fallar si TikTok restringe acceso
* Se recomienda usar videos públicos

---

## 📌 Autor

Ronaldo Meza - Desarrollado como práctica de laboratorio de Contenedores y Microservicios
