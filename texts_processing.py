import random

def get_daily_motivation_text():
    with open("texts/before_task.txt", "r", encoding="utf-8") as f:
        texts = f.read().split("\n")
        return random.choice(texts)

def get_score_text(score):
    with open("texts/after_task.txt", "r", encoding="utf-8") as f:
        texts = f.read().split("\n")
        text = random.choice(texts)
        return text.replace("{score}", f"{score}")
