# Usa la imagen base de Ubuntu 16.10
FROM ubuntu:20.10

# Copia el archivo sources.list
COPY sources.list /etc/apt/sources.list

# Actualiza el paquete apt e instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    tshark \
    openssh-client \
    openssh-server \
    whois

# Crea el directorio para sshd
RUN mkdir -p /var/run/sshd

# Permite el inicio de sesión root
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Exponer el puerto 22
EXPOSE 22

# Comando para iniciar sshd
CMD ["/usr/sbin/sshd", "-D"]
