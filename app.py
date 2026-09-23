"""
Calculadora de Precios con IVA
Endpoint POST /calcular para calcular precios con IVA
"""
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calcular', methods=['POST'])
def calcular():
    """
    Calcula el subtotal, IVA y total para un producto.
    
    Request body JSON:
        producto (str): Nombre del producto
        cantidad (int): Cantidad del producto
        precio (float): Precio unitario del producto
    
    Returns:
        JSON con producto, cantidad, subtotal, iva y total
    """
    data = request.get_json()
    
    producto = data.get('producto')
    cantidad = data.get('cantidad')
    precio = data.get('precio')
    
    if producto is None or cantidad is None or precio is None:
        return jsonify({'error': 'Faltan campos requeridos: producto, cantidad, precio'}), 400
    
    if not isinstance(cantidad, int) or cantidad <= 0:
        return jsonify({'error': 'La cantidad debe ser un entero positivo'}), 400
    
    if not isinstance(precio, (int, float)) or precio <= 0:
        return jsonify({'error': 'El precio debe ser un numero positivo'}), 400
    
    subtotal = cantidad * precio
    iva = subtotal * 0.16
    total = subtotal + iva
    
    return jsonify({
        'producto': producto,
        'cantidad': cantidad,
        'subtotal': subtotal,
        'iva': iva,
        'total': total
    }), 200


@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    
    Returns:
        JSON con estado del servicio
    """
    return jsonify({
        'status': 'healthy',
        'service': 'calculadora-iva',
        'version': '1.0.0'
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
