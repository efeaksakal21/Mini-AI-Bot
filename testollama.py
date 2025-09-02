import ollama

print("Kod başladı!")  # ilk test için

response = ollama.chat(
    model="llama2:7b",   # ✅ doğru model adı
    messages=[
        {"role": "user", "content": "Merhaba! Nasılsın?"}
    ],
    options={"num_predict": 100}
)

print("Cevap geldi!")  # ikinci test için
print(response)         # tüm çıktıyı ham haliyle yazdır
