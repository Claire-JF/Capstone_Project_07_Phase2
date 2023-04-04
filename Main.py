import joblib
import datetime as DT
from GetModel import GetModel
import matplotlib.pyplot as plt


# Train and save the model and return the MAE
r = GetModel()
print("MAE:", r[0])
# Read the saved model
model = joblib.load('Model.pkl')

# predict result
preds = model.predict(r[1])
# 打印结果到控制台
print("未来7天预测")
all_ave_t = []
all_high_t = []
all_low_t = []
all_rainfall = []
for a in range(0, 6):
    today = DT.datetime.now()
    time = (today + DT.timedelta(days=a)).date()
    print(time.year, '/', time.month, '/', time.day,
          ':最高气温', preds[a][0],
          '最低气温', preds[a][1],)
    all_high_t.append(preds[a][0])
    all_low_t.append(preds[a][1])

temp = {"high_t": all_high_t, "low_t": all_low_t}
# 绘画折线图
plt.plot(range(0, 6), temp["high_t"], color="red", label="high_t")
plt.plot(range(0, 6), temp["low_t"], color="blue", label="low_t")
plt.legend()  # 显示图例
plt.ylabel("Temperature(°C)")
plt.xlabel("day")
plt.show()
