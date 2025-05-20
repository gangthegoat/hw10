import os
import pickle

def input_scores():
    scores = []
    print("[점수 입력]")
    i = 1
    while True:
        s = int(input(f"#{i}? "))
        if s < 0:
            break
        scores.append(s)
        i += 1
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print("[점수 출력]")
    print("개인점수:", end=' ')
    for s in scores:
        print(s, end=' ')
    print()
    print("평균:", get_average(scores))

def save_scores(scores, filename="score.bin"):
    with open(filename, "wb") as file:
        pickle.dump(scores, file)

def load_scores(filename="score.bin"):
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)
    else:
        return None

def main():
    filename = "score.bin"
    scores = load_scores(filename)
    
    if scores is None:
        scores = input_scores()
        save_scores(scores, filename)
    
    show_scores(scores)

if __name__ == "__main__":
    main()