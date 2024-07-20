from octoai.util import to_file, from_file
from octoai.client import OctoAI

if __name__ == "__main__":
    client = OctoAI()

    client = OctoAI(
    api_key="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNkMjMzOTQ5In0.eyJzdWIiOiI3MGFmZGRlYi04YTU4LTQ3MTUtOTQzYi1iYzFmYTJlNDdkOWYiLCJ0eXBlIjoidXNlckFjY2Vzc1Rva2VuIiwidGVuYW50SWQiOiJmNGE5ZWIxNi1kNzA5LTRmZWEtYmFjZC02MzExNGM0ZjQ0MjciLCJ1c2VySWQiOiJmODhhNjNkZC01YmM0LTQ3MzctYWY1MC1kMWRhYzdiZjFiN2YiLCJhcHBsaWNhdGlvbklkIjoiYTkyNmZlYmQtMjFlYS00ODdiLTg1ZjUtMzQ5NDA5N2VjODMzIiwicm9sZXMiOlsiRkVUQ0gtUk9MRVMtQlktQVBJIl0sInBlcm1pc3Npb25zIjpbIkZFVENILVBFUk1JU1NJT05TLUJZLUFQSSJdLCJhdWQiOiIzZDIzMzk0OS1hMmZiLTRhYjAtYjdlYy00NmY2MjU1YzUxMGUiLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lm9jdG8uYWkiLCJpYXQiOjE3MjE0OTk5Mjd9.EBtUxtL3JvSmWX7IFzPrcTLeNrI_n1xOxNKse5jS43ZdT8UtZddY6zU6M23IxF73qiXd_3c4GZLmCZ2DGKnh94XSzx49FK85EfhogCvPDsQWfkVclVgzQ-LFBvzqbIgF80VBxygZ4-iYQeKGRCGLLTvsG6O2PbIwBAq5jBYKN1SXuPWUqbZpdDt71vgcJGperLWOuW1ZKeCbmEeszQoMvVZVy5fExpGqrDiR4aFlov7_elCHpnHQw3leqPns-HAYMnZMEGRtTNrPP8nl9MbsJRZmzQF3_fTTRM8a-355OvEO-iHXQ3-z2qaY4KwcuHH2rTcqggrGAo0ELGZWnpMwvg",
    )        

    init = from_file("room.jpg")
    images_resp = client.image_gen.generate_sdxl(
        prompt="Modify this room with new furniture. Ensure that the exact dimensions of the room, including details such as floor color, are maintained. Decorate the output image with a couch. Also decorate the output image with a lamp. The output image can also include other new furniture.",
        init_image=init, # Only used for image-to-image
        strength=0.9, # Only used for image-to-image
    )
    images = images_resp.images

    to_file(images[0], "room_out.jpg")
