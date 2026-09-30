from sklearn.ensemble import RandomForestRegressor

# Initialize the model
model = RandomForestRegressor()

# Train the model using the predictor variables
model.fit(predictor_vars, target_var)