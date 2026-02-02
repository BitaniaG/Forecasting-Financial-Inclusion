import matplotlib.pyplot as plt

def plot_pre_post_changes(df, title):
    df = df.sort_values("absolute_change")
    plt.figure(figsize=(10, 6))
    plt.barh(df["indicator_code"], df["absolute_change"])
    plt.axvline(0, linestyle="--")
    plt.title(title)
    plt.xlabel("Absolute Change")
