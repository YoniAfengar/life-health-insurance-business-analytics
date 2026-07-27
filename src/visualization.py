"""Reusable visualization and notebook display utilities."""

import html
import re

import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import HTML, display
from matplotlib.container import BarContainer
from matplotlib.ticker import FuncFormatter

from src.config import (
    BOXPLOT_SIZE,
    FIGURE_SIZE,
    FIGURES_DIR,
    HISTOGRAM_BINS,
    NUMERIC_COLUMNS,
)

# ---------------------------------------------------------------------------
# Visual theme
# ---------------------------------------------------------------------------

PRIMARY_COLOR = "#2563EB"
SECONDARY_COLOR = "#93C5FD"
ACCENT_COLOR = "#F59E0B"

SUCCESS_COLOR = "#10B981"
WARNING_COLOR = "#F59E0B"
PURPLE_COLOR = "#8B5CF6"

GRID_COLOR = "#D1D5DB"
TEXT_COLOR = "#1F2937"
MUTED_TEXT_COLOR = "#6B7280"
BACKGROUND_COLOR = "#FFFFFF"

INSIGHT_BACKGROUND = "#EFF6FF"
BUSINESS_BACKGROUND = "#ECFDF5"
LIMITATION_BACKGROUND = "#FFFBEB"
FUTURE_BACKGROUND = "#F5F3FF"


# ---------------------------------------------------------------------------
# General chart helpers
# ---------------------------------------------------------------------------


def _apply_chart_style() -> None:
    """Apply a consistent visual style across all charts."""
    plt.rcParams.update(
        {
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "axes.edgecolor": GRID_COLOR,
            "axes.labelcolor": TEXT_COLOR,
            "axes.titlecolor": TEXT_COLOR,
            "axes.titlesize": 16,
            "axes.titleweight": "bold",
            "axes.labelsize": 12,
            "xtick.color": TEXT_COLOR,
            "ytick.color": TEXT_COLOR,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "font.size": 11,
            "grid.color": GRID_COLOR,
            "grid.alpha": 0.45,
            "grid.linestyle": "--",
            "legend.frameon": False,
        }
    )


def _save_figure(
    fig: plt.Figure,
    filename: str,
) -> None:
    """Save a figure in the configured reports/figures directory."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    output_path = FIGURES_DIR / filename

    fig.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
    )


def _create_filename(value: str) -> str:
    """Convert text into a safe lowercase filename."""
    filename = re.sub(r"[^a-zA-Z0-9]+", "_", value)

    return filename.strip("_").lower()


def _format_large_number(
    value: float,
    _: int = 0,
) -> str:
    """Format large values using K and M notation."""
    absolute_value = abs(value)

    if absolute_value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"

    if absolute_value >= 1_000:
        return f"{value / 1_000:.1f}K"

    return f"{value:.0f}"


def _remove_chart_borders(axis: plt.Axes) -> None:
    """Remove unnecessary chart borders."""
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)
    axis.spines["left"].set_color(GRID_COLOR)
    axis.spines["bottom"].set_color(GRID_COLOR)


def _get_readable_name(column: str) -> str:
    """Convert a DataFrame column name into readable text."""
    return column.replace("_", " ")


def _validate_numeric_columns(df: pd.DataFrame) -> list[str]:
    """Return configured numerical columns that exist in the DataFrame."""
    columns = [column for column in NUMERIC_COLUMNS if column in df.columns]

    if not columns:
        raise ValueError(
            "None of the configured numerical columns exist in the DataFrame."
        )

    return columns


def _add_bar_labels(
    axis: plt.Axes,
    bars: BarContainer,
    horizontal: bool = False,
) -> None:
    """Add formatted values to bar charts."""
    for bar in bars:
        if horizontal:
            value = bar.get_width()

            axis.text(
                value,
                bar.get_y() + bar.get_height() / 2,
                f"  {_format_large_number(value)}",
                va="center",
                ha="left",
                fontsize=11,
                fontweight="bold",
                color=TEXT_COLOR,
            )

        else:
            value = bar.get_height()

            axis.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                _format_large_number(value),
                va="bottom",
                ha="center",
                fontsize=11,
                fontweight="bold",
                color=TEXT_COLOR,
            )


# ---------------------------------------------------------------------------
# Numerical-variable charts
# ---------------------------------------------------------------------------


def plot_numeric_histograms(df: pd.DataFrame) -> None:
    """Display and save histograms for configured numerical columns."""
    _apply_chart_style()

    columns = _validate_numeric_columns(df)

    fig, axes = plt.subplots(
        1,
        len(columns),
        figsize=FIGURE_SIZE,
        squeeze=False,
    )

    axes = axes.flatten()

    for axis, column in zip(
        axes,
        columns,
        strict=True,
    ):
        values = df[column].dropna()

        if values.empty:
            axis.set_visible(False)
            continue

        axis.hist(
            values,
            bins=HISTOGRAM_BINS,
            color=PRIMARY_COLOR,
            edgecolor=BACKGROUND_COLOR,
            linewidth=0.8,
            alpha=0.9,
        )

        median_value = values.median()

        axis.axvline(
            median_value,
            color=ACCENT_COLOR,
            linestyle="--",
            linewidth=2.3,
        )

        axis.text(
            median_value,
            axis.get_ylim()[1] * 0.93,
            f"Median: {_format_large_number(median_value)}",
            rotation=90,
            va="top",
            ha="right",
            fontsize=10,
            color=ACCENT_COLOR,
            fontweight="bold",
        )

        axis.set_title(
            _get_readable_name(column),
            pad=12,
        )

        axis.set_xlabel("")
        axis.set_ylabel("Number of Records")

        axis.grid(axis="y")
        axis.grid(axis="x", visible=False)

        _remove_chart_borders(axis)

        if column in {"Income", "Claim_Amount"}:
            axis.xaxis.set_major_formatter(FuncFormatter(_format_large_number))

    fig.suptitle(
        "Distribution of Numerical Variables",
        fontsize=19,
        fontweight="bold",
        color=TEXT_COLOR,
        y=1.02,
    )

    fig.tight_layout(
        rect=(0, 0, 1, 0.96),
    )

    _save_figure(
        fig,
        "numeric_histograms.png",
    )

    plt.show()
    plt.close(fig)


def plot_numeric_boxplots(df: pd.DataFrame) -> None:
    """Display and save boxplots for configured numerical columns."""
    _apply_chart_style()

    columns = _validate_numeric_columns(df)

    fig, axes = plt.subplots(
        1,
        len(columns),
        figsize=BOXPLOT_SIZE,
        squeeze=False,
    )

    axes = axes.flatten()

    for axis, column in zip(
        axes,
        columns,
        strict=True,
    ):
        values = df[column].dropna()

        if values.empty:
            axis.set_visible(False)
            continue

        axis.boxplot(
            values,
            patch_artist=True,
            widths=0.5,
            boxprops={
                "facecolor": SECONDARY_COLOR,
                "edgecolor": PRIMARY_COLOR,
                "linewidth": 1.6,
            },
            medianprops={
                "color": ACCENT_COLOR,
                "linewidth": 2.5,
            },
            whiskerprops={
                "color": PRIMARY_COLOR,
                "linewidth": 1.4,
            },
            capprops={
                "color": PRIMARY_COLOR,
                "linewidth": 1.4,
            },
            flierprops={
                "marker": "o",
                "markerfacecolor": PRIMARY_COLOR,
                "markeredgecolor": "none",
                "markersize": 3.5,
                "alpha": 0.3,
            },
        )

        axis.set_title(
            _get_readable_name(column),
            pad=12,
        )

        axis.set_xticks([])
        axis.grid(axis="y")
        axis.grid(axis="x", visible=False)

        _remove_chart_borders(axis)

        if column in {"Income", "Claim_Amount"}:
            axis.yaxis.set_major_formatter(FuncFormatter(_format_large_number))

    fig.suptitle(
        "Spread and Outliers of Numerical Variables",
        fontsize=19,
        fontweight="bold",
        color=TEXT_COLOR,
        y=1.02,
    )

    fig.tight_layout(
        rect=(0, 0, 1, 0.96),
    )

    _save_figure(
        fig,
        "numeric_boxplots.png",
    )

    plt.show()
    plt.close(fig)


# ---------------------------------------------------------------------------
# Correlation chart
# ---------------------------------------------------------------------------


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Display and save a correlation heatmap."""
    _apply_chart_style()

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        raise ValueError(
            "At least two numerical columns are required "
            "to create a correlation heatmap."
        )

    correlation = numeric_df.corr()

    fig, axis = plt.subplots(figsize=(8.5, 6.5))

    heatmap = axis.imshow(
        correlation,
        cmap="Blues",
        vmin=-1,
        vmax=1,
        aspect="auto",
    )

    axis.set_xticks(range(len(correlation.columns)))
    axis.set_yticks(range(len(correlation.columns)))

    axis.set_xticklabels(
        [_get_readable_name(column) for column in correlation.columns],
        rotation=35,
        ha="right",
    )

    axis.set_yticklabels([_get_readable_name(column) for column in correlation.columns])

    for row_index in range(len(correlation.columns)):
        for column_index in range(len(correlation.columns)):
            value = correlation.iloc[row_index, column_index]

            text_color = BACKGROUND_COLOR if abs(value) >= 0.55 else TEXT_COLOR

            axis.text(
                column_index,
                row_index,
                f"{value:.2f}",
                ha="center",
                va="center",
                color=text_color,
                fontsize=11,
                fontweight="bold",
            )

    colorbar = fig.colorbar(
        heatmap,
        ax=axis,
        fraction=0.046,
        pad=0.04,
    )

    colorbar.set_label(
        "Correlation Coefficient",
        color=TEXT_COLOR,
        fontsize=11,
    )

    axis.set_title(
        "Relationships Between Numerical Variables",
        fontsize=18,
        fontweight="bold",
        pad=18,
    )

    for spine in axis.spines.values():
        spine.set_visible(False)

    fig.tight_layout()

    _save_figure(
        fig,
        "correlation_heatmap.png",
    )

    plt.show()
    plt.close(fig)

    # ---------------------------------------------------------------------------


# Customer-group claim charts
# ---------------------------------------------------------------------------


def _create_group_summary(
    df: pd.DataFrame,
    group_column: str,
) -> pd.DataFrame:
    """Calculate median claim amount and group size."""
    return (
        df.groupby(
            group_column,
            observed=True,
            dropna=False,
        )["Claim_Amount"]
        .agg(
            median_claim="median",
            record_count="size",
        )
        .dropna(subset=["median_claim"])
        .sort_values("median_claim")
    )


def _plot_two_group_kpi_comparison(
    summary: pd.DataFrame,
    readable_column: str,
) -> plt.Figure:
    """Create KPI cards for a two-category comparison."""
    labels = summary.index.astype(str).tolist()
    values = summary["median_claim"].astype(float).tolist()
    counts = summary["record_count"].astype(int).tolist()

    difference = abs(values[1] - values[0])
    baseline = min(abs(values[0]), abs(values[1]))

    if baseline > 0:
        difference_percentage = difference / baseline * 100
    else:
        difference_percentage = 0.0

    fig, axis = plt.subplots(figsize=(10, 5.5))

    axis.set_xlim(0, 1)
    axis.set_ylim(0, 1)
    axis.axis("off")

    card_positions = [0.28, 0.72]

    for position, label, value, count in zip(
        card_positions,
        labels,
        values,
        counts,
        strict=True,
    ):
        axis.text(
            position,
            0.63,
            _format_large_number(value),
            ha="center",
            va="center",
            fontsize=30,
            fontweight="bold",
            color=PRIMARY_COLOR,
            bbox={
                "boxstyle": "round,pad=0.75",
                "facecolor": INSIGHT_BACKGROUND,
                "edgecolor": SECONDARY_COLOR,
                "linewidth": 1.6,
            },
        )

        axis.text(
            position,
            0.36,
            label,
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            color=TEXT_COLOR,
        )

        axis.text(
            position,
            0.27,
            f"n = {count:,}",
            ha="center",
            va="center",
            fontsize=10,
            color=MUTED_TEXT_COLOR,
        )

    axis.text(
        0.5,
        0.10,
        (
            "Difference in median claim amount: "
            f"{_format_large_number(difference)} "
            f"({difference_percentage:.1f}%)"
        ),
        ha="center",
        va="center",
        fontsize=11,
        color=MUTED_TEXT_COLOR,
    )

    axis.set_title(
        f"Median Claim Amount by {readable_column}",
        fontsize=18,
        fontweight="bold",
        pad=20,
        color=TEXT_COLOR,
    )

    return fig


def _plot_vertical_group_bars(
    summary: pd.DataFrame,
    readable_column: str,
) -> plt.Figure:
    """Create a vertical bar chart for a small number of groups."""
    fig, axis = plt.subplots(figsize=(9.5, 6.5))

    labels = [
        f"{label}\n(n={count:,})"
        for label, count in zip(
            summary.index.astype(str),
            summary["record_count"],
            strict=True,
        )
    ]

    bars = axis.bar(
        labels,
        summary["median_claim"],
        color=PRIMARY_COLOR,
        width=0.58,
        alpha=0.95,
    )

    _add_bar_labels(
        axis,
        bars,
        horizontal=False,
    )

    maximum = summary["median_claim"].max()

    axis.set_ylim(
        0,
        maximum * 1.18,
    )

    axis.set_title(
        f"Median Claim Amount by {readable_column}",
        fontsize=18,
        fontweight="bold",
        pad=16,
    )

    axis.set_xlabel(readable_column)
    axis.set_ylabel("Median Claim Amount")

    axis.yaxis.set_major_formatter(FuncFormatter(_format_large_number))

    axis.grid(axis="y")
    axis.grid(axis="x", visible=False)

    _remove_chart_borders(axis)

    return fig


def _plot_horizontal_group_bars(
    summary: pd.DataFrame,
    readable_column: str,
) -> plt.Figure:
    """Create a horizontal bar chart for many groups."""
    fig, axis = plt.subplots(figsize=(10.5, max(5.5, len(summary) * 0.78)))

    labels = [
        f"{label} (n={count:,})"
        for label, count in zip(
            summary.index.astype(str),
            summary["record_count"],
            strict=True,
        )
    ]

    bars = axis.barh(
        labels,
        summary["median_claim"],
        color=PRIMARY_COLOR,
        height=0.6,
        alpha=0.95,
    )

    _add_bar_labels(
        axis,
        bars,
        horizontal=True,
    )

    maximum = summary["median_claim"].max()

    axis.set_xlim(
        0,
        maximum * 1.18,
    )

    axis.set_title(
        f"Median Claim Amount by {readable_column}",
        fontsize=18,
        fontweight="bold",
        pad=16,
    )

    axis.set_xlabel("Median Claim Amount")
    axis.set_ylabel("")

    axis.xaxis.set_major_formatter(FuncFormatter(_format_large_number))

    axis.grid(axis="x")
    axis.grid(axis="y", visible=False)

    _remove_chart_borders(axis)

    return fig


def plot_claims_by_group(
    df: pd.DataFrame,
    group_column: str,
) -> None:
    """
    Display and save median claim amounts by customer group.

    Two groups are displayed as KPI cards.
    Three or four groups use vertical bars.
    Five or more groups use horizontal bars.

    Group sample sizes are included to support responsible interpretation.
    """
    _apply_chart_style()

    required_columns = {
        group_column,
        "Claim_Amount",
    }

    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    summary = _create_group_summary(
        df,
        group_column,
    )

    if summary.empty:
        raise ValueError(f"No valid data is available for {group_column}.")

    readable_column = _get_readable_name(group_column)

    if len(summary) == 2:
        fig = _plot_two_group_kpi_comparison(
            summary,
            readable_column,
        )

    elif len(summary) <= 4:
        fig = _plot_vertical_group_bars(
            summary,
            readable_column,
        )

    else:
        fig = _plot_horizontal_group_bars(
            summary,
            readable_column,
        )

    fig.tight_layout()

    filename = f"claim_amount_by_{_create_filename(group_column)}.png"

    _save_figure(
        fig,
        filename,
    )

    plt.show()
    plt.close(fig)


# ---------------------------------------------------------------------------
# Category-distribution charts
# ---------------------------------------------------------------------------


def plot_category_distribution(
    df: pd.DataFrame,
    column: str,
    chart_type: str = "bar",
) -> None:
    """
    Display and save category frequencies.

    Supported chart types:
    - bar
    - donut
    """
    _apply_chart_style()

    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

    counts = df[column].fillna("Missing").astype(str).value_counts()

    if counts.empty:
        raise ValueError(f"No valid data is available for {column}.")

    readable_column = _get_readable_name(column)
    normalized_chart_type = chart_type.lower().strip()

    if normalized_chart_type == "donut":
        if len(counts) > 6:
            raise ValueError("Donut charts should contain no more than six categories.")

        fig, axis = plt.subplots(figsize=(8.5, 6.5))

        _, _, percentage_labels = axis.pie(
            counts.values,
            labels=counts.index,
            autopct="%1.1f%%",
            startangle=90,
            counterclock=False,
            wedgeprops={
                "width": 0.42,
                "edgecolor": BACKGROUND_COLOR,
                "linewidth": 2,
            },
            textprops={
                "color": TEXT_COLOR,
                "fontsize": 11,
            },
        )

        for percentage_label in percentage_labels:
            percentage_label.set_fontweight("bold")
            percentage_label.set_fontsize(10)

        axis.text(
            0,
            0.04,
            f"{counts.sum():,}",
            ha="center",
            va="center",
            fontsize=22,
            fontweight="bold",
            color=TEXT_COLOR,
        )

        axis.text(
            0,
            -0.10,
            "Records",
            ha="center",
            va="center",
            fontsize=11,
            color=MUTED_TEXT_COLOR,
        )

        axis.set_title(
            f"{readable_column} Distribution",
            fontsize=18,
            fontweight="bold",
            pad=18,
        )

        axis.axis("equal")

    elif normalized_chart_type == "bar":
        horizontal = len(counts) > 4

        if horizontal:
            counts = counts.sort_values()

            fig, axis = plt.subplots(figsize=(10.5, max(5.5, len(counts) * 0.72)))

            bars = axis.barh(
                counts.index,
                counts.values,
                color=PRIMARY_COLOR,
                height=0.6,
            )

            _add_bar_labels(
                axis,
                bars,
                horizontal=True,
            )

            axis.set_xlim(
                0,
                counts.max() * 1.17,
            )

            axis.set_xlabel("Number of Records")
            axis.set_ylabel("")

            axis.xaxis.set_major_formatter(FuncFormatter(_format_large_number))

            axis.grid(axis="x")
            axis.grid(axis="y", visible=False)

        else:
            fig, axis = plt.subplots(figsize=(9.5, 6.5))

            bars = axis.bar(
                counts.index,
                counts.values,
                color=PRIMARY_COLOR,
                width=0.58,
            )

            _add_bar_labels(
                axis,
                bars,
                horizontal=False,
            )

            axis.set_ylim(
                0,
                counts.max() * 1.17,
            )

            axis.set_xlabel(readable_column)
            axis.set_ylabel("Number of Records")

            axis.yaxis.set_major_formatter(FuncFormatter(_format_large_number))

            axis.grid(axis="y")
            axis.grid(axis="x", visible=False)

        axis.set_title(
            f"{readable_column} Distribution",
            fontsize=18,
            fontweight="bold",
            pad=16,
        )

        _remove_chart_borders(axis)

    else:
        raise ValueError("chart_type must be either 'bar' or 'donut'.")

    fig.tight_layout()

    filename = f"{_create_filename(column)}_distribution_{normalized_chart_type}.png"

    _save_figure(
        fig,
        filename,
    )

    plt.show()
    plt.close(fig)

    # ---------------------------------------------------------------------------


# Styled notebook message boxes
# ---------------------------------------------------------------------------


def _show_message_box(
    title: str,
    text: str,
    icon: str,
    background_color: str,
    border_color: str,
    title_color: str,
) -> None:
    """Display a consistently styled message box in Jupyter."""
    safe_title = html.escape(title)

    safe_text = html.escape(text)
    safe_text = safe_text.replace("\n\n", "<br><br>")
    safe_text = safe_text.replace("\n", "<br>")

    display(
        HTML(
            f"""
            <div style="
                width:100%;
                box-sizing:border-box;
                background-color:{background_color};
                border-left:8px solid {border_color};
                padding:22px 26px;
                border-radius:10px;
                margin:18px 0 26px 0;
                box-shadow:0 3px 10px rgba(0, 0, 0, 0.07);
                font-family:inherit;
            ">
                <div style="
                    display:flex;
                    align-items:center;
                    gap:10px;
                    margin-bottom:10px;
                    color:{title_color};
                    font-size:19px;
                    font-weight:700;
                    line-height:1.3;
                ">
                    <span
                        aria-hidden="true"
                        style="font-size:20px;"
                    >
                        {icon}
                    </span>

                    <span>{safe_title}</span>
                </div>

                <div style="
                    color:{TEXT_COLOR};
                    font-size:17px;
                    line-height:1.75;
                    font-weight:400;
                ">
                    {safe_text}
                </div>
            </div>
            """
        )
    )


def show_key_insight(text: str) -> None:
    """Display a blue analytical-insight box."""
    _show_message_box(
        title="Key Insight",
        text=text,
        icon="💡",
        background_color=INSIGHT_BACKGROUND,
        border_color=PRIMARY_COLOR,
        title_color="#1E3A8A",
    )


def show_business_finding(text: str) -> None:
    """Display a green business-finding box."""
    _show_message_box(
        title="Business Finding",
        text=text,
        icon="📊",
        background_color=BUSINESS_BACKGROUND,
        border_color=SUCCESS_COLOR,
        title_color="#065F46",
    )


def show_limitation(text: str) -> None:
    """Display an orange limitation box."""
    _show_message_box(
        title="Limitation",
        text=text,
        icon="⚠️",
        background_color=LIMITATION_BACKGROUND,
        border_color=WARNING_COLOR,
        title_color="#92400E",
    )


def show_future_work(text: str) -> None:
    """Display a purple future-work box."""
    _show_message_box(
        title="Future Work",
        text=text,
        icon="🚀",
        background_color=FUTURE_BACKGROUND,
        border_color=PURPLE_COLOR,
        title_color="#5B21B6",
    )
