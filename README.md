# 🛡️ APISpyder: Security Secret Scanner

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Security](https://img.shields.io/badge/security-OSINT-red)

**APISpyder** es una herramienta de análisis estático (SAST) diseñada para identificar de forma proactiva la exposición de credenciales, tokens y llaves de API dentro del código fuente. Su objetivo es prevenir fugas de información antes de que lleguen a entornos de producción.

---

## 🚀 Características

- 🔍 **Detección Multiservicio:** Identifica patrones de AWS, Google Cloud, Slack, Stripe y más.
- 📂 **Escaneo Recursivo:** Analiza directorios completos buscando archivos sensibles (`.env`, `.conf`, `.js`).
- 📊 **Análisis de Entropía:** Utiliza cálculos matemáticos para detectar cadenas aleatorias que no siguen un patrón fijo.
- 📝 **Reportes Claros:** Salida detallada con la ubicación exacta (archivo y línea) del hallazgo.

## 🛠️ Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/apispyder.git](https://github.com/tu-usuario/apispyder.git)
cd apispyder