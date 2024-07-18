class MedBotModel:
    def __init__(self):
        pass

    def diagnose(self, keywords):
        # 模拟的诊断结果
        return f"Diagnosis based on keywords: {keywords}"

medbot = MedBotModel()

def get_diagnosis(keywords):
    return medbot.diagnose(keywords)
