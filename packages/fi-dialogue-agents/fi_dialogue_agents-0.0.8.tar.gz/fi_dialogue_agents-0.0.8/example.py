from fi_dialogue_agents import Agent
import time

# Define how the agent should handle incoming messages
def received_message(message):
    print(f"Processing message: {message}")
    
    # Simulate thinking time before typing starts
    time.sleep(2)  
    
    # Start typing simulation
    agent.start_typing()

    # Simulate typing time
    time.sleep(0.5)
    
    # Send the response message
    agent.send_message(f"Hello there!")

    # Stop typing simulation
    agent.stop_typing()

    time.sleep(0.5)

    # Start typing simulation
    agent.start_typing()

    # Simulate typing time
    time.sleep(1)

    # Send the response message
    agent.send_message(f"General Ken!")

    # Stop typing simulation
    agent.stop_typing()



# Create an agent instance
agent = Agent(host="127.0.0.1", port=5002)

# Register the user-defined message handler
agent.on_message(received_message)

# Run the SocketIO server
agent.run()
# agent.run(ngrok_token="<ngrok_token>")  # Run with Ngrok tunnel for public access
