import pandas as pd
import matplotlib.pylab as plt

# 專案名稱：外匯趨勢分析工具

# 設定 Matplotlib 字體以支援中文顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False 

# 定義數據檔案路徑
FILE_PATH = "./half a year USD.csv"

try:
    # --- 數據讀取與處理階段 ---
    # 第一步：使用 Pandas 高效讀取 CSV 檔案
    # 將第一欄（索引 0）設為 DataFrame 的索引，並解析為日期格式
    # 只讀取日期（欄位 0）與匯率（欄位 3）
    df = pd.read_csv(
        FILE_PATH,
        index_col=0,
        parse_dates=True,
        usecols=[0, 3]
    )

    # 由於數據排序是從舊到新，將其反轉以符合 Matplotlib 繪圖的習慣（由右至左）
    # 如果數據源本身就是從新到舊排序，則這行是必須的。
    df = df.iloc[::-1]

    # --- 數據可視化階段 ---
    # 第二步：使用 Pandas 內建的繪圖功能創建圖表
    # 以藍色虛線樣式繪製，並設定圖表大小
    df.plot(style='b--', figsize=(10, 6))

    # 第三步：設定圖表標題與座標軸標籤
    # 讓使用者可以快速理解圖表內容
    plt.xlabel("日期")
    plt.ylabel("匯率")
    plt.title("USD換匯率趨勢圖")

    # 顯示圖例
    plt.legend(["USD"])
    
    # 自動調整 X 軸日期標籤，避免標籤重疊，提升圖表可讀性
    plt.gcf().autofmt_xdate()

    # 顯示最終圖表
    plt.show()

# --- 錯誤處理階段 ---
# 使用 try-except 區塊處理潛在的程式錯誤
except FileNotFoundError:
    # 當找不到指定檔案時，給出明確的錯誤提示
    print(f"錯誤：找不到檔案，請確認檔案路徑是否正確：{FILE_PATH}")
except Exception as e:
    # 處理其他未預期的錯誤，提供通用錯誤訊息
    print(f"發生了其他錯誤：{e}")