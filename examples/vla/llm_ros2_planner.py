import openai
import os
import json

# Set your OpenAI API key
# Ensure you have your API key set as an environment variable or replace 'YOUR_OPENAI_API_KEY'
# For example: export OPENAI_API_KEY='your_api_key_here'
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ros2_plan(natural_language_command, current_robot_state, available_objects):
    """
    Generates a ROS 2 action plan from a natural language command using an LLM.
    """
    if not openai.api_key:
        print("OPENAI_API_KEY environment variable not set. Please set it to use the OpenAI API.")
        return None

    system_message = """You are a robotic planning assistant. Your goal is to translate natural language commands into a sequence of ROS 2 compatible actions.
Available actions:
- move_to(location): Move the robot to a specified location.
- grasp(object_name): Grasp an object.
- release(object_name): Release a grasped object.
- look_at(direction/object_name): Direct the robot's gaze.

Output the plan as a JSON array of action objects, each with 'action' and 'parameters'.
Example:
[
  {"action": "move_to", "parameters": {"location": "table"}},
  {"action": "grasp", "parameters": {"object_name": "red_block"}}
]
"""

    user_message = f""
Current Robot State: {current_robot_state}
Available Objects in Environment: {', '.join(available_objects)}
Command: "{natural_language_command}"

Generate a ROS 2 action plan in JSON format:
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-4o", # Using a more recent model for better performance
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0, # For more deterministic output
            response_format={ "type": "json_object" } # Request JSON output
        )
        plan_json_string = response.choices[0].message.content
        return json.loads(plan_json_string)
    except Exception as e:
        print(f"Error generating plan: {e}")
        return None

if __name__ == "__main__":
    print("This script demonstrates LLM-driven ROS 2 action plan generation.")
    print("Please ensure your OPENAI_API_KEY environment variable is set.")
    print("Example: set OPENAI_API_KEY=your_key_here (Windows) or export OPENAI_API_KEY=your_key_here (Linux/macOS)\n")

    command = input("Enter a natural language command for the robot (e.g., 'pick up the red block and place it on the table'): ")
    
    current_robot_state = "Robot is at workstation, not gripping any object."
    available_objects = ["red_block", "blue_sphere", "green_cube", "table", "shelf"]

    print(f"\nGenerating plan for command: '{command}'")
    action_plan = generate_ros2_plan(command, current_robot_state, available_objects)

    if action_plan:
        print("\nGenerated ROS 2 Action Plan:")
        for i, action in enumerate(action_plan):
            print(f"Step {i+1}: Action: {action.get('action', 'N/A')}, Parameters: {action.get('parameters', 'N/A')}")
        print("\n--- Plan Execution Simulation ---")
        print("In a real system, this plan would now be translated into ROS 2 messages and executed by the robot.")
    else:
        print("Failed to generate an action plan. Check API key and network connection.")
