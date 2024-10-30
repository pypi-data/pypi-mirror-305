import psutil


def stop_vr_bridge(port=12740):
    # Iterate over all active connections
    for conn in psutil.net_connections():
        # Check if the connection is using the specified port
        if conn.laddr.port == port:
            # Get the process ID (PID) of the connection
            pid = conn.pid
            if pid is not None:
                # Terminate the process using the PID
                process = psutil.Process(pid)
                process.terminate()
                process.wait()
                print(f"Process {pid} terminated successfully.")
                return
    print(f"No process found using port {port}.")


if __name__ == "__main__":
    # Specify the port to kill the process
    stop_vr_bridge()
