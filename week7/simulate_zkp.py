import random

def simulate_zkp(trials=20, knows_password=False):
    success_count = 0
    for i in range(trials):
        path_entered = random.choice(['A', 'B'])
        challenge = random.choice(['A', 'B'])

        if knows_password:
            success = True  # The prover always succeeds if they know the password
        else:
            success = path_entered == challenge  # Malicious prover only succeeds if guess matches challenge

        if success:
            success_count += 1

        print(f"Trial {i+1}: Entered {path_entered}, Challenge {challenge}, {'Success' if success else 'Fail'}")

    success_probability = success_count / trials
    print(f"\n[+] Successful responses: {success_count}/{trials}")
    print(f"[+] Success probability: {success_probability:.2f}")

# Run simulation for malicious prover
simulate_zkp(knows_password=False)
