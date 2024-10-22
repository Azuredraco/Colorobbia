import json
import random
import string

from utils import generate_seed_phrase


def generate_unique_id():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=8))


def generate_questionnaires(num_managers, team_members_per_manager):
    return [
        {
            "id": manager_id,
            "type": "mando",
            "manager_id": manager_id,
            "seed_phrase": generate_seed_phrase(),
        }
        for _ in range(num_managers)
        for manager_id in [generate_unique_id()]
    ] + [
        {
            "id": generate_unique_id(),
            "type": "equipo",
            "manager_id": manager_id,
            "seed_phrase": generate_seed_phrase(),
        }
        for manager_id in [generate_unique_id() for _ in range(num_managers)]
        for _ in range(team_members_per_manager)
    ]


def main():
    questionnaires = generate_questionnaires(num_managers=2, team_members_per_manager=2)

    with open("questionnaires.json", "w", encoding="utf-8") as f:
        json.dump(questionnaires, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
