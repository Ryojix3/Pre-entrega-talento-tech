# 🧪 Pre-Entrega — Automatización de Testing Web

Proyecto de automatización de pruebas sobre [SauceDemo](https://www.saucedemo.com) utilizando **Selenium WebDriver** y **Python**, desarrollado como pre-entrega del curso.

---

## 📋 Descripción del proyecto

Este proyecto demuestra la capacidad de automatizar pruebas funcionales en una aplicación web real. Se implementan casos de prueba para las funcionalidades principales del sitio: autenticación, catálogo de productos e interacción con el carrito de compras.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.10+ | Lenguaje principal |
| Selenium WebDriver | 4.18.1 | Automatización del navegador |
| pytest | 8.1.1 | Framework de testing |
| pytest-html | 4.1.1 | Generación de reportes HTML |
| webdriver-manager | 4.0.1 | Gestión automática de ChromeDriver |

---

## 📁 Estructura del proyecto

```
pre-entrega-testing/
│
├── tests/
│   ├── test_login.py          # Caso 1: Autenticación de usuario
│   ├── test_catalogo.py       # Caso 2: Navegación y verificación del catálogo
│   └── test_carrito.py        # Caso 3: Interacción con productos y carrito
│
├── pages/                     # Page Object Model
│   ├── login_page.py          # Elementos y acciones de la página de login
│   ├── inventory_page.py      # Elementos y acciones del catálogo
│   └── cart_page.py           # Elementos y acciones del carrito
│
├── conftest.py                # Configuración y fixtures compartidos de pytest
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
```

---

## ⚙️ Instalación de dependencias

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/pre-entrega-testing.git
cd pre-entrega-testing
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> **Nota:** No es necesario instalar ChromeDriver manualmente. `webdriver-manager` lo descarga automáticamente.

---

## ▶️ Cómo ejecutar las pruebas

### Ejecutar todos los tests

```bash
pytest tests/
```

### Ejecutar un archivo específico

```bash
pytest tests/test_login.py
pytest tests/test_catalogo.py
pytest tests/test_carrito.py
```

### Ejecutar con salida detallada

```bash
pytest tests/ -v
```

### Generar reporte HTML

```bash
pytest tests/ --html=reporte.html --self-contained-html
```

El reporte se genera en la raíz del proyecto como `reporte.html`.

---

## 🧪 Casos de prueba implementados

### 1. Autenticación de Login (`test_login.py`)
| Test | Descripción |
|---|---|
| `test_login_exitoso` | Verifica redirección a `/inventory.html` con credenciales válidas |
| `test_validacion_con_credenciales_invalidas` | Verifica mensaje de error con credenciales incorrectas |
| `test_login_redirige_a_pagina_correcta` | Verifica que el título de la página sea correcto |

### 2. Catálogo de Productos (`test_catalogo.py`)
| Test | Descripción |
|---|---|
| `test_titulo_pagina_es_correcto` | Verifica que el título sea "Products" |
| `test_hay_productos_visibles` | Verifica que haya al menos 1 producto |
| `test_productos_tienen_nombre` | Verifica nombres no vacíos en todos los productos |
| `test_productos_tienen_precio` | Verifica precios con formato `$X.XX` |
| `test_dropdown_de_filtro_es_visible` | Verifica presencia del ordenamiento |

### 3. Carrito de Compras (`test_carrito.py`)
| Test | Descripción |
|---|---|
| `test_agregar_producto_actualiza_contador` | Verifica que el badge del carrito muestre "1" |
| `test_producto_aparece_en_carrito` | Verifica que el producto agregado aparezca en el carrito |
| `test_carrito_tiene_un_item` | Verifica que haya exactamente 1 ítem en el carrito |

---

## 🔑 Credenciales de prueba

| Usuario | Contraseña |
|---|---|
| `standard_user` | `secret_sauce` |

---

## 📊 Reporte de pruebas

Para generar el reporte HTML ejecutar:

```bash
pytest tests/ --html=reporte.html --self-contained-html
```

Luego abrir `reporte.html` en cualquier navegador.
