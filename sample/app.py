import time

# 問題データベース
problems = [
    {
        "question": "配列 [2, 7, 11, 15] の中から、合計が9になる2つの数値のインデックスを返してください。",
        "example": "入力: nums = [2, 7, 11, 15], target = 9\n出力: [0, 1]",
        "solution": lambda nums, target: two_sum(nums, target),
        "answer": [0, 1]
    },
    {
        "question": "文字列 'hello' を逆順にしてください。",
        "example": "入力: 'hello'\n出力: 'olleh'",
        "solution": lambda s: reverse_string(s),
        "answer": 'olleh'
    }
]

# 解答関数
def two_sum(nums, target):
    # 配列内で合計がtargetになる2つのインデックスを探す
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

def reverse_string(s):
    # 文字列を逆順にする
    return s[::-1]

# 模擬試験モード
def mock_exam():
    print("模擬試験モード開始！")
    score = 0

    for i, problem in enumerate(problems):
        print(f"\n問題 {i+1}: {problem['question']}")
        print(f"例: {problem['example']}")
        
        start_time = time.time()
        user_input = input("あなたの解答（Pythonコードで入力してください）: ")
        
        try:
            # ユーザーコード実行
            user_solution = eval(user_input)
            correct_answer = problem["solution"](*eval(user_input))
            
            if user_solution == correct_answer:
                print("正解です！")
                score += 1
            else:
                print(f"不正解です。正しい答えは {problem['answer']} です。")
        
        except Exception as e:
            print(f"エラーが発生しました: {e}")

        elapsed_time = time.time() - start_time
        print(f"解答時間: {elapsed_time:.2f}秒")

    print(f"\n模擬試験終了！あなたのスコアは {score}/{len(problems)} です。")

# 実行
if __name__ == "__main__":
    mock_exam()