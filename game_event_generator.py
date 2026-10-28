
import json
import random
import uuid
from datetime import datetime, timezone

# Game event types and their parameters
EVENT_TYPES = {
    "player_login": {
        "login_method": ["google", "guest", "facebook"]
    },
    "session_start": {
        "session_source": ["organic", "ad", "referral"]
    },
    "level_started": {
        "level_number": [1, 2, 3, 4, 5],
        "difficulty": ["easy", "medium", "hard"]
    },
    "level_completed": {
        "level_number": [1, 2, 3, 4, 5],
        "score": [100, 250, 500, 1000],
        "completion_time_seconds": [45.5, 62.3, 92.5, 120.0]
    },
    "level_failed": {
        "level_number": [1, 2, 3, 4, 5],
        "failure_reason": ["time_out", "no_lives", "obstacle"]
    },
    "reward_claimed": {
        "reward_type": ["coins", "gems", "extra_life"],
        "reward_amount": [10, 25, 50, 100]
    },
    "item_purchased": {
        "item_id": ["skin_01", "boost_01", "extra_life"],
        "price": [10, 50, 100],
        "currency": ["coins", "gems"]
    },
    "ad_watched": {
        "ad_type": ["rewarded", "interstitial"],
        "ad_rewarded": [True, False]
    },
    "session_end": {
        "session_duration_seconds": [60, 180, 300, 600]
    }
}


def create_parameter(key, value):
    """Represent each parameter using a typed value field."""
    parameter = {
        "key": key,
        "string_value": None,
        "int_value": None,
        "double_value": None,
        "bool_value": None
    }

    if isinstance(value, bool):
        parameter["bool_value"] = value
    elif isinstance(value, int):
        parameter["int_value"] = value
    elif isinstance(value, float):
        parameter["double_value"] = value
    else:
        parameter["string_value"] = str(value)

    return parameter


def generate_event(player_id, session_id):
    """Generate one event with nested event parameters."""
    event_name = random.choice(list(EVENT_TYPES.keys()))
    parameters = EVENT_TYPES[event_name]

    event_params = [
        create_parameter(key, random.choice(values))
        for key, values in parameters.items()
    ]

    return {
        "event_id": str(uuid.uuid4()),
        "event_name": event_name,
        "event_timestamp": datetime.now(timezone.utc).isoformat(),
        "player_id": player_id,
        "session_id": session_id,
        "country": random.choice(["India", "USA", "UK", "UAE"]),
        "device": random.choice(["Android", "iOS", "Web"]),
        "event_params": event_params
    }


if __name__ == "__main__":
    players = [f"player_{i:03d}" for i in range(1, 6)]

    events = []
    for _ in range(10):
        player = random.choice(players)
        session = f"session_{random.randint(1000, 1010)}"
        events.append(generate_event(player, session))

    # Save generated events as newline-delimited JSON
    with open("game_events.jsonl", "w", encoding="utf-8") as file:
        for event in events:
            file.write(json.dumps(event) + "\n")

    print(f"Generated {len(events)} game events.")
    print("Saved to game_events.jsonl")
    print("\nFirst event:")
    print(json.dumps(events[0], indent=2))
