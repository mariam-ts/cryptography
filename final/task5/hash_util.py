import hashlib, json

def compute_hashes(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return {
        'SHA-256': hashlib.sha256(data).hexdigest(),
        'SHA-1': hashlib.sha1(data).hexdigest(),
        'MD5': hashlib.md5(data).hexdigest()
    }

original = compute_hashes("original.txt")
with open("hashes.json", "w") as f:
    json.dump(original, f, indent=2)

# Simulate tampering
with open("tampered.txt", "w") as f:
    f.write("Tampered content!")

tampered = compute_hashes("tampered.txt")
match = original == tampered

print("Integrity check:", "PASS" if match else "FAIL")
