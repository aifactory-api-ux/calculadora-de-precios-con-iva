# DEVELOPMENT PLAN: Calculadora de Precios con IVA

## 1. ARCHITECTURE OVERVIEW
Proyecto Flask simple con un único endpoint POST `/calcular` que recibe datos de producto en JSON, calcula subtotal (cantidad × precio), IVA (subtotal × 0.16) y total, devolviendo el resultado en formato JSON.

## 2. ACCEPTANCE CRITERIA
1. El endpoint `POST /calcular` acepta body JSON con `producto`, `cantidad` y `precio`
2. Calcula `subtotal` = cantidad × precio
3. Calcula `iva` = subtotal × 0.16
4. Calcula `total` = subtotal + iva
5. Devuelve JSON con `producto`, `cantidad`, `subtotal`, `iva` y `total`

## TEAM SCOPE
- `role-be` (backend_developer)

## 3. EXECUTABLE ITEMS

### ITEM 1: Implementar endpoint POST /calcular
**Goal:** Crear endpoint que reciba producto, cantidad y precio; calcule subtotal, IVA y total; devuelva resultado en JSON

**Files to create:**
- `app.py`
- `requirements.txt`

**Dependencies:** None

**Validation:**
```bash
# Ejecutar la aplicación
python app.py

# Probar endpoint (en otra terminal)
curl -X POST http://localhost:5000/calcular \
  -H "Content-Type: application/json" \
  -d '{"producto": "Laptop", "cantidad": 2, "precio": 15000.00}'

# Respuesta esperada:
# {
#   "producto": "Laptop",
#   "cantidad": 2,
#   "subtotal": 30000.0,
#   "iva": 4800.0,
#   "total": 34800.0
# }
```

**Role:** role-be (backend_developer)