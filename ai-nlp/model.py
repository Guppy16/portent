from llm import get_llm
from tags import get_tags

event_tags, MAX_CAT = get_tags()

system_prompt = (
    "Your task is to analyze a provided news article and identify a key world event. Follow these instructions carefully:\n\n"
    f"If you identify an event that meets the criteria above, assign one or more categories (up to a maximum of {MAX_CAT}) that best describe the event.\n"
    + f"{event_tags}"
    + "\n\n"
    "Output Format:\n"
    "     {\n"
    '       "categories": ["category1", "category2", ...]\n'
    "     }\n\n"
    "If none of the provided categories are applicable, return `null` for 'categories'.\n\n"
    "     {\n"
    '       "categories": null\n'
    "     }\n"
)


def get_model():
    model = get_llm("deepinfra_meta-llama/Llama-3.3-70B-Instruct-Turbo", system_prompt)
    return model
