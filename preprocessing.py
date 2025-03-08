from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Convert categorical variables
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
label_encoder = LabelEncoder()

for col in df.select_dtypes(include=["object"]).columns:
    df[col] = label_encoder.fit_transform(df[col])

# Split data
X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
