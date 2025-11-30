# 23f3001440@ds.study.iitm.ac.in
# MARIMO INTERACTIVE NOTEBOOK (analysis.py)

import marimo

app = marimo.App()


# ---------------------------------------------------------
# Cell 1 — Data loading
# ---------------------------------------------------------
@app.cell
def cell1():
    """
    Data flow:
    - Loads the Iris dataset into `df`
    - Next cells depend on df (reactive dependency)
    """
    import pandas as pd
    from sklearn import datasets

    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    return df, iris
    # 23f3001440@ds.study.iitm.ac.in


# ---------------------------------------------------------
# Cell 2 — Interactive slider widget depending on df
# ---------------------------------------------------------
@app.cell
def cell2(df, iris):
    """
    Data flow:
    - Depends on df imported from Cell 1
    - Creates slider widget for selecting target class
    """
    import marimo as mo
    target_slider = mo.ui.slider(
        0,
        int(df["target"].max()),
        1,
        label="Select class:"
    )
    return target_slider


# ---------------------------------------------------------
# Cell 3 — Dynamic Markdown that reacts to slider updates
# ---------------------------------------------------------
@app.cell
def cell3(df, iris, target_slider):
    """
    Data flow:
    - Depends on df and slider
    - Displays live summary of selected subset
    """
    import marimo as mo
    t = target_slider.value
    subset = df[df["target"] == t]

    md = f"""
    ### 📌 Dynamic Summary for Class {t} — *{iris.target_names[t]}*
    - **Sample count:** {len(subset)}
    - **Mean sepal length:** {subset['sepal length (cm)'].mean():.3f}
    - **Mean sepal width:** {subset['sepal width (cm)'].mean():.3f}
    """
    return mo.md(md)


# ---------------------------------------------------------
# Cell 4 — Interactive plot depends on slider + df
# ---------------------------------------------------------
@app.cell
def cell4(df, target_slider):
    """
    Data flow:
    - Depends on df and slider
    - Scatter plot updates automatically when slider changes
    """
    import marimo as mo
    import matplotlib.pyplot as plt

    t = target_slider.value
    subset = df[df["target"] == t]

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(subset["sepal length (cm)"], subset["sepal width (cm)"], color="purple")
    ax.set_xlabel("sepal length (cm)")
    ax.set_ylabel("sepal width (cm)")
    ax.set_title(f"Scatter plot for class {t}")
    return mo.pyplot(fig)


# ---------------------------------------------------------
# Launch
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run()
