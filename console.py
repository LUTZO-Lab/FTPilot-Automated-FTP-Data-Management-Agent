import threading
import time

#small Test dor console logic


running = True
status_message = "Alles läuft!"

def custom_console():
    global running, status_message
    print("Eigene Konsole gestartet. Gib 'help' für Befehle ein.")
    while True:
        cmd = input("> ").strip()
        if cmd == "help":
            print("Verfügbare Befehle:")
            print("  status     - Zeigt den aktuellen Status")
            print("  stop       - Beendet das Programm")
            print("  say [msg]  - Gibt eine Nachricht aus")
        elif cmd == "status":
            print(f"Status: {status_message}")
        elif cmd.startswith("say "):
            print("Nachricht:", cmd[4:])
        elif cmd == "stop":
            print("Beende...")
            running = False
            break
        else:
            print("Unbekannter Befehl:", cmd)


def main_program():
    global status_message
    i = 0
    while running:
        status_message = f"Läuft seit {i} Sekunden..."
        time.sleep(1)
        i += 1

threading.Thread(target=custom_console, daemon=True).start()

main_program()
