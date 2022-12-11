def start_listening_tcp_socket(http_server: HTTPServer) -> None:
    call_count = 0

    port = None
    while call_count < MAX_PORT_SEARCH_RETRIES:
        address = config.get_option("server.address")
        port = config.get_option("server.port")

        try:
            http_server.listen(port, address)
            break  # It worked! So let's break out of the loop.

        except (OSError, socket.error) as e:
            if e.errno == errno.EADDRINUSE:
                if server_port_is_manually_set():
                    LOGGER.error("Port %s is already in use", port)
                    sys.exit(1)
                else:
                    LOGGER.debug(
                        "Port %s already in use, trying to use the next one.", port
                    )
                    port += 1
                    # Save port 3000 because it is used for the development
                    # server in the front end.
                    if port == 3000:
                        port += 1

                    config.set_option(
                        "server.port", port, ConfigOption.STREAMLIT_DEFINITION
                    )
                    call_count += 1
            else:
                raise