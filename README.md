# Ejercicio RSA

## Descripción del proyecto

Este proyecto implementa un sistema de cifrado híbrido utilizando criptografía asimétrica (RSA) y simétrica (AES-GCM). El objetivo es simular un escenario real donde se necesita proteger documentos confidenciales durante su transmisión.

El sistema funciona de la siguiente manera:

- Se genera un par de claves RSA (pública y privada).
- El documento se cifra utilizando AES-256 en modo GCM.
- La clave AES generada se cifra utilizando RSA-OAEP con la clave pública del destinatario.
- Todos los elementos necesarios para descifrar el documento se empaquetan en un solo objeto (`pkg`).
- El receptor utiliza su clave privada para recuperar la clave AES y luego descifrar el documento.

Este enfoque combina la eficiencia del cifrado simétrico con la seguridad del cifrado asimétrico, tal como se utiliza en sistemas reales como TLS.

## Instalación

### Clonar el repositorio

```bash
git clone <URL_DEL_REPO>
cd RSA_Cipher_Cdl
```

## Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

## Uso

### Generar claves RSA

```bash
python generar_claves.py
```

Esto generará:
- public_key.pem
- private_key.pem

Nota: La clave privada está protegida con la passphrase `lab04uvg`.

### Cifrado y descifrado con RSA-OAEP

```bash
python rsa_OAEP.py
```

Este script:
- cifra un mensaje con la clave pública
- lo descifra con la clave privada
- demuestra que el mismo mensaje cifrado dos veces produce resultados distintos

### Cifrado híbrido (RSA + AES-GCM)

```bash
python rsa_AES_GCM.py
```

Este script:
- cifra un documento utilizando AES-256-GCM
- cifra la clave AES con RSA
- empaqueta todo en un objeto pkg
- descifra el documento correctamente
- prueba el sistema con un archivo de 1 MB

## Ejemplos de ejecución

### RSA-OAEP
```bash
Original  : b'El mensaje sera la clave secreta de AES'
Cifrado   : 3b519037df1f45e4d9ec1e87e39313b32a1cba3cc68b7d901b909c436adc4af3...
Descifrado: b'El mensaje sera la clave secreta de AES'

c1 == c2: False
```

### Cifrado híbrido

```bash
Documento original : b'Contrato de confidencialidad No. 2025-GT-001'
Documento recuperado: b'Contrato de confidencialidad No. 2025-GT-001'
Archivo 1 MB: OK
```

### Nota de seguridad

La clave privada (private_key.pem) no debe compartirse ni subirse al repositorio, ya que permite descifrar toda la información protegida. Esta debe mantenerse únicamente en el entorno local del usuario.

## Respuesta Parte 1

El sistema usa RSA como mecanismo de intercambio de clave, protegiendo una clave AES que cifra el documento real. ¿Explique por qué no cifrar el documento directamente con RSA?

Realmente no se cifra un documento directamene con RSA porque este no está diseñado para cifrar grandes cantidades
de datos de manera eficiente. Aunque RSA sí puede cifrar datos, su uso principal es proteger pequeñas porciones de 
datos, como claves de cifrado, no fue diseñado para cifrar documentos completos.

Además RSA es significativamente más lento en comparación con algoritmos simétricos como AES, debido a que sus 
operaciones criptográficas involucran cálculos matemáticos complejos con números muy grandes. Otra limitación es que 
RSA solo puede cifrar mensajes donde el tamaño sea menor al de la clave. Por esta razón, RSA no es adecuado para cifrar archivos o documentos grandes.

## Respuesta Parte 2

¿Qué información contiene un archivo .pem? Abre public_key.pem con un editor de texto y
describe su estructura.

El archivo .pem contiene la información criptográfica codificada en texto para que pueda ser leída y compartida fácilmente. Al abrir
la public_key.pem logre ver que contiene un encabezado que indica que es una llave pública, seguido de un bloque de texto en Base64
que es la clave en sí, y al final un pie que marca el final de la llave. No es legible totalmente pero entre ese bloque se encuentran los datos de la clave pública RSA.

## Respuesta Parte 3

¿Porqué cifrar el mismo mensaje dos veces produce resultados distintos? Demuéstrenlo y
expliquen que propiedad de OAEP lo cause

Al cifrar el mismo mensaje dos veces con RSA-OAEP, se obtienen resultados distintos porque OAEP agrega aleatoriedad al proceso de cifrado. Esto hace que, aunque el mensaje y la clave pública sean los mismos, cada salida cifrada sea diferente, lo cual mejora la seguridad al evitar patrones repetidos.
