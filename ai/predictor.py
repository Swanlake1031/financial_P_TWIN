# ai/predictor.py

def predict_months_to_goal(income, rent, food, entertainment, goal_amount):
    total_spending = rent + food + entertainment
    savings = income - total_spending
    if savings <= 0:
        return float('inf')  # 无法实现目标
    return round(goal_amount / savings, 1)

# 示例调用（测试用）
if __name__ == "__main__":
    months = predict_months_to_goal(
        income=3500,
        rent=1200,
        food=500,
        entertainment=300,
        goal_amount=10000
    )
    print(f"你预计需要 {months} 个月达成你的目标 🎯")