import seaborn as sns
import matplotlib.pyplot as plt

def ranklist(df, column_name):
    """
        This function provides the barplot for the each series in a column and plot it in bar plot

        Input:
        column_name

        Output:
        plt bar plot of the column variable in descending order
    """
    df = df.sort_values([column_name], ascending=False).reset_index(drop=True)
    sns.set(font_scale=1)
    plt.figure(figsize=(20, 20))
    sns.barplot(x=df[column_name], y=df["name"])
    plt.ylabel("Product Name", fontsize=21)
    plt.xlabel(column_name, fontsize=21)
    plt.title(column_name, fontsize=30)
    plt.show()
