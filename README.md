# Image Processing (MC920) - Steganography

- [Requirements](papers/enunciado.pdf)
- [Report](papers/entrega.pdf)

This project implements basic LSB steganography to hide and retrieve arbitrary data within color PNGs. A pair of Python scripts encodes a file into the chosen bit plane of each channel and decodes it back, demonstrating how hidden payloads affect human perception.

Features:
- Hide text or binary files using any of the eight bit planes
- Optional pseudo-random permutation of bit positions for scrambling
- Separate encode and decode commands with simple CLI interface
- Visualize individual bit planes before and after embedding

![Peppers with a hidden message](resultados/bits/pep6.png "Not-so-hidden message on bit plane 6 exposed!")
