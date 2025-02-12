
def plot_gain_chart(y_test, y_pred, n_bins=10):
    """
    Plots a gain chart for a regression model.
    
    Parameters:
        y_test (array-like): Actual target values.
        y_pred (array-like): Predicted target values.
        n_bins (int): Number of bins/quantiles to group the data (default: 10).
    
    Returns:
        None: Displays the gain chart.
    """
    # Combine actual and predicted values into a DataFrame
    results = pd.DataFrame({
        'Actual': y_test,
        'Predicted': y_pred
    })

    # Sort by predicted values
    results = results.sort_values(by='Predicted', ascending=False).reset_index(drop=True)

    # Calculate cumulative sums for actual and predicted values
    results['Cumulative_Actual'] = results['Actual'].cumsum()
    results['Cumulative_Predicted'] = results['Predicted'].cumsum()

    # Normalize cumulative sums to percentage of total
    results['Cumulative_Actual_Percent'] = results['Cumulative_Actual'] / results['Actual'].sum() * 100
    results['Cumulative_Predicted_Percent'] = results['Cumulative_Predicted'] / results['Predicted'].sum() * 100
    results['Percentage_of_Data'] = np.linspace(1 / len(results), 1, len(results)) * 100

    # Plot the gain chart
    plt.figure(figsize=(10, 6))
    plt.plot(results['Percentage_of_Data'], results['Cumulative_Predicted_Percent'], label='Predicted', marker='o')
    plt.plot(results['Percentage_of_Data'], results['Cumulative_Actual_Percent'], label='Actual', marker='s')
    plt.title("Gain Chart")
    plt.xlabel("Percentage of Data")
    plt.ylabel("Cumulative Percentage")
    plt.legend()
    plt.grid()
    plt.show()

