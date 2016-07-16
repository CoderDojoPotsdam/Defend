#include <iostream>
#include <string.h>
#ifdef __linux__
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#elif WIN32
#error Not ready for Windows
#endif

#define PORT 1234

int main() {
    std::cout << "Starting Defend Server" << std::endl;
    // create socket
    int m_socket = socket(AF_INET, SOCK_STREAM, 0);

    // address
    struct sockaddr_in server;
    memset(&server, 0, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    server.sin_addr.s_addr = htonl(INADDR_ANY);

    struct sockaddr_in client;
    int client_socket;
    socklen_t len;

    // listen
    if (listen(m_socket, 5) == -1) {
        std::cout << "Error while listening" << std::endl;
        close(m_socket);
        return -1;
    }

    // main loop
    for (;;) {
        len = sizeof(client);
        client_socket = accept(m_socket, (struct sockaddr*)&client, len);
        if (client_socket < 0) {
            // error
            std::cout << "Error while connecting to client" << std::endl;
            close(m_socket);
            return -1;
        }
        send(client_socket, "5", sizeof("5"), 0);
        std::cout << "Msg sended" << std::endl;
        break;
    }

    // close socket
    close(m_socket);
    return 0;
}
