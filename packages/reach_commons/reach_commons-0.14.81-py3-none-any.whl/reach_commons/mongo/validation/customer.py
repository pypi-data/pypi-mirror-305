import jsonschema
from jsonschema import validate

customer_schema = {
    "type": "object",
    "properties": {
        "customer_id": {"type": "string"},
        "business_id": {"type": "integer"},
        "email": {"type": ["string", "null"], "format": "email"},
        "phone_number": {"type": ["string", "null"]},
        "name": {"type": "string"},
        "age": {"type": ["integer", "null"]},
        "gender": {"type": ["string", "null"]},
        "created_at": {
            "type": ["string", "null"],
            "format": "date-time",
            "pattern": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$",
        },
        "updated_at": {
            "type": ["string", "null"],
            "format": "date-time",
            "pattern": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$",
        },
        "cohorts": {
            "type": "object",
            "properties": {
                "preferred_day": {"type": "array", "items": {"type": "string"}},
                "ticket_average_min": {"type": ["integer", "null"]},
                "ticket_average_max": {"type": ["integer", "null"]},
                "prices_min": {"type": ["integer", "null"]},
                "prices_max": {"type": ["integer", "null"]},
                "future_appointment": {"type": "array", "items": {"type": "boolean"}},
                "allow_book_online": {"type": "array", "items": {"type": "boolean"}},
                "accept_online": {
                    "type": ["array", "null"],
                    "items": {"type": "boolean"},
                },
                "single_visits": {
                    "type": ["array", "null"],
                    "items": {"type": "boolean"},
                },
                "winback": {"type": ["array", "null"], "items": {"type": "boolean"}},
                "new_customers": {
                    "type": ["array", "null"],
                    "items": {"type": "boolean"},
                },
                "inactive_customers": {
                    "type": ["array", "null"],
                    "items": {"type": "boolean"},
                },
                "preferred_season": {
                    "type": ["array", "null"],
                    "items": {"type": "string"},
                },
                "services": {"type": ["array", "null"], "items": {"type": "string"}},
                "preferred_month": {
                    "type": ["array", "null"],
                    "items": {"type": "string"},
                },
                "preferred_period": {
                    "type": ["array", "null"],
                    "items": {"type": "string"},
                },
                "visit_count": {"type": ["array", "null"], "items": {"type": "string"}},
                "resources": {"type": ["array", "null"], "items": {"type": "string"}},
                "categories": {"type": ["array", "null"], "items": {"type": "string"}},
            },
            "additionalProperties": False,
        },
    },
    "required": ["customer_id", "business_id", "email"],
    "additionalProperties": True,
}


def validate_customer(data: dict):
    try:
        validate(instance=data, schema=customer_schema)
        return data
    except jsonschema.exceptions.ValidationError as e:
        field_path = " -> ".join([str(elem) for elem in e.path])
        return f"Validation error in field: {field_path}. Error: {e.message}"


"""
Example:
{
  "customer_id": "C129C0DA-FF8C-428E-88CB-AE82018B1558",
  "business_id": 2,
  "name": "Abby Cebular",
  "email": "aar5042@gmail.com",
  "phone_number":"+55111111111",
  "age": 10,
  "gender": "male",
  "updated_at": "2024-10-26T00:00:00",
  "created_at": "2024-10-26T00:00:00",
  "cohorts": {
    "preferred_day": [
      "saturday"
    ],
    "ticket_average_min": 50,
    "ticket_average_max": 50,
    "prices_min": 0,
    "prices_max": 9999,
    "future_appointment": [
      false
    ],
    "allow_book_online": [
      false
    ],
    "accept_online": [
      true
    ],
    "single_visits": [
      false
    ],
    "winback": [
      false
    ],
    "new_customers": [
      false
    ],
    "inactive_customers": [
      false
    ],
    "preferred_season": [
      "summer"
    ],
    "services": [
      "spray tan"
    ],
    "preferred_month": [
      "June"
    ],
    "preferred_period": [
      "afternoon"
    ],
    "visit_count": "1",
    "resources": [
      "jess",
      "ainsley"
    ],
    "categories": [
      "subcategory 1"
    ]
  }
}
"""
