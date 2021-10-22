with open('binary.bin', 'wb') as f:
    f.write(b'\xff\x00\x7f')  # 11101010_10110000_10000000

input()
with open('binary.bin', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)