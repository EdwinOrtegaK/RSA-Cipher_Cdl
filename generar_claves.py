from Crypto.PublicKey import RSA

def generar_par_claves(bits: int = 3072):
    if bits < 2048:
        raise ValueError("RSA requiere al menos 2048 bits por seguridad.")
    
    # Generar clave privada RSA
    private_key = RSA.generate(bits)

    # Obtener clave publica a partir de la privada
    public_key = private_key.publickey()

    # Exportar clave privada protegida
    private_pem = private_key.export_key(
        format="PEM",
        passphrase="lab04uvg",
        pkcs=8,
        protection="scryptAndAES128-CBC"
    )

    # Exportar clave publica en formato PEM
    public_pem = public_key.export_key(format="PEM")

    # Guardar archivos
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_pem)

    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_pem)

if __name__ == '__main__':
    generar_par_claves(3072)
    print("Claves generadas: private_key.pem y public_key.pem")