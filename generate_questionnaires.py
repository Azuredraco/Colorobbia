import json
import random
import string

from utils import generate_seed_phrase

# Set to keep track of generated IDs
generated_ids = set()


def generate_unique_id():
    while True:
        new_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        if new_id not in generated_ids:
            generated_ids.add(new_id)
            return new_id


def generate_questionnaires(num_managers, team_members_per_manager):
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
    # Generate team member questionnaires
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
    questionnaires = generate_questionnaires(num_managers=2, team_members_per_manager=2)

    with open("questionnaires.json", "w", encoding="utf-8") as f:
        json.dump(questionnaires, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
