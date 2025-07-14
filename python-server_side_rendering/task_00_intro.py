# task_00_intro.py
import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, 1):
        try:
            # Create a copy of the template
            invitation = template

            # Replace placeholders with values or "N/A" if missing
            placeholders = ['name', 'event_title', 'event_date', 'event_location']
            for placeholder in placeholders:
                value = attendee.get(placeholder, 'N/A')
                if value is None:
                    value = 'N/A'
                invitation = invitation.replace(f'{{{placeholder}}}', str(value))

            # Generate output filename
            output_file = f'output_{index}.txt'

            # Check if file already exists
            if os.path.exists(output_file):
                print(f"Warning: {output_file} already exists, overwriting.")

            # Write to output file
            with open(output_file, 'w') as file:
                file.write(invitation)

        except Exception as e:
            print(f"Error processing attendee {index}: {str(e)}")
