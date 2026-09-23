```markdown
# SPEC.md

## 1. TECHNOLOGY STACK

- Python 3.x
- Flask

## 2. DATA CONTRACTS

**Request Model (JSON body):**
```json
{
  "producto": "nombre_del_producto",
  "cantidad": 1,
  "precio": 100.00
}
```

**Response Model (JSON):**
```json
{
  "producto": "nombre_del_producto",
  "cantidad": 1,
  "subtotal": 100.00,
  "iva": 16.00,
  "total": 116.00
}
```

## 3. API ENDPOINTS

- `POST /calcular`

## 4. FILE STRUCTURE

```
app.py
requirements.txt
```

## 5. ENVIRONMENT VARIABLES

None

## 6. IMPORT CONTRACTS

**app.py**
- `from flask import Flask, request, jsonify`
- `app = Flask(__name__)`
- `@app.route('/calcular', methods=['POST'])`

## 10. FUNCTIONAL REQUIREMENTS COVERAGE

| Requisito fuente | Criterio de aceptación | Archivo |
|------------------|------------------------|---------|
| "Crear un endpoint que reciba un producto y cantidad" | El endpoint acepta POST con producto, cantidad y precio en el body JSON | app.py |
| "Calcule el subtotal" | La respuesta incluye campo `subtotal` calculado como cantidad × precio | app.py |
| "Calcule el IVA" | La respuesta incluye campo `iva` calculado como subtotal × 0.16 | app.py |
| "Calcule el total" | La respuesta incluye campo `total` calculado como subtotal + iva | app.py |
| "Devuelva el resultado en JSON" | La respuesta es un objeto JSON con producto, cantidad, subtotal, iva y total | app.py |
```