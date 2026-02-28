# ⚡ Guía Rápida: Compartir en Red Local

## 🚀 Inicio Rápido (3 pasos)

### 1️⃣ Configurar Firewall

Ejecuta esto en PowerShell **como Administrador**:

```powershell
New-NetFirewallRule -DisplayName "NutriLife" -Direction Inbound -LocalPort 5000,8000 -Protocol TCP -Action Allow
```

### 2️⃣ Obtener Tu IP Local

```powershell
ipconfig | findstr /i "IPv4"
```

Busca la IP que NO sea `192.168.106.1` ni `192.168.35.1`.

**Ejemplo:** `192.168.1.8`

### 3️⃣ Iniciar Servidores

**Opción A: Script Automático (Más Fácil)**
```powershell
.\iniciar_todo_red_local.bat
```

**Opción B: Manual**

Terminal 1 - Backend:
```powershell
.\iniciar_backend_red_local.ps1
```

Terminal 2 - Frontend:
```powershell
.\iniciar_frontend_red_local.ps1
```

---

## 📱 Acceder desde Otros Dispositivos

Una vez iniciado, abre en el navegador del otro dispositivo:

```
http://TU_IP:8000
```

**Ejemplo:** `http://192.168.1.8:8000`

---

## ✅ Verificación

- ✅ Backend muestra: "Running on http://0.0.0.0:5000"
- ✅ Frontend muestra: "Serving HTTP on 0.0.0.0 port 8000"
- ✅ Otros dispositivos pueden acceder usando tu IP

---

## 🔧 Si No Funciona

1. **Verifica Firewall:** Asegúrate de haber ejecutado el comando del firewall
2. **Verifica Red:** Todos los dispositivos deben estar en la misma Wi-Fi
3. **Verifica IP:** Usa la IP correcta (no localhost)
4. **Verifica Puertos:** Los puertos 5000 y 8000 deben estar libres

---

**Para más detalles, consulta:** `COMPARTIR_EN_RED_LOCAL.md`

