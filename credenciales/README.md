# 🔐 Credenciales y Configuración del Proyecto

**⚠️ IMPORTANTE: Esta carpeta contiene información sensible. NO subir a GitHub.**

Esta carpeta contiene todas las credenciales, claves y configuraciones necesarias para que el proyecto funcione correctamente.

---

## 📁 Archivos Incluidos

### 1. `backend.env`
**Ubicación original:** `backend/.env`

**Contiene:**
- `PINATA_JWT`: Token JWT de Pinata para subir archivos a IPFS

**Cómo usar:**
1. Copia este archivo a `backend/.env`
2. Asegúrate de que el nombre del archivo sea exactamente `.env` (sin el prefijo "backend")

**Ejemplo:**
```bash
# En Windows PowerShell:
Copy-Item credenciales\backend.env backend\.env
```

---

### 2. `contract-config.js`
**Ubicación original:** `frontend/js/contract-config.js`

**Contiene:**
- Dirección del contrato inteligente deployado en Sepolia Testnet
- Configuración de red (Sepolia)
- ABI del contrato (cargado desde NutriLifeABI.json)

**Información del contrato:**
- **Dirección:** `0xcb726f3e59518C7b24c74FB7279aA4554927D4A1`
- **Red:** Sepolia Testnet (Chain ID: 11155111)
- **Deployado en:** Block 9857790
- **Verificado en:** Sourcify, Blockscout, Routescan

**Cómo usar:**
1. Copia este archivo a `frontend/js/contract-config.js`
2. Reemplaza el archivo existente

**Ejemplo:**
```bash
# En Windows PowerShell:
Copy-Item credenciales\contract-config.js frontend\js\contract-config.js
```

---

### 3. `NutriLifeABI.json`
**Ubicación original:** `frontend/js/NutriLifeABI.json`

**Contiene:**
- ABI (Application Binary Interface) del contrato inteligente NutriLife
- Necesario para interactuar con el contrato desde el frontend

**Cómo usar:**
1. Copia este archivo a `frontend/js/NutriLifeABI.json`
2. Reemplaza el archivo existente

**Ejemplo:**
```bash
# En Windows PowerShell:
Copy-Item credenciales\NutriLifeABI.json frontend\js\NutriLifeABI.json
```

---

## 🚀 Instrucciones de Instalación

### Paso 1: Configurar Backend

```bash
# Copiar archivo .env al backend
Copy-Item credenciales\backend.env backend\.env
```

### Paso 2: Configurar Frontend

```bash
# Copiar configuración del contrato
Copy-Item credenciales\contract-config.js frontend\js\contract-config.js

# Copiar ABI del contrato
Copy-Item credenciales\NutriLifeABI.json frontend\js\NutriLifeABI.json
```

### Paso 3: Verificar

1. **Backend:** Verifica que `backend/.env` existe y contiene `PINATA_JWT`
2. **Frontend:** Verifica que los archivos en `frontend/js/` están actualizados

---

## 🔒 Seguridad

- ✅ Esta carpeta NO debe subirse a GitHub
- ✅ Los archivos originales están protegidos por `.gitignore`
- ✅ Comparte esta carpeta solo con personas de confianza
- ✅ Si compartes por error, regenera todas las claves inmediatamente

---

## 📝 Notas Adicionales

### Si necesitas regenerar credenciales:

1. **PINATA_JWT:**
   - Ve a: https://app.pinata.cloud/developers/api-keys
   - Crea una nueva API Key
   - Copia el JWT token
   - Actualiza `backend/.env`

2. **Contrato:**
   - Si redeployas el contrato, actualiza la dirección en `contract-config.js`
   - La dirección actual es: `0xcb726f3e59518C7b24c74FB7279aA4554927D4A1`

---

**Última actualización:** Diciembre 2025

