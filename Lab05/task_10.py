# Задание 10. Комплексное задание: датасет tips
import pandas as pd
import seaborn as sns

# 1. Загрузка датасета
tips = sns.load_dataset('tips')

# 2. Диагностика
print("--- info() ---")
tips.info()
print("\n--- describe() ---\n", tips.describe())
print("\nShape:", tips.shape, "\n")

# 3. Средний чек по дням недели
print("Средний чек по дням:\n", tips.groupby('day', observed=False)['total_bill'].mean(), "\n")

# 4. Средние чаевые в процентах от чека по дням недели
tips['tip_pct_temp'] = (tips['tip'] / tips['total_bill']) * 100
print("Средний % чаевых по дням:\n", tips.groupby('day', observed=False)['tip_pct_temp'].mean(), "\n")

# 5. Сводная таблица: средний total_bill по day x time
pt_tips = tips.pivot_table(values='total_bill', index='day', columns='time', aggfunc='mean', observed=False)
print("Сводная таблица (day x time):\n", pt_tips, "\n")

# 6. Количество заказов, средний чек, максимальные чаевые по дням
day_report = tips.groupby('day', observed=False).agg(
    orders_count=('total_bill', 'count'),
    avg_bill=('total_bill', 'mean'),
    max_tip=('tip', 'max')
)
print("Агрегированный отчет по дням:\n", day_report, "\n")

# 7. Заказы с tip > 5 и их доля
tips_gt_5 = tips[tips['tip'] > 5]
share_gt_5 = (len(tips_gt_5) / len(tips)) * 100
print(f"Количество заказов с чаевыми > $5: {len(tips_gt_5)} ({share_gt_5:.2f}%)\n")

# 8. Топ-10 самых больших заказов по total_bill, с сортировкой по size
top10_bills = tips.sort_values(by=['size', 'total_bill'], ascending=[True, False]).head(10)
print("Топ-10 заказов по size и total_bill:\n", top10_bills[['total_bill', 'tip', 'size', 'day']], "\n")

# 9. Признак tip_pct и сравнение по smoker
tips['tip_pct'] = (tips['tip'] / tips['total_bill']) * 100
print("Средний % чаевых по курящим/некурящим:\n", tips.groupby('smoker', observed=False)['tip_pct'].mean(), "\n")

# 10. Сохранение агрегированного отчета (3 столбца) в CSV
# Сформируем отчет: день, средний чек, средний процент чаевых
final_report = tips.groupby('day', observed=False).agg(
    avg_total_bill=('total_bill', 'mean'),
    avg_tip_pct=('tip_pct', 'mean'),
    total_orders=('total_bill', 'count')
).reset_index()

final_report.to_csv('tips_summary.csv', index=False)
print("Итоговый отчет сохранен в 'tips_summary.csv':\n", final_report)

