from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r, g, b = g ^ key, b ^ key, r ^ key

            pixels[x, y] = (r, g, b)

    img.save(output_path)
    print("✅ Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r, g, b = b ^ key, r ^ key, g ^ key

            pixels[x, y] = (r, g, b)

    img.save(output_path)
    print("✅ Image decrypted successfully!")
print("---- IMAGE ENCRYPTION / DECRYPTION TOOL ----")

choice = input("Enter 'e' to Encrypt or 'd' to Decrypt: ").lower()

input_path = input("Enter input image path: ")
output_path = input("Enter output image path: ")

key = int(input("Enter encryption key (0–255): "))

if choice == 'e':
    encrypt_image(input_path, output_path, key)

elif choice == 'd':
    decrypt_image(input_path, output_path, key)

else:
    print("❌ Invalid option! Please choose 'e' or 'd'.")
