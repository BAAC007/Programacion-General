Primero sacamos en terminal

listamos modelos disponibles de ollama list

Alternativa1: ollama pull qwen2.5-coder:7b

Alternativa2: Buscamos modelos en la web de ollama 

https://ollama.com/search

Primero vamos a hacer una pregunta en consola:

ollama run qwen2.5-coder:7b "Dame el codigo html y css de una web personal"

Restringimos el prompt:

ollama run qwen2.5-coder:7b "Dame el codigo HTML y CSS de una web personal. No me hagas introduccion ni salida, solo quiero el codigo sin fences. Hazme un single file. "