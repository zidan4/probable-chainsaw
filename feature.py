importances = model.feature_importances_
features = X.columns

# Sort feature importance
sorted_indices = importances.argsort()[::-1]

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=importances[sorted_indices], y=features[sorted_indices], palette="viridis")
plt.title("Feature Importance")
plt.show()
