def submit_profile(answer_list):
    """
    Tool declaration for OpenAI Assistant API:
    {
      "name": "submit_profile",
      "description": "Tool to call to submit the profile, once all the questions have been answered.",
      "strict": true,
      "parameters": {
        "type": "object",
        "properties": {
          "arguments": {
            "type": "array",
            "description": "The answers to the questions, as list",
            "items": {
              "type": "string"
            }
          }
        },
        "additionalProperties": false,
        "required": [
          "arguments"
        ]
      }
    }
    """
    print("---Submitting profile---")
    print(answer_list)
    return "Profile submitted successfully."


def view_profile(kwargs):
    """
    Tool declaration for OpenAI Assistant API:
    {
      "name": "view_profile",
      "description": "Tool to call when the user asks to view the profile.",
      "strict": true,
      "parameters": {
        "type": "object",
        "additionalProperties": false,
        "properties": {},
        "required": []
      }
    }
    """
    print("---Viewing profile---")
    profile = {
        "name": "Vincent",
        "address": "Nairobi",
        "age": "30",
    }
    return str(profile)


def browse_market(kwargs):
    """
    Tool declaration for OpenAI Assistant API:
    {
      "name": "browse_market",
      "description": "Tool to call when the user wants to see the available offers, listing or products in the marketplace.",
      "strict": true,
      "parameters": {
        "type": "object",
        "properties": {
          "search_criteria": {
            "type": "array",
            "description": "The search criteria to retrieve the marketplace listing, as list of strings",
            "items": {
              "type": "string"
            }
          }
        },
        "additionalProperties": false,
        "required": ["search_criteria"]
      }
    }
    """
    print("---Browsing the marketplace---")
    products = [
        {
            "name": "Product 1",
            "price": "100",
            "description": "This is a product description",
        },
        {
            "name": "Product 2",
            "price": "200",
            "description": "This is a product description",
        },
    ]
    return str(products)
