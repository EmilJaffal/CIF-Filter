import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
from matplotlib.colors import Normalize

# Define the element_prevalence function
def element_prevalence(
    elem_tracker,
    name="ptable",
    save_dir="output",
    log_scale=False,
    ptable_fig=True,
):
    current_dir = os.path.dirname(os.path.abspath(__file__))  
    cif_filter_dir = os.path.dirname(current_dir)  
    ptable_path = os.path.join(cif_filter_dir, "ptable.csv") 

    ptable = pd.read_csv(ptable_path)
    ptable.index = ptable["symbol"].values

    n_row = ptable["row"].max()
    n_column = ptable["column"].max()

    if ptable_fig:
        fig, ax = plt.subplots(figsize=(n_column, n_row))
        rows = ptable["row"]
        columns = ptable["column"]
        symbols = ptable["symbol"]
        rw = 1.0  # rectangle width (rw)
        rh = 1.0  # rectangle height (rh)
        for row, column, symbol in zip(rows, columns, symbols):
            row = ptable["row"].max() - row
            cmap = cm.GnBu  # Color
            count_min = elem_tracker.min()
            count_max = elem_tracker.max()
            count_max = count_max + 24

            norm = Normalize(vmin=count_min, vmax=count_max)
            count = elem_tracker[symbol]

            if log_scale:
                norm = Normalize(vmin=np.log(1), vmax=np.log(count_max))
                if count != 0:
                    count = np.log(count)
            color = cmap(norm(count))
            if count == 0:
                color = "white"
            if 0 < count <= 10:
                color = "lightyellow"
            rect = patches.Rectangle(
                (column, row),
                rw,
                rh,
                linewidth=2,
                edgecolor="black",
                facecolor=color,
                alpha=1,
            )

            plt.text(
                column + rw / 2,
                row + rw / 2,
                symbol,
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=20,
                fontweight="semibold",
                color="black",
            )
            ax.add_patch(rect)

        granularity = 20
        for i in range(granularity):
            value = int(round((i) * count_max / (granularity - 1)))
            if log_scale:
                if value != 0:
                    value = np.log(value)
            color = cmap(norm(value))
            if value == 0:
                color = "white"  # white
            if 0 < value <= 40:
                color = "lightyellow"
            length = 9
            x_offset = 3.5
            y_offset = 9.5  # 7.8
            x_loc = i / (granularity) * length + x_offset
            width = length / granularity
            height = 0.35
            rect = patches.Rectangle(
                (x_loc, y_offset),
                width,
                height,
                linewidth=1.5,
                edgecolor="gray",
                facecolor=color,
                alpha=1,
            )

            if i in [0, 4, 9, 14, 19]:
                text = f"{value:0.0f}"
                if log_scale:
                    text = f"{np.exp(value):0.1e}".replace("+", "")
                plt.text(
                    x_loc + width / 2,
                    y_offset - 0.4,
                    text,
                    horizontalalignment="center",
                    verticalalignment="center",
                    fontweight="semibold",
                    fontsize=20,
                    color="k",
                )

            ax.add_patch(rect)

        plt.text(
            x_offset + length / 2,
            y_offset + 0.7,
            "log(Element Count)" if log_scale else "Element Count",
            horizontalalignment="center",
            verticalalignment="center",
            fontweight="semibold",
            fontsize=20,
            color="k",
        )

        ax.set_ylim(-0.15, n_row + 0.1)
        ax.set_xlim(0.15, n_column + 4.5)

        # fig.patch.set_visible(False)
        ax.axis("off")

        if save_dir is not None:
            base_name = os.path.basename(os.path.normpath(name))
            file_name = (
                f"{base_name}_ptable.png"
                if not base_name.endswith("_ptable")
                else f"{base_name}.png"
            )
            fig_name = os.path.join(save_dir, file_name)
            os.makedirs(save_dir, exist_ok=True)
            plt.savefig(fig_name, format="png", bbox_inches="tight", dpi=600)

        plt.draw()
        plt.pause(0.001)
        plt.close()
