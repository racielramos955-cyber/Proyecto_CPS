# 🌐 Cómo Compartir la Aplicación en Red Local

Esta guía te ayudará a compartir NutriLife con otros dispositivos en tu red local (móviles, tablets, otras computadoras).

---

## 📋 Requisitos Previos

1. ✅ Backend y Frontend funcionando correctamente
2. ✅ Todos los dispositivos conectados a la misma red Wi-Fi/Ethernet
3. ✅ Firewall de Windows permitiendo conexiones entrantes (lo configuraremos)

---

## 🔍 Paso 1: Obtener Tu IP Local

### Método 1: Desde PowerShell

```powershell
ipconfig | findstr /i "IPv4"
```

Busca la IP que comienza con `192.168.x.x` o `10.x.x.x` (normalmente la que NO es `192.168.106.1` ni `192.168.35.1`).

**Ejemplo:** `192.168.1.8`

### Método 2: Desde Configuración de Windows

1. Presiona `Win + I`
2. Ve a "Red e Internet" → "Wi-Fi" o "Ethernet"
3. Haz clic en tu conexión activa
4. Busca "Dirección IPv4"

---

## 🔧 Paso 2: Configurar Firewall de Windows

Necesitas permitir que otros dispositivos accedan a los puertos 5000 y 8000.

### Opción A: Desde PowerShell (Como Administrador)

```powershell
# Permitir puerto 5000 (Backend)
New-NetFirewallRule -DisplayName "NutriLife Backend" -Direction Inbound -LocalPort 5000 -Protocol TCP -Action Allow

# Permitir puerto 8000 (Frontend)
New-NetFirewallRule -DisplayName "NutriLife Frontend" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow
```

### Opción B: Desde Interfaz Gráfica

1. Presiona `Win + R`, escribe `wf.msc` y presiona Enter
2. Haz clic en "Reglas de entrada" → "Nueva regla..."
3. Selecciona "Puerto" → Siguiente
4. Selecciona "TCP" y "Puertos locales específicos": `5000,8000`
5. Selecciona "Permitir la conexión"
6. Marca todos los perfiles (Dominio, Privada, Pública)
7. Nombre: "NutriLife - Backend y Frontend"
8. Finalizar

---

## 🚀 Paso 3: Iniciar Servidores con Acceso de Red

### Opción A: Usar Scripts Mejorados (Recomendado)

He creado scripts que automáticamente detectan tu IP y la muestran.

**Backend:**
```powershell
.\iniciar_backend_red_local.ps1
```

**Frontend:**
```powershell
.\iniciar_frontend_red_local.ps1
```

### Opción B: Manual

**Backend (Terminal 1):**
```powershell
cd "C:\Proyecto IA\IBM_Inteligente"
.venv\Scripts\Activate.ps1
python backend\app.py
```

El backend ya está configurado para escuchar en `0.0.0.0`, así que aceptará conexiones desde cualquier IP.

**Frontend (Terminal 2):**
```powershell
cd "C:\Proyecto IA\IBM_Inteligente\frontend"
python -m http.server 8000 --bind 0.0.0.0
```

El `--bind 0.0.0.0` hace que el servidor HTTP escuche en todas las interfaces de red.

---

## 📱 Paso 4: Acceder desde Otros Dispositivos

Una vez que ambos servidores estén corriendo, otros dispositivos pueden acceder usando:

**Frontend:**
```
http://TU_IP:8000
```

**Ejemplo:**
```
http://192.168.1.8:8000
```

**Backend (solo para pruebas):**
```
http://TU_IP:5000
```

---

## 🔗 Paso 5: Actualizar URL del Backend en el Frontend

El frontend necesita saber la IP del backend. Hay dos opciones:

### Opción A: Cambiar la URL en el código (si conoces tu IP)

Edita `frontend/index.html` línea 286:

```javascript
// Cambiar de:
const API_URL = "http://localhost:5000/api";

// A (usando tu IP):
const API_URL = "http://192.168.1.8:5000/api";
```

### Opción B: Detectar automáticamente (Recomendado)

He actualizado el código para detectar automáticamente si estás accediendo desde otra IP y ajustar la URL del backend.

---

## 🧪 Paso 6: Probar la Conexión

### Desde tu computadora:
1. Abre el navegador
2. Ve a: `http://TU_IP:8000`
3. Debería funcionar igual que `localhost:8000`

### Desde otro dispositivo:
1. Conéctalo a la misma red Wi-Fi
2. Abre el navegador
3. Ve a: `http://TU_IP:8000`
4. Debería cargar la aplicación

---

## ⚠️ Solución de Problemas

### Error: "No se puede acceder a este sitio"

**Solución:**
- Verifica que ambos servidores estén corriendo
- Verifica que estés usando la IP correcta
- Verifica que el firewall permita las conexiones
- Asegúrate de que el dispositivo esté en la misma red

### Error: "Failed to fetch" en el frontend

**Solución:**
- El frontend no puede conectar con el backend
- Verifica que el backend esté corriendo
- Verifica que la IP del backend sea correcta
- Verifica el firewall de Windows

### El frontend carga pero no funciona

**Solución:**
- Verifica que la URL del API en el frontend use la IP correcta
- Abre la consola del navegador (F12) para ver errores
- Verifica que CORS esté configurado correctamente

### No puedo encontrar mi IP

**Solución:**
```powershell
# Obtener solo la IP principal
(Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -like "192.168.*" -or $_.IPAddress -like "10.*"} | Select-Object -First 1).IPAddress
```

---

## 🔒 Seguridad

⚠️ **Importante:** Estos servidores están configurados para desarrollo. No los expongas a Internet sin protección adicional.

- ✅ Solo funcionan en tu red local
- ✅ No son accesibles desde Internet (si tu router está configurado correctamente)
- ✅ Para producción, usa un servidor web profesional (Nginx, Apache) con HTTPS

---

## 📝 Ejemplo Completo

Supongamos que tu IP es `192.168.1.8`:

1. **Inicia el backend:**
   ```powershell
   python backend\app.py
   ```
   Deberías ver: `Running on http://0.0.0.0:5000`

2. **Inicia el frontend:**
   ```powershell
   cd frontend
   python -m http.server 8000 --bind 0.0.0.0
   ```
   Deberías ver: `Serving HTTP on 0.0.0.0 port 8000`

3. **Desde tu móvil/tablet:**
   - Abre el navegador
   - Ve a: `http://192.168.1.8:8000`
   - ¡La aplicación debería cargar!

---

## 💡 Tips Adicionales

- **IP Dinámica:** Si tu IP cambia, tendrás que actualizar la URL en los dispositivos
- **Nombre de Host:** Algunos routers permiten usar un nombre en lugar de IP (ej: `nutrilife.local`)
- **QR Code:** Puedes generar un QR code con la URL para que otros la escaneen fácilmente

---

**¡Listo! Ahora puedes compartir tu aplicación con otros dispositivos en tu red local.** 🎉

