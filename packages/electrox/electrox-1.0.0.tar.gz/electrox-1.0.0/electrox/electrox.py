import tkinter as tk
from tkinter import messagebox
import socket
import threading

class GameObject:
    def __init__(self, name):
        self.name = name
        self.position = {"x": 0, "y": 0}

    def move(self, direction):
        if direction == "left":
            self.position["x"] -= 1
        elif direction == "right":
            self.position["x"] += 1
        elif direction == "up":
            self.position["y"] -= 1
        elif direction == "down":
            self.position["y"] += 1
        else:
            raise ValueError("srry this code can't ate right now, invalid direction.")

    def __repr__(self):
        return f"GameObject(name={self.name}, position={self.position})"


class Electrox:
    def __init__(self):
        self.objects = {}
        self.server_socket = None
        self.clients = []

    def create_player(self, name):
        if name in self.objects:
            raise ValueError("This code is sooo skibidi fix it, player name already exists.")
        self.objects[name] = GameObject(name)
        return self.objects[name]

    def move_player(self, name, direction):
        if name not in self.objects:
            raise ValueError("Oops, can't find that player—this code is low-key sus.")
        player = self.objects[name]
        player.move(direction)
        return player.position

    def create_game_object(self, name):
        if name in self.objects:
            raise ValueError("This object is giving major 'already exists' vibes, try another name.")
        self.objects[name] = GameObject(name)
        return self.objects[name]

    def get_object_position(self, name):
        if name not in self.objects:
            raise ValueError("Object not found—definitely a 'this isn't it' moment.")
        return self.objects[name].position

    def list_objects(self):
        if not self.objects:
            raise ValueError("No objects to show—this is dry fr.")
        return list(self.objects.keys())

    def create_game(self, name, window_size):
        window_sizes = {
            "small": (400, 400),
            "medium": (600, 600),
            "max": (800, 800)
        }

        if window_size not in window_sizes:
            raise ValueError("This window size is sooo not the move, choose small, medium, or max.")

        root = tk.Tk()
        root.title(name)
        width, height = window_sizes[window_size]

        # Apply circular window look
        root.geometry(f"{width}x{height}")
        root.overrideredirect(True)  # Remove window decorations

        canvas = tk.Canvas(root, width=width, height=height)
        canvas.create_oval(0, 0, width, height, outline="#000", fill="#F0F0F0")
        canvas.pack()

        # Create a close button
        close_button = tk.Button(root, text="Close", command=root.quit)
        close_button.place(x=width // 2 - 40, y=height - 50)

        root.mainloop()

    # Socket server functionality
    def start_server(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server started at {host}:{port}, waiting for connections...")

        threading.Thread(target=self._accept_clients).start()

    def _accept_clients(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address}")
            self.clients.append(client_socket)
            threading.Thread(target=self._handle_client, args=(client_socket,)).start()

    def _handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Received message: {message}")
                self._broadcast(message, client_socket)
            except:
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def _broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    self.clients.remove(client)
