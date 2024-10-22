import json
import random
import string

from utils import generate_seed_phrase

# Set to keep track of generated IDs to ensure uniqueness
generated_ids = set()


def generate_unique_id():
    """Generate a unique ID consisting of uppercase letters and digits."""
    while True:
        # Create a new ID with a length of 10 characters
        new_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        # Check if the ID is unique
        if new_id not in generated_ids:
            generated_ids.add(new_id)  # Add the unique ID to the set
            return new_id


def generate_questionnaires(num_managers, team_members_per_manager):
    """Generate a list of questionnaires for managers and their team members.

    Args:
        num_managers (int): The number of managers to generate.
        team_members_per_manager (int): The number of team members per manager.

    Returns:
        list: A list of dictionaries representing the generated questionnaires.
    """
    # Generate unique manager IDs
    managers = [generate_unique_id() for _ in range(num_managers)]

    questionnaires = [
        {
            "id": manager_id,
            "manager_id": manager_id,
            "seed_phrase": generate_seed_phrase(),
        }
        for manager_id in managers
    ]

    # Generate team member questionnaires for each manager
    for manager_id in managers:
        questionnaires.extend(
            {
                "id": generate_unique_id(),
                "manager_id": manager_id,
                "seed_phrase": generate_seed_phrase(),
            }
            for _ in range(team_members_per_manager)
        )

    return questionnaires


def main():
    """Main function to generate questionnaires and save them to a JSON file."""
    questionnaires = generate_questionnaires(num_managers=2, team_members_per_manager=2)

    # Write the generated questionnaires to a JSON file
    with open("questionnaires.json", "w", encoding="utf-8") as f:
        json.dump(questionnaires, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()  # Execute the main function when the script is run
