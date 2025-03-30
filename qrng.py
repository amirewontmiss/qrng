from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.primitives import StatevectorSampler  # Using the V2 API as recommended

def quantum_rng(num_bits=8):
    """Generates a quantum random number with the given number of bits."""
    # Create a simulator
    simulator = AerSimulator()
    # Create a sampler using the new API
    sampler = StatevectorSampler()
    
    random_bits = ""
    for _ in range(num_bits):
        # Create a new circuit for each bit
        qrng_circuit = QuantumCircuit(1, 1)  # 1 qubit, 1 classical bit
        qrng_circuit.h(0)  # Put qubit in superposition
        qrng_circuit.measure(0, 0)  # Measure and collapse the state
        
        # Run the circuit directly with the simulator
        result = simulator.run(qrng_circuit, shots=1).result()
        counts = result.get_counts()
        bit = list(counts.keys())[0]  # Get the measured bit
        random_bits += bit
    
    random_number = int(random_bits, 2)  # Convert bits to integer
    return random_number, random_bits

# Generate an 8-bit quantum random number
random_number, bits = quantum_rng(8)
print(f"Quantum Random Number: {random_number} (Binary: {bits})")
