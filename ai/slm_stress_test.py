"""SLM Stress Test for GPU VRAM usage and performance"""

import subprocess
import requests
import time
import json
import sys
import threading
import signal
from datetime import datetime

# --- Configuration ---
OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "qwen2.5:7b"  # Ensure this model is pulled in Ollama first
MAX_TOKENS_PER_TURN = 1000   # How many tokens to generate per turn
NUM_TURNS = 5               # Number of conversation turns

# --- Global Flags for Monitoring Thread ---
stop_monitoring = False
monitor_lock = threading.Lock()

def get_nvml_library():
    """Import pynvml with error handling."""
    try:
        import pynvml
        return pynvml
    except ImportError:
        print("Error: pynvml is not installed. Please run 'pip install pynvml'")
        sys.exit(1)

def get_vram_usage_nvml(pynvml):
    """Get current VRAM usage using pynvml."""
    try:
        pynvml.nvmlInit()
        # Assuming single GPU for this test, or index 0
        handle = pynvvl.nvmlDeviceGetHandleByIndex(0) 
        info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        return info.used / (1024 * 1024) # Convert to MB
    except Exception as e:
        print(f"NVML Error: {e}")
        return None

def monitor_vram_spikes():
    """Background thread to catch VRAM spikes during generation."""
    global stop_monitoring
    pynvml_lib = get_nvml_library()
    
    while not stop_monitoring:
        with monitor_lock:
            current_mem = get_vram_usage_nvml(pynvml_lib)
            if current_mem is not None:
                # In a real scenario, you'd append this to a log file or global list
                pass 
        time.sleep(0.1) # Check every 100ms

def generate_complex_dummy_text(num_tokens):
    """Generate a 'heavy' dummy text that tests attention patterns better than simple repetition."""
    
    # Heuristic: ~4 chars per token for English, less for code/structured data.
    # Let's assume ~3 chars per token to be safe on the high side.
    target_chars = num_tokens * 3 
    
    # A "technical manual" chunk is denser and harder to compress than simple prose.
    base_block = (
        "### Technical Manual Section: System Architecture\n"
        "The system utilizes a distributed microservice architecture designed for high throughput.\n"
        "Key components include:\n"
        "- Service A: Handles authentication via JWT tokens.\n"
        "- Service B: Manages stateful sessions in Redis clusters.\n"
        "- Service C: Processes asynchronous events via Kafka streams.\n\n"
    )
    
    # Repeat the block until we hit the token count
    output = []
    current_len = 0
    counter = 1
    
    while current_len < target_chars:
        line = f"[Ref {counter}] " + base_block.replace("System Architecture", f"Architecture Level {counter}")
        output.append(line)
        current_len += len(output[-1])
        counter += 1
        
        # Safety break to prevent infinite loops if logic fails
        if counter > num_tokens * 2: 
            break
            
    return "".join(output)

def send_conversation(messages, max_new_tokens):
    """Send a message to Ollama API and measure performance metrics."""
    
    url = f"{OLLAMA_URL}/api/chat"
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False 
    }
    
    start_time = time.time()
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            end_time = time.time()
            
            # Parse response to get token count (approximate)
            data = response.json()
            generated_text = data.get('message', {}).get('content', '')
            
            # Estimate tokens generated (rough heuristic: ~4 chars per token for English, less for code)
            # A better way is to use the tokenizer, but this is a stress test script.
            estimated_tokens_generated = len(generated_text) // 3 
            
            duration = end_time - start_time
            
            if duration > 0 and estimated_tokens_generated > 0:
                tps = estimated_tokens_generated / duration
                print(f"   [Metrics] Generated ~{estimated_tokens_generated} tokens in {duration:.2f}s -> {tps:.2f} TPS")
            
            return True, estimated_tokens_generated
            
        else:
            print(f"   Error: {response.status_code} - {response.text}")
            return False, 0
            
    except Exception as e:
        print(f"Exception: {e}")
        return False, 0

def main():
    print("Starting VRAM & Performance Stress Test...")
    
    # Initialize NVML once if we were doing live monitoring, 
    # but here we check before and after to avoid overhead during test.
    
    initial_vram = get_vram_usage_nvml(get_nvml_library())
    print(f"Initial VRAM Usage: {initial_vram:.1f} MB")
    
    messages = []
    
    for i in range(NUM_TURNS):
        print(f"\n--- Turn {i+1}/{NUM_TURNS}: Adding Context ---")
        
        # 1. Generate Complex Text (The "Heavy" Data)
        # We generate slightly less than MAX_TOKENS_PER_TURN to leave room for the prompt itself
        # but we simulate a large context window fill.
        dummy_text = generate_complex_dummy_text(MAX_TOKENS_PER_TURN)
        
        # Add to conversation history
        messages.append({"role": "user", "content": f"Here is some technical data: {dummy_text}"})
        messages.append({"role": "assistant", "content": "I have processed this information."})
        
        print(f"   Context size increased. Sending request...")
        
        # 2. Send Request & Measure Performance
        success, tokens_generated = send_conversation(messages, MAX_TOKENS_PER_TURN)
        
        if not success:
            print("Failed to send message. Context might be too large or OOM.")
            break
        
        # 3. Check VRAM immediately after generation settles
        time.sleep(1) 
        current_vram = get_vram_usage_nvml(get_nvml_library())
        
        if initial_vram is not None and current_vram is not None:
            delta = current_vram - initial_vram
            print(f"   VRAM Usage: {current_vram:.1f} MB (Delta: +{delta:.1f} MB)")
            
            # Optional: Log to a file or list for later plotting
            # log_data.append({'turn': i+1, 'vram': current_vram})

        # Safety check: If VRAM is near max, stop
        if current_vram > 23000: # Example threshold for 24GB card
             print("VRAM Critical Limit Approaching. Stopping test.")
             break

    print("\nTest completed.")

if __name__ == "__main__":
    main()