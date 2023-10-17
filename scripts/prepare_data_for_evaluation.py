"""This script prepares the data for manual evaluation by converting the json file to a csv file.
It selects 15 items for each (prompt variation, answer) combination for manual evaluation."""
import json
import random

import pandas as pd

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

if __name__ == "__main__":
    data_file = "../data/processed/evaluations_per_prompt_gpt-3.5-turbo-0613_eval_gpt-3.5-turbo-0613.json"

    with open(data_file, "r") as f:
        data = json.load(f)

    prompt_variations = data.keys()
    print(prompt_variations)

    select_for_each_prompt_answer = 15

    evaluation_dict = {}
    index_i = 0
    for prompt_variation in prompt_variations:
        for disease_name in data[prompt_variation]:
            for selected_prompt in data[prompt_variation][disease_name]:
                evaluation = selected_prompt["evaluation"]
                evaluation["answer"] = evaluation["answer"].lower()
                del selected_prompt["evaluation"]

                evaluation_dict[index_i] = {
                    "prompt_variation": prompt_variation,
                    "disease_name": disease_name,
                }
                evaluation_dict[index_i].update(selected_prompt)
                evaluation_dict[index_i].update(evaluation)
                index_i += 1

    df = pd.DataFrame.from_dict(evaluation_dict, orient="index")

    print(df.groupby(["prompt_variation", "answer"]).count()["disease_name"].to_dict())

    # sample select_for_each_prompt_answer items for each (prompt variation, answer) combination
    df = df.groupby(["prompt_variation", "answer"]).sample(
        n=select_for_each_prompt_answer, random_state=RANDOM_SEED, replace=False
    )

    df.to_csv(
        "../data/processed/evaluations_per_prompt_gpt-4-0613_eval_gpt-3.5-turbo-0613.csv",
        index=False,
    )
