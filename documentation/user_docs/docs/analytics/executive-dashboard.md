# Executive Dashboard

The **Analytics Dashboard** provides a comprehensive, high-level view of your reconciliation operations, allowing you to track performance, identify trends, and spot inefficiencies.

## Overview Metrics

The core KPIs at the top of the dashboard give you an instant pulse on your system's health.

![Analytics Overview Statistics](../assets/analytics_overview.png)

*   **Total Volume**: The total number of transactions processed.
*   **Success Rate**: The percentage of records successfully matched.
*   **Exception Rate**: The percentage of records requiring manual intervention.
*   **Processing Time**: average time taken to process a batch or record.

## Period Comparison

Analyze your performance over time by comparing current metrics against historical data.

![Period Comparison](../assets/analytics_period_comparison.png)

*   **Timeframes**: Switch between *Week*, *Month*, and *Year* views to see short-term fluctuations or long-term growth.
*   **Trend Indicators**: Visual cues (e.g., percentage changes) highlight whether metrics are improving or declining.

## Visual Trends and Distribution

Deep dive into the data with interactive charts.

![Volume and Accuracy Trends](../assets/analytics_trends.png)

*   **Volume & Accuracy Trends**: A dual-axis chart showing the correlation between transaction volume and match accuracy over the selected period.
*   **Match Type Distribution**: A stacked bar chart visualizing *how* records are being matched (e.g., *One-to-One*, *One-to-Many*) over time.

### Weekly Performance Trends
Track the detailed relationship between volume and accuracy on a weekly basis.

![Weekly Performance Trends](../assets/analytics_weekly_trends.png)

This line graph overlays **Accuracy** (green) and **Volume** (purple) to help correlations between high-load periods and matching efficiency.

## Performance Analysis

Understand the operational efficiency of your pipelines.

![Performance Analysis](../assets/analytics_performance.png)

*   **Reconciliation Processing Time**: A line graph tracking the speed of your reconciliation jobs, helping you identify performance bottlenecks.
*   **Reconciliation Status**: A pie chart offering a breakdown of match categories (e.g., *Exact*, *Tolerated Date*, *Manual Match*).

### Job & Reconciliation Insights

Gain granular visibility into job performance and result composition.

![Job Performance and Reconciliation Trends](../assets/analytics_job_stats.png)

*   **Reconciliation Trends**: A pie chart breaking down results into *Matches*, *Mismatches*, and *Unmatched* records.
*   **Job Performance**: A scatter plot correlating **Volume** vs. **Accuracy**, helping to identify outlying jobs that had high volume but low accuracy (or vice versa).

### Real-time Throughput

Monitor the engine's processing capabilities in real-time.

![Real-time Throughput](../assets/analytics_throughput.png)

This multi-metric bar chart visualizes:

*   **Job Count**
*   **Accuracy**
*   **Volume**
*   **Duration** (Avg)
*   Result Counts (**Matches**, **Mismatches**, **Unmatched**)
