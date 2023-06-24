import tkinter as tk
# Instalar pillow para interfaz grafica PIL
from PIL import ImageTk, Image
import requests
import json
import io

# Obtener la lista de géneros de la API
response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=6bd5e7fdf1de00d2f53c7a10a37ae32f&language=es")
genres_data = json.loads(response.text)["genres"]
genres_dict = {genre["id"]: genre["name"] for genre in genres_data}

# Obtener la lista de películas de la API
response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=6bd5e7fdf1de00d2f53c7a10a37ae32f&language=es")
movies_data = json.loads(response.text)["results"]
movies_list = [(movie["title"], movie["overview"], movie["original_language"], movie["release_date"], [genres_dict[genre_id] for genre_id in movie["genre_ids"]], movie["poster_path"]) for movie in movies_data]

# Crear la interfaz gráfica
window = tk.Tk()
window.title("Cinéfilos Argentinos")
window.geometry("1500x700")

main_frame = tk.Frame(window)
main_frame.grid(row=0, column=0, sticky="nsew")

title_listbox = tk.Listbox(main_frame, width=30, font=("Arial", 12))
title_listbox.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

info_frame = tk.Frame(main_frame)
info_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

title_label = tk.Label(info_frame, text="Título:", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, sticky="w")

overview_label = tk.Label(info_frame, text="Resumen:", font=("Arial", 14), wraplength=500, justify=tk.LEFT)
overview_label.grid(row=1, column=0, sticky="w", pady=10)

language_label = tk.Label(info_frame, text="Lenguaje:", font=("Arial", 14))
language_label.grid(row=2, column=0, sticky="w")

release_label = tk.Label(info_frame, text="Fecha de lanzamiento:", font=("Arial", 14))
release_label.grid(row=3, column=0, sticky="w")

genres_label = tk.Label(info_frame, text="Géneros:", font=("Arial", 14))
genres_label.grid(row=4, column=0, sticky="w")

poster_label = tk.Label(window)
poster_label.grid(row=0, column=1, sticky="nsew", padx=20, pady=10)

def show_movie_info(event):
    selection = title_listbox.curselection()
    if selection:
        movie = movies_list[selection[0]]
        title_label.config(text="Título: " + movie[0])
        overview_label.config(text="Resumen: " + movie[1])
        language_label.config(text="Lenguaje: " + movie[2])
        release_label.config(text="Fecha de lanzamiento: " + movie[3])
        genres_label.config(text="Géneros: " + ", ".join(movie[4]))
        
        # Cargar la imagen de la película
        response = requests.get(f"https://image.tmdb.org/t/p/w300{movie[5]}")
        if response.status_code == 200:
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((250, 375))  # Ajustar el tamaño de la imagen
            poster = ImageTk.PhotoImage(image)
            poster_label.config(image=poster)
            poster_label.image = poster  # Guardar una referencia para evitar que la imagen se borre de la memoria

title_listbox.bind("<Double-Button-1>", show_movie_info)

for movie in movies_list:
    title_listbox.insert(tk.END, movie[0])

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

window.mainloop()
