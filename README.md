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
git clone https://github.com/tu-usuario/apispyder.git
cd apispyder
```
### 2. Preparar el entorno virtual
```bash
# Crear el entorno
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Activar (Linux/Mac)
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
# Dependencias de desarrollo e investigación
pip install -r requirements_dev.txt
```

## 💻 Uso

Una vez instalado, puedes ejecutar el scanner de la siguiente manera:

```bash
python src/main.py --path <directorio>
```

### Ejemplo:
```bash
python src/main.py --path ./proyecto
```

La herramienta escaneará recursivamente el directorio especificado buscando credenciales, tokens y llaves de API expuestas.

## 📋 Capacidades de Detección

| Servicio     | Tipo de Credencial        | Método de Detección   |
|-------------|--------------------------|----------------------|
| **AWS**     | Access Key ID / Secret   | Regex / Patrones fijos |
| **Google Cloud** | API Keys / OAuth     | Regex                |
| **Stripe**  | Publishable & Secret Keys | Regex               |
| **Genérico**| Contraseñas / Tokens     | Alta Entropía        |

## 📋 Estado del Proyecto

**APISpyder** se encuentra en **fase inicial de desarrollo**. Las funcionalidades básicas están en construcción y se irán añadiendo gradualmente.

## 📈 Hoja de Ruta (Roadmap)

- [ ] Integración con más servicios (GitHub, Azure, Twilio, etc.)
- [ ] Exportación de reportes en JSON y HTML
- [ ] Integración con GitHub Actions para CI/CD
- [ ] Configuración personalizada de patrones de detección
- [ ] Filtrado de falsos positivos
- [ ] Tests automatizados

## 📝 Licencia

Este proyecto está licenciado bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## ⚠️ Aviso Legal

**IMPORTANTE:** Esta herramienta ha sido creada exclusivamente con fines educativos y de auditoría de seguridad ética. El autor no se hace responsable del uso indebido de este software ni de los daños que puedan derivarse de su aplicación en sistemas sin autorización previa.

Esta es una herramienta de **código abierto** para el análisis de seguridad. Úsala responsablemente y solo en sistemas donde tengas permiso explícito.