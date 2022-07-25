import seaborn as sns
import matplotlib.pyplot as plt


def graph(df, column_name):
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

def top(df,column_name)->str:
    """
    :param df: the dataframe that got passed into the function
    :param column_name: the variable that we are interested in ranking in descending order
    :return: a string of the top five products in the rank list of the column category
    """
    df = df.sort_values([column_name], ascending=False).reset_index(drop=True)
    string1 = 'Top: '.append(", ".join(str(i) for i in list(df['name'].head())))
    return string1


def bottom(df,column_name)->str:
    """
    :param df: the dataframe that got passed into the function
    :param column_name: the variable that we are interested in ranking in descending order
    :return: a string of the bottom five products in the rank list of the column category
    """
    df = df.sort_values([column_name], ascending=False).reset_index(drop=True)
    string2 = ", ".join(str(i) for i in list(df['name'].tail()))
    return string2


print(graph.__doc__)
print(top.__doc__)
print(bottom.__doc__)