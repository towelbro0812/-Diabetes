# 糖尿病 BRFSS 2021 資料集疾病預測
[streamlit app 連結](https://towelbrodiabetes.streamlit.app/)
[kaggle 資料集連結](https://www.kaggle.com/datasets/julnazz/diabetes-health-indicators-dataset/data)

糖尿病是一種慢性健康狀況，會影響您的身體將食物轉化為能量的方式。糖尿病主要分為三種：1 型、2 型和妊娠期糖尿病。
Type 1 diabetes is an autoimmune disease that causes your body to attack the cells in your pancreas that produce insulin. Insulin is a hormone that helps your body use glucose for energy.
1 型糖尿病是一種自體免疫疾病，會導致您的身體攻擊胰臟中產生胰島素的細胞。胰島素是一種幫助您的身體利用葡萄糖獲取能量的荷爾蒙。

Type 2 diabetes is the most common type of diabetes. It occurs when your body doesn't respond normally to insulin, or when your body doesn't produce enough insulin.
2 型糖尿病是最常見的糖尿病類型。當您的身體對胰島素沒有正常反應，或者您的身體無法產生足夠的胰島素時，就會發生這種情況。

Gestational diabetes is a type of diabetes that develops during pregnancy. It usually goes away after the baby is born.
妊娠糖尿病是一種在懷孕期間發生的糖尿病。通常在嬰兒出生後就會消失。

### 此資料集有21個特徵，為了預測 Diabetes_012 的class

| 序號 | 名稱                    | 說明                                                                                           |
|------|-------------------------|------------------------------------------------------------------------------------------------|
| 0    | Diabetes_binary            | 0 = 無糖尿病, 1 = 糖尿病                                                       |
| 1    | HighBP                  | 0 = 無高血壓, 1 = 高血壓                                                                      |
| 2    | HighChol                | 0 = 無高膽固醇, 1 = 高膽固醇                                                                   |
| 3    | CholCheck               | 0 = 過去5年未檢查膽固醇, 1 = 過去5年內有檢查膽固醇                                            |
| 4    | BMI                     | BMI指數                                                                                        |
| 5    | Smoker                  | 是否有抽菸過至少100支香煙？[註: 5包 = 100支香煙] 0 = 否, 1 = 是                                  |
| 6    | Stroke                  | (曾告知) 是否中風？ 0 = 否, 1 = 是                                                            |
| 7    | HeartDiseaseorAttack    | 冠心病或心肌梗塞 0 = 否, 1 = 是                                                                |
| 8    | PhysActivity            | 過去30天內的體育活動 - 不包括工作 0 = 否, 1 = 是                                                |
| 9    | Fruits                  | 每天是否食用1份或更多的水果？ 0 = 否, 1 = 是                                                    |
| 10   | Veggies                 | 每天是否食用1份或更多的蔬菜？ 0 = 否, 1 = 是                                                    |
| 11   | HvyAlcoholConsump       | 0 = 否, 1 = 是 (男性每週飲酒超過14杯，女性每週飲酒超過7杯)                                     |
| 12   | AnyHealthcare           | 0 = 否, 1 = 是 (是否有醫療保險)                                                                |
| 13   | NoDocbcCost             | 0 = 否, 1 = 是 (過去12個月因為費用昂貴而無法就醫)                                               |
| 14   | GenHlth                 | 1 = 極佳, 2 = 很好, 3 = 好, 4 = 尚可, 5 = 差 (自我健康狀況評分1-5)                                |
| 15   | MentHlth                | 0-30 (過去30天內有多少天心理健康不佳？以天數計算，範圍0-30)                                       |
| 16   | PhysHlth                | 0-30 (過去30天內有多少天身體健康不佳？以天數計算，範圍0-30)                                       |
| 17   | DiffWalk                | 爬樓梯是否有困難？ 0 = 否, 1 = 是                                                               |
| 18   | Sex                     | 0 = 女性, 1 = 男性                                                                             |
| 19   | Age                     | 年齡13級量表 18-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80-99 |
| 20   | Education               | 教育程度6級量表 1 = 沒上學, 2 = 1~8年級, 3 = 9~11年級(國中高中), 4 = 12年級(高中畢業), 5 = 大學1~3年級, 6 = 大學畢業或4年以上   |
| 21   | Income                  | 收入11級量表                                                                                   |

</br>

| 序號 | 收入區間                                |
|------|---------------------------------------|
| 1    | Less than $10,000                     |
| 2    | Less than $15,000 ($10,000 to < $15,000)|
| 3    | Less than $20,000 ($15,000 to < $20,000)|
| 4    | Less than $25,000 ($20,000 to < $25,000)|
| 5    | Less than $35,000 ($25,000 to < $35,000)|
| 6    | Less than $50,000 ($35,000 to < $50,000)|
| 7    | Less than $75,000 ($50,000 to < $75,000)|
| 8    | Less than $100,000? ($75,000 to < $100,000)|
| 9    | Less than $150,000? ($100,000 to < $150,000)?|
| 10   | Less than $200,000? ($150,000 to < $200,000)|
| 11   | $200,000 or more                      |
